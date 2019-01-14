# -*- coding:utf-8 -*-

import numpy as np
import UI.dataFm
from PySide2 import QtCore, QtWidgets, QtGui


class DataFm(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui = UI.dataFm.Ui_dataFm()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(), self.height())
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def init(self, Row, Col):
        self.Row = Row
        self.Col = Col
        self.ui.tableWidget.setRowCount(Row)
        self.ui.tableWidget.setColumnCount(Col)

    def update(self, Data):
        self.Data = Data.copy()
        for col in range(0, self.Col):
            for row in range(0, self.Row):
                self.ui.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(self.Data[row][col])))
