from PyQt6 import QtGui, QtCore, QtWidgets


class FramelessMsgBx(QtWidgets.QMessageBox):

    def __init__(self, **kwargs):
        parent = kwargs.get('parent', None)
        super().__init__(parent=parent)

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.FramelessWindowHint)
