import sys

from PySide6.QtGui import QIcon


def run_ui():
    from PySide6.QtWidgets import QApplication
    from ui.MainWindow import MainWindow
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ui/icon/01.jpeg"))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_ui()
