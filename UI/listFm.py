# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listFm.ui',
# licensing of 'listFm.ui' applies.
#
# Created: Mon Jan  7 10:31:33 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_listFm(object):
    def setupUi(self, listFm):
        listFm.setObjectName("listFm")
        listFm.resize(370, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/MPPC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listFm.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(listFm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 351))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ok_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.ok_Btn.setFont(font)
        self.ok_Btn.setObjectName("ok_Btn")
        self.verticalLayout.addWidget(self.ok_Btn)
        self.close_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.close_Btn.setFont(font)
        self.close_Btn.setObjectName("close_Btn")
        self.verticalLayout.addWidget(self.close_Btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.delete_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.delete_Btn.setFont(font)
        self.delete_Btn.setObjectName("delete_Btn")
        self.verticalLayout.addWidget(self.delete_Btn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(listFm)
        QtCore.QMetaObject.connectSlotsByName(listFm)

    def retranslateUi(self, listFm):
        listFm.setWindowTitle(QtWidgets.QApplication.translate("listFm", "选择", None, -1))
        self.ok_Btn.setText(QtWidgets.QApplication.translate("listFm", "确定", None, -1))
        self.close_Btn.setText(QtWidgets.QApplication.translate("listFm", "取消", None, -1))
        self.delete_Btn.setText(QtWidgets.QApplication.translate("listFm", "删除", None, -1))

