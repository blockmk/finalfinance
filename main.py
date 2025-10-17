

import json
import sys

import data
import data_util
import app_terminal

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

expenses = data_util.load_finance()



def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Hello PySide6")
    window.setMinimumSize(300, 200)

    label = QLabel("Hello, this is PySide6!")
    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


main()
#app_terminal.main()
