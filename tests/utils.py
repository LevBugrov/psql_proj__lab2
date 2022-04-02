"""Various utilities for testing"""
from PyQt5 import Qt as Q


def get_app() -> 'QApplication':
    """Initialize framework and return reference to Qt application."""
    if not hasattr(get_app, 'app'):
        get_app.app = Q.QApplication([])
    return get_app.app


def compare_list_and_table(lst, table):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != table.item(i, j).text():
                return False
    return True


def open_db(window, name="test"):
    window.ui.open_db_edit.setText(name)
    window.create_db()
    window.delete_all_tables()
