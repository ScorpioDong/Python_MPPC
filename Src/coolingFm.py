# -*- coding:utf-8 -*-

import UI.coolingFm
from PySide2 import QtCore, QtWidgets, QtGui


class CoolingFm(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~
                            QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(342, 96)
        self.ui = UI.coolingFm.Ui_Form()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(),self.height())
