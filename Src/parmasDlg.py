# -*- coding:utf-8 -*-

import json
import UI.parmasFm
import serial.tools.list_ports
from PySide2 import QtCore, QtWidgets, QtGui


class ParmasDlg(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui = UI.parmasFm.Ui_parmasFm()
        self.ui.setupUi(self)

        self.ui_init()
        self.connect_init()
        self.parmas_load()

    def ui_init(self):
        self.ui.gatetime_Cmb.addItems(("1", "2", "5", "10", "20", "50", "100"))
        self.ui.threshold_Cmb.addItems(
            ("0.5 p.e.", "1.5 p.e.", "2.5 p.e.", "3.5 p.e.", "4.5 p.e.", "5.5 p.e.", "6.5 p.e.", "7.5 p.e.", "Disable"))
        self.port_check()

    def connect_init(self):
        self.ui.reflush_Btn.clicked.connect(self.port_check)

    def parmas_load(self):
        with open("Config/parmas.json", "r", encoding='utf-8') as file:
            self.Parmas = json.load(file)
        self.ui.pic_x_len_LE.setText(str(self.Parmas['pic_x_len']))
        self.ui.pic_y_len_LE.setText(str(self.Parmas['pic_y_len']))
        self.ui.pic_x_count_LE.setText(str(self.Parmas['pic_x_count']))
        self.ui.pic_y_count_LE.setText(str(self.Parmas['pic_y_count']))
        self.ui.mt_x_speed_LE.setText(str(self.Parmas['mt_x_speed']))
        self.ui.mt_y_speed_LE.setText(str(self.Parmas['mt_y_speed']))
        self.ui.gatetime_Cmb.setCurrentIndex(self.Parmas['gatetime_index'])
        self.ui.threshold_Cmb.setCurrentIndex(self.Parmas['threshold_index'])

    def parmas_save(self):
        self.Parmas['pic_x_len'] = int(self.ui.pic_x_len_LE.text())
        self.Parmas['pic_y_len'] = int(self.ui.pic_y_len_LE.text())
        self.Parmas['pic_x_count'] = int(self.ui.pic_x_count_LE.text())
        self.Parmas['pic_y_count'] = int(self.ui.pic_y_count_LE.text())
        self.Parmas['mt_x_speed'] = int(self.ui.mt_x_speed_LE.text())
        self.Parmas['mt_y_speed'] = int(self.ui.mt_y_speed_LE.text())
        self.Parmas['gatetime_index'] = self.ui.gatetime_Cmb.currentIndex()
        self.Parmas['threshold_index'] = self.ui.threshold_Cmb.currentIndex()
        with open("Config/parmas.json", "w", encoding='utf-8') as file:
            json.dump(self.Parmas, file, indent=4)

    @QtCore.Slot()
    def port_check(self):
        self.ui.serial_Cmb.clear()
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            self.ui.serial_Cmb.addItem(port[0])
