import sys

import PySide2
from PySide2 import QtGui, QtWidgets

from CSB_MercurioR1 import Fprincipal

import esky
if hasattr(sys,"frozen"):
    print("Updating firmware")
    app = esky.Esky(sys.executable,"https://github.com/4rielo/thorbell.git")
    app.auto_update()

def main():
    app = QtWidgets.QApplication(sys.argv)
    print("version 0.0.2")
    print("Loading Window")
    window = Fprincipal.MainWindow()   #  loader.load("mainwindow.ui", None)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()