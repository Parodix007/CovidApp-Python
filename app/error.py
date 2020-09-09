from PyQt5.QtWidgets import QMessageBox


class Error:

    def __init__(self, error_text):
        error = QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setText('Error')
        error.setInformativeText(str(error_text))
        error.setWindowTitle('Error')
        error.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        error.exec_()
