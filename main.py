# -*- coding:utf-8 -*-

import sys
import Src.mainFm
from PySide2 import QtCore, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Src.mainFm.MainFm()
    win.start()
    app.exec_()
