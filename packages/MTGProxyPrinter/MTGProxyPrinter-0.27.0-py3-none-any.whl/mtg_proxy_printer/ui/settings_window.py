# Copyright (C) 2020-2024 Thomas Hess <thomas.hess@udo.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import configparser
import logging
import pathlib
import typing

from PyQt5.QtCore import QStringListModel, pyqtSignal as Signal, pyqtSlot as Slot, Qt, QUrl, QStandardPaths, QThreadPool
from PyQt5.QtWidgets import QDialogButtonBox, QCheckBox, QApplication, \
    QFileDialog, QLineEdit, QMessageBox, QWidget, QDialog
from PyQt5.QtGui import QDesktopServices, QIcon

import mtg_proxy_printer.app_dirs
from mtg_proxy_printer.model.document import Document
from mtg_proxy_printer.printing_filter_updater import PrintingFilterUpdater
from mtg_proxy_printer.document_controller import DocumentAction
from mtg_proxy_printer.document_controller.edit_document_settings import ActionEditDocumentSettings

import mtg_proxy_printer.settings
from mtg_proxy_printer.logger import get_logger

try:
    from mtg_proxy_printer.ui.generated.settings_window.settings_window import Ui_SettingsWindow
except ModuleNotFoundError:
    from mtg_proxy_printer.ui.common import load_ui_from_file
    Ui_SettingsWindow = load_ui_from_file("settings_window/settings_window")

logger = get_logger(__name__)
del get_logger
__all__ = [
    "SettingsWindow",
]
CheckState = Qt.CheckState
bool_to_check_state: typing.Dict[typing.Optional[bool], CheckState] = {
    True: CheckState.Checked,
    False: CheckState.Unchecked,
    None: CheckState.PartiallyChecked,
}
check_state_to_bool_str: typing.Dict[CheckState, str] = {v: str(k) for k, v in bool_to_check_state.items()}
QueuedConnection = Qt.ConnectionType.QueuedConnection


class SettingsWindow(QDialog):
    """Implements the Settings window."""
    saved = Signal()
    preferred_language_changed = Signal(str)
    document_settings_updated = Signal(DocumentAction)
    error_occurred = Signal(str)
    requested_card_download = Signal(pathlib.Path)
    long_running_process_begins = Signal(int, str)
    process_updated = Signal(int)
    process_finished = Signal()

    def __init__(self, language_model: QStringListModel, document: Document, parent: QWidget = None):
        super().__init__(parent)
        self.ui = ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.language_model = language_model
        self.document = document
        self.card_db = document.card_db
        self.requested_card_download.connect(lambda _: ui.debug_download_card_data_as_file.setEnabled(False))
        ui.preferred_language_combo_box.setModel(self.language_model)
        ui.page_configuration_group_box.setTitle("Default settings for new documents")
        ui.add_card_widget_style_combo_box.addItem("Horizontal layout", "horizontal")
        ui.add_card_widget_style_combo_box.addItem("Columnar layout", "columnar")
        ui.add_card_widget_style_combo_box.addItem("Tabbed layout", "tabbed")

        ui.log_level_combo_box.addItems(map(logging.getLevelName, range(10, 60, 10)))

        self._setup_button_box()
        logger.info(f"Created {self.__class__.__name__} instance.")

    def _setup_button_box(self):
        StandardButton = QDialogButtonBox.StandardButton
        button_box = self.ui.button_box
        button_box.button(StandardButton.RestoreDefaults).clicked.connect(self.restore_defaults)
        button_box.button(StandardButton.Reset).clicked.connect(self.reset)
        buttons_with_icons = [
            (StandardButton.Reset, "edit-undo"),
            (StandardButton.Save, "document-save"),
            (StandardButton.Cancel, "dialog-cancel"),
            (StandardButton.RestoreDefaults, "document-revert"),
        ]
        for role, icon in buttons_with_icons:
            button = button_box.button(role)
            if button.icon().isNull():
                button.setIcon(QIcon.fromTheme(icon))

    def show(self):
        logger.info("Show the settings window.")
        self.load_settings(mtg_proxy_printer.settings.settings)
        super(SettingsWindow, self).show()

    def load_settings(self, settings: configparser.ConfigParser):
        logger.debug("Loading the settings")
        self._load_look_and_feel_settings(settings)
        self._load_images_settings(settings)
        self._load_card_filter_settings(settings)
        self.ui.page_configuration_group_box.load_document_settings_from_config(settings)
        self._load_document_settings(settings)
        self._load_save_path_settings(settings)
        self._load_debug_settings(settings)
        self._load_print_guessing_settings(settings)
        self._load_update_check_settings(settings)
        self._load_printer_settings(settings)
        logger.debug("Finished loading settings")

    def _load_update_check_settings(self, settings: configparser.ConfigParser):
        section = settings["application"]
        for widget, setting in self._get_update_check_settings_widgets():
            widget.setCheckState(bool_to_check_state[section.getboolean(setting)])

    def _load_look_and_feel_settings(self, settings: configparser.ConfigParser):
        gui_section = settings["gui"]
        search_layout_index = self.ui.add_card_widget_style_combo_box.findData(gui_section["central-widget-layout"])
        self.ui.add_card_widget_style_combo_box.setCurrentIndex(search_layout_index)

    def _load_images_settings(self, settings: configparser.ConfigParser):
        images_section = settings["images"]
        preferred_language_combo_box = self.ui.preferred_language_combo_box
        preferred_language = images_section.get("preferred-language")
        if not (known := preferred_language_combo_box.model().stringList()) or preferred_language not in known:
            preferred_language_combo_box.addItem(preferred_language)
        preferred_language_combo_box.setCurrentIndex(self.get_index_for_language_code(preferred_language))
        self.ui.automatically_add_opposing_faces.setChecked(
            images_section.getboolean("automatically-add-opposing-faces")
        )

    def _load_document_settings(self, settings: configparser.ConfigParser):
        document_section = settings["documents"]
        self.ui.pdf_page_count_limit.setValue(document_section.getint("pdf-page-count-limit"))

    def _load_card_filter_settings(self, settings: configparser.ConfigParser):
        section = settings["card-filter"]
        self.ui.set_filter_settings.setPlainText(section["hidden-sets"])
        self.ui.card_filter_general_settings.load_settings(section)
        self.ui.card_filter_format_settings.load_settings(section)

    def _load_save_path_settings(self, settings: configparser.ConfigParser):
        section = settings["default-filesystem-paths"]
        widgets_with_settings = self._get_save_path_settings_widgets()
        for widget, setting in widgets_with_settings:
            widget.setText(section[setting])

    def _load_debug_settings(self, settings: configparser.ConfigParser):
        section = settings["debug"]
        for widget, setting in self._get_debug_settings_checkbox_widgets():
            widget.setChecked(section.getboolean(setting))
        log_level_combo_box = self.ui.log_level_combo_box
        log_level_combo_box.setCurrentIndex(log_level_combo_box.findText(section["log-level"]))

    def _load_printer_settings(self, settings: configparser.ConfigParser):
        section = settings["printer"]
        for widget, setting in self._get_printer_settings_widgets():
            widget.setChecked(section.getboolean(setting))

    def _load_print_guessing_settings(self, settings: configparser.ConfigParser):
        section = settings["decklist-import"]
        for widget, setting in self._get_print_guessing_checkbox_widgets():
            widget.setChecked(section.getboolean(setting))

    def _get_update_check_settings_widgets(self):
        ui = self.ui
        widgets_with_settings: typing.List[typing.Tuple[QCheckBox, str]] = [
            (ui.check_application_updates_enabled, "check-for-application-updates"),
            (ui.check_card_data_updates_enabled, "check-for-card-data-updates"),
        ]
        return widgets_with_settings

    def _get_save_path_settings_widgets(self):
        ui = self.ui
        widgets_with_settings: typing.List[typing.Tuple[QLineEdit, str]] = [
            (ui.document_save_path, "document-save-path"),
            (ui.pdf_save_path, "pdf-export-path"),
            (ui.deck_list_search_path, "deck-list-search-path"),
        ]
        return widgets_with_settings

    def _get_debug_settings_checkbox_widgets(self):
        ui = self.ui
        widgets_with_settings: typing.List[typing.Tuple[QCheckBox, str]] = [
            (ui.enable_cutelog_integration, "cutelog-integration"),
            (ui.enable_write_log_file, "write-log-file")
        ]
        return widgets_with_settings

    def _get_print_guessing_checkbox_widgets(self):
        ui = self.ui
        widgets_with_settings: typing.List[typing.Tuple[QCheckBox, str]] = [
            (ui.print_guessing_enable, "enable-print-guessing-by-default"),
            (ui.print_guessing_prefer_already_downloaded, "prefer-already-downloaded-images"),
            (ui.automatic_deck_list_translation_enable, "always-translate-deck-lists"),
        ]
        return widgets_with_settings

    def _get_printer_settings_widgets(self):
        ui = self.ui
        widgets_with_settings: typing.List[typing.Tuple[QCheckBox, str]] = [
            (ui.printer_use_borderless_printing, "borderless-printing")
        ]
        return widgets_with_settings

    def accept(self):
        """Automatically called when the user hits the "Save" button."""
        logger.info("User wants to save the settings.")
        old_preferred_language = mtg_proxy_printer.settings.settings["images"]["preferred-language"]
        new_preferred_language = self.ui.preferred_language_combo_box.currentText()
        if old_preferred_language != new_preferred_language:
            self.preferred_language_changed.emit(new_preferred_language)
        old_layout = self.document.page_layout
        new_layout = self.ui.page_configuration_group_box.page_layout
        if old_layout != new_layout and QMessageBox.question(
                self, "Apply settings to the current document?",
                "The new default settings differ from the settings used by the current document.\n"
                "Apply the new settings to the current document?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes
        ) == QMessageBox.StandardButton.Yes:
            logger.info("User applies changed document settings to the current document")
            self.document_settings_updated.emit(ActionEditDocumentSettings(new_layout))
        self.save()
        super(SettingsWindow, self).accept()

    def reset(self):
        logger.info("User reverts the made changes.")
        self.load_settings(mtg_proxy_printer.settings.settings)

    def reject(self):
        """Automatically called when the user hits the "Cancel" button or closes the settings window."""
        logger.info("User closes the settings dialog. This will reset any made changes.")
        self.reset()
        super(SettingsWindow, self).reject()

    def save(self):
        logger.info("User saves the configuration to disk.")
        self._save_look_and_feel_settings()
        self._save_images_settings()
        self._save_card_filter_settings()
        self.ui.page_configuration_group_box.save_document_settings_to_config()
        self._save_documents_settings()
        self._save_save_path_settings()
        self._save_debug_settings()
        self._save_print_guessing_settings()
        self._save_update_check_settings()
        self._save_printer_settings()
        logger.debug("Settings read from UI widgets, about to write the configuration to disk.")
        mtg_proxy_printer.settings.write_settings_to_file()
        self.saved.emit()
        logger.debug("Save finished.")

    def _save_update_check_settings(self):
        section = mtg_proxy_printer.settings.settings["application"]
        for widget, setting in self._get_update_check_settings_widgets():
            section[setting] = check_state_to_bool_str[widget.checkState()]

    def _save_look_and_feel_settings(self):
        gui_section = mtg_proxy_printer.settings.settings["gui"]
        gui_section["central-widget-layout"] = self.ui.add_card_widget_style_combo_box.currentData(
            Qt.ItemDataRole.UserRole)

    def _save_images_settings(self):
        images_section = mtg_proxy_printer.settings.settings["images"]
        images_section["preferred-language"] = self.ui.preferred_language_combo_box.currentText()
        images_section["automatically-add-opposing-faces"] = str(self.ui.automatically_add_opposing_faces.isChecked())

    def _save_card_filter_settings(self):
        section = mtg_proxy_printer.settings.settings["card-filter"]
        self.ui.card_filter_general_settings.save_settings(section)
        self.ui.card_filter_format_settings.save_settings(section)
        section["hidden-sets"] = self.ui.set_filter_settings.toPlainText()
        updater = PrintingFilterUpdater(self.card_db)
        updater.connect_progress_signals(self.long_running_process_begins, self.process_updated, self.process_finished)
        updater.signals.error_occurred.connect(self.error_occurred, QueuedConnection)
        QThreadPool.globalInstance().start(updater)

    def _save_documents_settings(self):
        documents_section = mtg_proxy_printer.settings.settings["documents"]
        documents_section["pdf-page-count-limit"] = str(self.ui.pdf_page_count_limit.value())

    def _save_save_path_settings(self):
        section = mtg_proxy_printer.settings.settings["default-filesystem-paths"]
        widgets_and_settings = self._get_save_path_settings_widgets()
        for widget, setting in widgets_and_settings:
            section[setting] = widget.text()

    def _save_debug_settings(self):
        debug_section = mtg_proxy_printer.settings.settings["debug"]
        for widget, setting in self._get_debug_settings_checkbox_widgets():
            debug_section[setting] = str(widget.isChecked())
        debug_section["log-level"] = self.ui.log_level_combo_box.currentText()

    def _save_print_guessing_settings(self):
        section = mtg_proxy_printer.settings.settings["decklist-import"]
        for widget, setting in self._get_print_guessing_checkbox_widgets():
            section[setting] = str(widget.isChecked())

    def _save_printer_settings(self):
        section = mtg_proxy_printer.settings.settings["printer"]
        for widget, setting in self._get_printer_settings_widgets():
            section[setting] = str(widget.isChecked())

    def restore_defaults(self):
        logger.info("User resets the configuration to the default settings.")
        self.load_settings(mtg_proxy_printer.settings.DEFAULT_SETTINGS)
        logger.debug("Loaded DEFAULT_SETTINGS.")

    def get_index_for_language_code(self, language: str):
        languages = self.language_model.stringList()
        if language in languages:
            return languages.index(language)
        else:
            return languages.index("en")

    @Slot()
    def on_document_save_path_browse_button_clicked(self):
        logger.debug("User about to select a new default document save path.")
        if location := QFileDialog.getExistingDirectory(self, "Select default save location"):
            logger.info("User selected a new default document save path.")
            self.ui.document_save_path.setText(location)

    @Slot()
    def on_pdf_save_path_browse_button_clicked(self):
        logger.debug("User about to select a new default PDF document export path.")
        if location := QFileDialog.getExistingDirectory(self, "Select default PDF export location"):
            logger.info("User selected a new default PDF document export path.")
            self.ui.pdf_save_path.setText(location)

    @Slot()
    def on_deck_list_search_path_browse_button_clicked(self):
        logger.debug("User about to select a new default deck list search path.")
        if location := QFileDialog.getExistingDirectory(self, "Select default deck list search path"):
            logger.info("User selected a new default deck list search path.")
            self.ui.deck_list_search_path.setText(location)

    @Slot()
    def on_open_debug_log_location_clicked(self):
        logger.debug("About to open the log directory using the default file manager.")
        log_dir = mtg_proxy_printer.app_dirs.data_directories.user_log_dir
        log_url = QUrl.fromLocalFile(log_dir)
        QDesktopServices.openUrl(log_url)

    @Slot()
    def on_debug_download_card_data_as_file_clicked(self):
        logger.debug("User about to download the card data from Scryfall to a file.")
        location = QFileDialog.getExistingDirectory(
            self, "Select download location",
            QStandardPaths.locate(QStandardPaths.DownloadLocation, "", QStandardPaths.LocateDirectory))
        if not location:
            logger.debug("User cancelled location selection. Not downloading.")
            return
        if not (path := pathlib.Path(location)).is_dir():
            QMessageBox.critical(
                self, "Selected location is not a directory",
                f"Cannot write the card data at the given location, because it is not a directory:\n{location}",
                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            return
        logger.info(f"Download card data to file {path}")
        self.requested_card_download.emit(path)

    @Slot()
    def on_debug_import_card_data_from_file_clicked(self):
        logger.debug("User about to import card tata from a previously downloaded file.")
        location, _ = QFileDialog.getOpenFileName(
            self, "Import previously downloaded card data obtained from Scryfall",
            QStandardPaths.locate(QStandardPaths.DownloadLocation, "", QStandardPaths.LocateDirectory),
            "Scryfall card data (*.json, *.json.gz)")
        logger.info(f"{location=}")
        if not location:
            logger.debug("User cancelled file selection. Not importing.")
            return
        if not (path := pathlib.Path(location)).is_file():
            QMessageBox.critical(
                self, "Selected location is not a file",
                f"Cannot find the selected file:\n{location}",
                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            return
        logger.info(f"Import card data from {path}")
        QApplication.instance().card_info_downloader.import_from_file(path)
