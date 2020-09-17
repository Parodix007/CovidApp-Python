from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QToolBox
from api import Request
from error import Error


class Window:
    def __init__(self):
        self.__widget = QWidget()
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__label = QLabel(self.__widget)
        self.__label.setText('Enter country name: ')
        self.__grid.addWidget(self.__label, 0, 0)

        self.__entry = QLineEdit(self.__widget)
        self.__entry.setPlaceholderText('Type country...')
        self.__grid.addWidget(self.__entry, 0, 1)

        self.__button = QPushButton(self.__widget)
        self.__button.setText('Search')
        self.__button.clicked.connect(self.__make_request)
        self.__grid.addWidget(self.__button, 0, 2)

        self.__toolbox = QToolBox()
        self.__grid.addWidget(self.__toolbox)

        self.__data_label = QLabel()
        self.__toolbox.addItem(self.__data_label, 'Data:')

        self.__widget.setWindowTitle('Covid App')
        self.__widget.show()

    def __make_request(self):
        if self.__entry.text():
            req = Request("GET", self.__entry.text())
            res = req.get_api()
            if res:
                return self.__set_data(res)
            else:
                return
        else:
            Error('Enter country name')
            self.__data_label.setText("")

    def __set_data(self, data_item):
        if data_item['Country_text'].lower() == 'world':
            Error('Type valid country name')
        else:
            self.__data_label.setText(f"Cases: {data_item['Total Cases_text']}\n"
                                      f"Deaths: {data_item['Total Deaths_text']}\n"
                                      f"Recovered: {data_item['Total Recovered_text']}")
