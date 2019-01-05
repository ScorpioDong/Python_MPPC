# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFm.ui',
# licensing of 'mainFm.ui' applies.
#
# Created: Thu Jan  3 21:54:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainFm(object):
    def setupUi(self, mainFm):
        mainFm.setObjectName("mainFm")
        mainFm.resize(436, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/MPPC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainFm.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(mainFm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 417, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.row_LB = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.row_LB.setFont(font)
        self.row_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.row_LB.setObjectName("row_LB")
        self.horizontalLayout_2.addWidget(self.row_LB)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.col_LB = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.col_LB.setFont(font)
        self.col_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.col_LB.setObjectName("col_LB")
        self.horizontalLayout_2.addWidget(self.col_LB)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.count_LB = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count_LB.sizePolicy().hasHeightForWidth())
        self.count_LB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        self.count_LB.setFont(font)
        self.count_LB.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.count_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.count_LB.setObjectName("count_LB")
        self.verticalLayout_2.addWidget(self.count_LB)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_Btn.setEnabled(False)
        self.start_Btn.setObjectName("start_Btn")
        self.verticalLayout.addWidget(self.start_Btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.data_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.data_Btn.setEnabled(False)
        self.data_Btn.setObjectName("data_Btn")
        self.verticalLayout.addWidget(self.data_Btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.stop_Btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stop_Btn.setEnabled(False)
        self.stop_Btn.setObjectName("stop_Btn")
        self.verticalLayout.addWidget(self.stop_Btn)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(mainFm)
        QtCore.QMetaObject.connectSlotsByName(mainFm)

    def retranslateUi(self, mainFm):
        mainFm.setWindowTitle(QtWidgets.QApplication.translate("mainFm", "光子计数扫描", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("mainFm", "行", None, -1))
        self.row_LB.setText(QtWidgets.QApplication.translate("mainFm", "0", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("mainFm", "列", None, -1))
        self.col_LB.setText(QtWidgets.QApplication.translate("mainFm", "0", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("mainFm", "计数值", None, -1))
        self.count_LB.setText(QtWidgets.QApplication.translate("mainFm", "0", None, -1))
        self.start_Btn.setText(QtWidgets.QApplication.translate("mainFm", "开始", None, -1))
        self.data_Btn.setText(QtWidgets.QApplication.translate("mainFm", "显示数据", None, -1))
        self.stop_Btn.setText(QtWidgets.QApplication.translate("mainFm", "结束", None, -1))
