import multiprocessing
import sys
import webbrowser

from PySide6 import *

from end import Ui_MainWindow
from PySide6 import QtCore

from PySide6.QtWidgets import *

from PySide6.QtWidgets import QApplication





class ExpenseTracker(QMainWindow):
    def __init__(self, parent=None):

        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.showMinimized)
        self.ui.pushButton_11.clicked.connect(self.close)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_13.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/@THETL-cf6sq/featured'))
        self.ui.pushButton_12.clicked.connect(lambda: webbrowser.open('https://vk.com/id201359102'))
        self.ui.pushButton_14.clicked.connect(lambda: webbrowser.open('https://discord.com/'))
        self.ui.pushButton_15.clicked.connect(lambda: webbrowser.open('https://mail.yandex.ru/?uid=196769690#inbox'))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.oldPos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())