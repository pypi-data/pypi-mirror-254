from PyQt6.QtWidgets import QDialog, QMessageBox, QApplication, QStyle
from ..ui_compiled.ConnectDialog import Ui_ConnectDialog
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtDBus import QDBusConnection
from typing import TYPE_CHECKING
from PyQt6.QtGui import QIcon


if TYPE_CHECKING:
    from .MainWindow import MainWindow


class ConnectDialog(QDialog, Ui_ConnectDialog):
    def __init__(self, main_window: "MainWindow") -> None:
        super().__init__(main_window)

        self.setupUi(self)

        self._ok = False
        self._connection = None
        self._main_window = main_window

        self.ok_button.setIcon(QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogOkButton)))
        self.cancel_button.setIcon(QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton)))

        self.ok_button.clicked.connect(self._ok_button_clicked)
        self.cancel_button.clicked.connect(self.close)

    def _ok_button_clicked(self) -> None:
        name = self.name_edit.text().strip()
        address = self.address_edit.text().strip()

        if name == "":
            QMessageBox.critical(self, QCoreApplication.translate("ConnectDialog", "Name not set"), QCoreApplication.translate("ConnectDialog", "You need to enter a name"))
            return

        if address == "":
            QMessageBox.critical(self, QCoreApplication.translate("ConnectDialog", "Adress not set"), QCoreApplication.translate("ConnectDialog", "You need to enter a address"))
            return

        connection = QDBusConnection(address)
        if not connection.isConnected():
            QMessageBox.critical(self, QCoreApplication.translate("ConnectDialog", "Invalid Address"), QCoreApplication.translate("ConnectDialog", "Could not connect to {{address}}").replace("{{address}}", address))
            return

        self._ok = True
        self._connection = connection

        self.close()

    def get_connection(self) -> tuple[str, str, QDBusConnection, bool] | None:
        self._ok = False

        self.exec()

        if not self._ok:
            return

        return (self.name_edit.text().strip(), self.address_edit.text().strip(), self._connection, self.auto_connect_check_box.isChecked())
