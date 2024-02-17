from PyQt6.QtWidgets import QComboBox, QTableWidget
from PyQt6.QtCore import QObject
from typing import Any
import json
import sys
import os


def read_json_file(path: str, default: Any) -> Any:
    """
    Tries to parse the given JSON file and prints a error if the file couldn't be parsed
    Returns default if the file is not found or couldn't be parsed
    """
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.decoder.JSONDecodeError as e:
            print(f"Can't parse {os.path.basename(path)}: {e.msg}: line {e.lineno} column {e.colno} (char {e.pos})", file=sys.stderr)
            return default
        except Exception:
            print("Can't read " + os.path.basename(path), file=sys.stderr)
            return default
    else:
        return default


def select_combo_box_data(box: QComboBox, data: Any, default_index: int = 0) -> None:
    """Set the index to the item with the given data"""
    index = box.findData(data)
    if index == -1:
        box.setCurrentIndex(default_index)
    else:
        box.setCurrentIndex(index)


def clear_table_widget(table: QTableWidget):
    """Removes all Rows from a QTableWidget"""
    while table.rowCount() > 0:
        table.removeRow(0)


def get_table_widget_sender_row(table: QTableWidget, column: int, sender: QObject) -> int:
    """Get the Row in a QTableWidget that contains the Button that was clicked"""
    for i in range(table.rowCount()):
        if table.cellWidget(i, column) == sender:
            return i
