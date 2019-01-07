# -*- coding:utf-8 -*-

import UI.startFm
from PySide2 import QtCore, QtWidgets, QtGui


class StartDlg(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui = UI.startFm.Ui_startFm()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(),self.height())
