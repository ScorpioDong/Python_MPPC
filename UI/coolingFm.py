# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coolingFm.ui',
# licensing of 'coolingFm.ui' applies.
#
# Created: Thu Jan  3 21:35:22 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 96)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/MPPC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "！", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Device is cooling!", None, -1))

