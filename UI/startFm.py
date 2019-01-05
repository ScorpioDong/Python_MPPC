# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startFm.ui',
# licensing of 'startFm.ui' applies.
#
# Created: Thu Jan  3 09:55:35 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_startFm(object):
    def setupUi(self, startFm):
        startFm.setObjectName("startFm")
        startFm.resize(425, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(startFm.sizePolicy().hasHeightForWidth())
        startFm.setSizePolicy(sizePolicy)
        startFm.setMinimumSize(QtCore.QSize(0, 205))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/MPPC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        startFm.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(startFm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_Btn.sizePolicy().hasHeightForWidth())
        self.start_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.start_Btn.setFont(font)
        self.start_Btn.setObjectName("start_Btn")
        self.horizontalLayout.addWidget(self.start_Btn)
        self.continue_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.continue_Btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_Btn.sizePolicy().hasHeightForWidth())
        self.continue_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.continue_Btn.setFont(font)
        self.continue_Btn.setObjectName("continue_Btn")
        self.horizontalLayout.addWidget(self.continue_Btn)

        self.retranslateUi(startFm)
        QtCore.QMetaObject.connectSlotsByName(startFm)

    def retranslateUi(self, startFm):
        startFm.setWindowTitle(QtWidgets.QApplication.translate("startFm", "开始", None, -1))
        self.start_Btn.setText(QtWidgets.QApplication.translate("startFm", "开始", None, -1))
        self.continue_Btn.setText(QtWidgets.QApplication.translate("startFm", "继续", None, -1))

