import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
import requests


class Window:

    def __init__(self):
        self.__widget = QWidget()
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__label = QLabel(self.__widget)
        self.__label.setText('Enter country name: ')
        self.__grid.addWidget(self.__label, 0, 0)

        self.__entry = QLineEdit(self.__widget)
        self.__grid.addWidget(self.__entry, 0, 1)

        self.__button = QPushButton(self.__widget)
        self.__button.setText('Search')
        self.__grid.addWidget(self.__button, 1, 0)

        self.__widget.setGeometry(300, 50, 400, 400)
        self.__widget.setWindowTitle('Covid App')
        self.__widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
