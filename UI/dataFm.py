# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataFm.ui',
# licensing of 'dataFm.ui' applies.
#
# Created: Mon Jan  7 17:29:29 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dataFm(object):
    def setupUi(self, dataFm):
        dataFm.setObjectName("dataFm")
        dataFm.resize(1334, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/MPPC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dataFm.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(dataFm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1311, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reflush_Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reflush_Btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Res/Refresh_16px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reflush_Btn.setIcon(icon1)
        self.reflush_Btn.setIconSize(QtCore.QSize(16, 16))
        self.reflush_Btn.setObjectName("reflush_Btn")
        self.verticalLayout.addWidget(self.reflush_Btn)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(dataFm)
        QtCore.QMetaObject.connectSlotsByName(dataFm)

    def retranslateUi(self, dataFm):
        dataFm.setWindowTitle(QtWidgets.QApplication.translate("dataFm", "数据", None, -1))

