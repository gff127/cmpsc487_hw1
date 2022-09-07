#the main for the gui

import gui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
