from PyQt6.QtDBus import QDBusConnection, QDBusMessage
from .Service import Service
from typing import Literal


class Connection:
    def __init__(self, connection: QDBusConnection, connection_type: Literal["session", "system", "custom"]) -> None:
        self.connection_type = connection_type
        self.connection = connection

        self._error_message: str | None = None

        self.service_list: list[Service] = []

        self.reload_services()

    def reload_services(self) -> None:
        self.service_list.clear()

        activatable_message = QDBusMessage.createMethodCall("org.freedesktop.DBus", "/org/freedesktop/DBus", "org.freedesktop.DBus", "ListActivatableNames")
        activatable_result = self.connection.call(activatable_message)

        if activatable_result.errorMessage() != "":
            self._error_message = activatable_result.errorMessage()
            return

        activatable_list: list[str] = activatable_result.arguments()[0]

        name_message = QDBusMessage.createMethodCall("org.freedesktop.DBus", "/org/freedesktop/DBus", "org.freedesktop.DBus", "ListNames")
        name_result = self.connection.call(name_message)

        if name_result.errorMessage() != "":
            self._error_message = name_result.errorMessage()
            return

        name_list: list[str] = name_result.arguments()[0]

        all_services: list[str] = []

        for i in activatable_list:
            all_services.append(i)

        for i in name_list:
            if i not in all_services:
                all_services.append(i)

        all_services.sort()

        for i in all_services:
            self.service_list.append(Service(self, i, i in activatable_list))

    def get_service_by_name(self, name: str) -> Service | None:
        for service in self.service_list:
            if service.name == name:
                return service
        return None

    def get_error_message(self) -> str | None:
        return self._error_message

