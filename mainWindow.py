import sys
from PyQt5 import QtGui;
from PyQt5.QtWidgets import QApplication ,QMainWindow

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title ="RAVI"
        self.top =100
        self.left = 100
        self.width = 680
        self.height = 500

        self.initWindow()


    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top ,self.left ,self.width ,self.height)
        self.setWindowIcon(QtGui.QIcon('images/koala.jpg'))
        self.show()


App = QApplication(sys.argv)
mywindow = Window()
sys.exit(App.exec())



