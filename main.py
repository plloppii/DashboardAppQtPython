# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from mainwindow import *
from Server.mainhand import mainhandler

#class dashboard(QtWidgets.QWidget):
#    def __init__(self, parent= None):
#        QtWidgets.QWidget.__init__(self,parent)
#        self.setGeometry(200,200,1080,720)
#        self.runpyscript = QtWidgets.QPushButton("Add Machine",self)
#        self.runpyscript.setGeometry(10,10,150,30)
#        self.runpyscript.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

#        self.connect(self.runpyscript, QtCore.SIGNAL("clicked()"),
#                    QtWidgets.qApp, QtCore.SLOT("quit()"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

    def refresh_text_box(self, astring):
        self.Serveroutput.append(astring)
        QtWidgets.QApplication.processEvents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()


    sys.exit(app.exec_())
