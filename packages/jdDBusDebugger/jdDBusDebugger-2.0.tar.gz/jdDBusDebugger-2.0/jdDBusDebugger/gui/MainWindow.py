from PyQt6.QtWidgets import QMainWindow, QTabBar, QInputDialog, QMessageBox, QApplication
from .GenerateScriptDialog import GenerateScriptDialog
from ..ui_compiled.MainWindow import Ui_MainWindow
from .ManageMacrosDialog import ManageMacrosDialog
from .EmitSignalDialog import EmitSignalDialog
from ..core.MacroManager import MacroManager
from .SettingsDialog import SettingsDialog
from typing import Literal, TYPE_CHECKING
from ..types.Connection import Connection
from PyQt6.QtCore import QCoreApplication
from .WelcomeDialog import WelcomeDialog
from PyQt6.QtDBus import QDBusConnection
from .CentralWidget import CentralWidget
from .ConnectDialog import ConnectDialog
from ..Functions import read_json_file
from .AboutDialog import AboutDialog
from PyQt6.QtGui import QAction
import webbrowser
import json
import sys
import os


if TYPE_CHECKING:
    from ..Environment import Environment


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, env: "Environment") -> None:
        super().__init__()

        self.setupUi(self)

        self._env = env
        self.macro_manager = MacroManager(env)

        self.tab_widget.tabCloseRequested.connect(self._tab_close)
        self.tab_widget.currentChanged.connect(self._tab_changed)

        self.connect_action.triggered.connect(self._connect_action_clicked)
        self.exit_action.triggered.connect(lambda: sys.exit(0))

        self.settings_action.triggered.connect(lambda: SettingsDialog(env, self).open_dialog())

        self.start_recording_macro_action.triggered.connect(self._start_recording_macro_action_clicked)
        self.stop_recording_macro_action.triggered.connect(self._stop_recording_macro_action_clicked)
        self.run_macro_action.triggered.connect(self._run_macro_action_clicked)
        self.save_macro_action.triggered.connect(self._save_macro_action_clicked)
        self.generate_script_macro_action.triggered.connect(self._generate_script_macro_action_clicked)
        self.manage_macros_action.triggered.connect(self._manage_macros_action_clicked)

        self.emit_signal_action.triggered.connect(lambda: EmitSignalDialog(self).open_dialog())

        self.show_welcome_dialog_action.triggered.connect(lambda: WelcomeDialog(self._env).open_dialog())
        self.view_source_action.triggered.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdDBusDebugger"))
        self.report_bug_action.triggered.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdDBusDebugger/issues"))
        self.translate_action.triggered.connect(lambda: webbrowser.open("https://translate.codeberg.org/projects/jdDBusDebugger"))
        self.donate_action.triggered.connect(lambda: webbrowser.open("https://ko-fi.com/jakobdev"))
        self.about_action.triggered.connect(lambda: AboutDialog(self._env).exec())
        self.about_qt_action.triggered.connect(QApplication.instance().aboutQt)

        self.tab_widget.clear()

        self._add_tab()

        self._update_macro_actions_enabled()
        self._update_macro_menu()

    def _get_saved_connections(self) -> list[dict[Literal["name", "address"], str]]:
        connections = read_json_file(os.path.join(self._env.data_dir, "connections.json"), {})
        return connections.get("connections", [])

    def _write_saved_connections(self, connections: list[dict[Literal["name", "address"], str]]) -> None:
        json_data = {
            "version": 1,
            "connections": connections
        }

        with open(os.path.join(self._env.data_dir, "connections.json"), "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

    def _remove_saved_connection(self, connections: list[dict[Literal["name", "address"], str]], name: str) -> tuple[list[dict[Literal["name", "address"], str]], bool]:
        for count, conn_data in enumerate(connections):
            if conn_data["name"].lower() == name.lower():
                del connections[count]
                return (connections, True)
        return (connections, False)

    def _add_tab(self):
        session_connection = QDBusConnection.sessionBus()
        if session_connection.isConnected():
            session_widget = CentralWidget(self._env, self, Connection(session_connection, "session"))
            index = self.tab_widget.addTab(session_widget,  QCoreApplication.translate("MainWindow", "Session"))
            self.tab_widget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, None)
        elif self._env.settings.get("warnSesssionSystemConnectionFail"):
            QMessageBox.critical(self, QCoreApplication.translate("MainWindow", "Could not connect to session bus"), QCoreApplication.translate("MainWindow", "jdDBusDebugger was unable to connect to the session bus. If you run jdDBusDebugger in a sandboxed environment make sure it has the correct permission."))

        system_connection = QDBusConnection.systemBus()
        if system_connection.isConnected():
            system_widget = CentralWidget(self._env, self, Connection(system_connection, "system"))
            index = self.tab_widget.addTab(system_widget,  QCoreApplication.translate("MainWindow", "System"))
            self.tab_widget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, None)
        elif self._env.settings.get("warnSesssionSystemConnectionFail"):
            QMessageBox.critical(self, QCoreApplication.translate("MainWindow", "Could not connect to system bus"), QCoreApplication.translate("MainWindow", "jdDBusDebugger was unable to connect to the system bus. If you run jdDBusDebugger in a sandboxed environment make sure it has the correct permission."))

        for conn_data in self._get_saved_connections():
            conn = QDBusConnection(conn_data["address"])

            if not conn.isConnected():
                QMessageBox.critical(self, QCoreApplication.translate("MainWindow", "Name exists"), QCoreApplication.translate("MainWindow", "Could not connect to {{connection}}").replace("{{connection}}", conn_data["address"]))
                continue

            self.tab_widget.addTab(CentralWidget(self._env, self, Connection(conn, "custom")), conn_data["name"])

    def _tab_close(self, index: int) -> None:
        name = self.tab_widget.tabText(index)

        self.tab_widget.removeTab(index)

        saved_connections = self._get_saved_connections()
        saved_connections, ok = self._remove_saved_connection(saved_connections, name)
        if ok:
            self._write_saved_connections(saved_connections)

    def _tab_changed(self) -> None:
        if not isinstance(self.get_current_central_widget(), CentralWidget):
            return

        self.macro_manager.reset_recording()
        self._update_macro_menu()
        self._update_macro_actions_enabled()

    def _connect_action_clicked(self) -> None:
        data = ConnectDialog(self).get_connection()

        if data is None:
            return

        widget = CentralWidget(self, Connection(data[2]))
        self.tab_widget.addTab(widget, data[0])

        if data[3]:
            saved_connections = self._get_saved_connections()
            saved_connections.append({"name": data[0], "address": data[1]})
            self._write_saved_connections(saved_connections)

    def _run_saved_macro(self) -> None:
        sender = self.sender()

        if sender is None:
            return

        macro = self.macro_manager.get_macro_by_id(sender.data())

        if macro is None:
            return

        for action in macro.actions:
            self.get_current_central_widget().execute_action(action)

    def _update_macro_menu(self) -> None:
        self.run_saved_macro_menu.clear()

        actions = self.macro_manager.get_macros_for_connection(self.get_current_central_widget().connection)

        if len(actions) == 0:
            empty_action = QAction(QCoreApplication.translate("MainWindow", "You have no macros saved"), self)
            empty_action.setEnabled(False)
            self.run_saved_macro_menu.addAction(empty_action)
            return

        for macro in actions:
            macro_action = QAction(macro.name, self)
            macro_action.setData(macro.id)
            macro_action.triggered.connect(self._run_saved_macro)
            self.run_saved_macro_menu.addAction(macro_action)

    def _update_macro_actions_enabled(self) -> None:
        self.start_recording_macro_action.setEnabled(not self.macro_manager.is_recording() and self.tab_widget.count() != 0)
        self.stop_recording_macro_action.setEnabled(self.macro_manager.is_recording())
        self.run_macro_action.setEnabled(not self.macro_manager.is_recording() and self.macro_manager.has_current_macro())
        self.save_macro_action.setEnabled(not self.macro_manager.is_recording() and self.macro_manager.has_current_macro())
        self.generate_script_macro_action.setEnabled(not self.macro_manager.is_recording() and self.macro_manager.has_current_macro())

    def _start_recording_macro_action_clicked(self) -> None:
        self.macro_manager.start_recording()
        self._update_macro_actions_enabled()

    def _stop_recording_macro_action_clicked(self) -> None:
        self.macro_manager.stop_recording()
        self._update_macro_actions_enabled()

    def _run_macro_action_clicked(self) -> None:
        for action in self.macro_manager.get_current_actions():
            self.get_current_central_widget().execute_action(action)

    def _save_macro_action_clicked(self) -> None:
        name = QInputDialog.getText(self, QCoreApplication.translate("MainWindow", "Enter Name"), QCoreApplication.translate("MainWindow", "Please enter a name for your macro"))[0].strip()

        if name == "":
            return

        if self.macro_manager.get_macro_by_name(name) is not None:
            QMessageBox.critical(self, QCoreApplication.translate("MainWindow", "Name exists"), QCoreApplication.translate("MainWindow", "There is already a macro with this name"))
            return

        self.macro_manager.save_current_macro(name, self.get_current_central_widget().connection)

    def _manage_macros_action_clicked(self) -> None:
        ManageMacrosDialog(self, self.macro_manager).open_dialog()

    def _generate_script_macro_action_clicked(self) -> None:
        GenerateScriptDialog().open_dialog(self.macro_manager.get_current_actions())

    def has_connection_name(self, name: str) -> bool:
        for pos in range(self.tab_widget.count()):
            if self.tab_widget.tabText(pos) == name.lower():
                return True
        return False

    def get_current_central_widget(self) -> CentralWidget:
        return self.tab_widget.currentWidget()