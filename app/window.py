from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QToolBox
from api import Request


class Window:

    def __init__(self):
        self.__widget = QWidget()
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__label = QLabel(self.__widget)
        self.__label.setText('Enter country name: ')
        self.__grid.addWidget(self.__label, 0, 0)

        self.__entry = QLineEdit(self.__widget)
        self.__entry.setPlaceholderText('Enter country name...')
        self.__grid.addWidget(self.__entry, 0, 1)

        self.__button = QPushButton(self.__widget)
        self.__button.setText('Search')
        self.__button.clicked.connect(self.make_request)
        self.__grid.addWidget(self.__button, 0, 2)

        self.__toolbox = QToolBox()
        self.__grid.addWidget(self.__toolbox, 1, 0)

        self.__data_label = QLabel()
        self.__toolbox.addItem(self.__data_label, 'Data:')

        self.__widget.setWindowTitle('Covid App')
        self.__widget.show()

    def make_request(self):
        api = Request('get', self.__entry.text())
        resp = api.get_api()
        print(type(resp))
