# -*- coding:utf-8 -*-

import os
import UI.listFm
from PySide2 import QtCore, QtWidgets, QtGui


class ListDlg(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui = UI.listFm.Ui_listFm()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(), self.height())

        listdirs = os.listdir("Cache")
        listdirs.sort(reverse=True)
        for dir in listdirs:
            self.ui.listWidget.addItem(dir)

        self.ui.listWidget.setCurrentRow(0)

        self.ui.close_Btn.clicked.connect(self.close)
        self.ui.delete_Btn.clicked.connect(self.delete_clicked_slot)

    @QtCore.Slot()
    def delete_clicked_slot(self):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setText("确定删除？")
        MsgBox.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        MsgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        result = MsgBox.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            path = "Cache/" + self.ui.listWidget.currentItem().text()
            os.remove(path + "/parmas.json")
            os.remove(path + "/temp.mat")
            os.rmdir(path)
            self.ui.listWidget.removeItemWidget(
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow()))
        else:
            return
