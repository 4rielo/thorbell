import sys

import PySide2
from PySide2 import QtGui, QtWidgets

from CSB_MercurioR1 import Fprincipal

def main():
    app = QtWidgets.QApplication(sys.argv)
    print("version 0.0.11")
    print("Loading Window")
    window = Fprincipal.MainWindow()   #  loader.load("mainwindow.ui", None)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()