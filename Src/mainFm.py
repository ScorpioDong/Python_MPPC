# -*- coding : utf-8 -*-

import os
import time
import json
import UI.mainFm
import Src.startDlg
import Src.parmasDlg
import Src.listDlg
import Src.dataDlg
import Src.coolingFm
import Src.control
from MPPCModule.MPPCModule import mppcum1a

from PySide2 import QtCore, QtWidgets, QtGui


class MainFm(QtWidgets.QWidget):

    quit_signal = QtCore.Signal()
    ctrl_init_signal = QtCore.Signal(dict)
    ctrl_run_signal = QtCore.Signal()
    ctrl_save_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~
                            QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowCloseButtonHint)
        self.ui = UI.mainFm.Ui_mainFm()
        self.ui.setupUi(self)

        self.setFixedSize(self.width(),self.height())

        self.var_init()
        self.connect_init()

    def var_init(self):
        self.Parmas = {}
        self._CYCLE_TIME = 100
        self.DeviceHandle = mppcum1a.INVALID_HANDLE_VALUE
        self.PipeHandle = mppcum1a.INVALID_HANDLE_VALUE
        self.DataDlg = Src.dataDlg.DataFm()
        self.StartDlg = Src.startDlg.StartDlg()
        self.ParmasDlg = Src.parmasDlg.ParmasDlg()
        self.CoolingDlg = Src.coolingFm.CoolingFm()
        self.Ctrler = Src.control.Control()
        self.CtrlThread = QtCore.QThread()
        self.Ctrler.moveToThread(self.CtrlThread)

        listdir = os.listdir('Cache')
        if len(listdir) == 0:
            return
        else:
            self.StartDlg.ui.continue_Btn.setEnabled(True)
            self.ListDlg = Src.listDlg.ListDlg()
            self.ListDlg.ui.ok_Btn.clicked.connect(self.listdlg_ok_clicked_slot)

    def connect_init(self):
        self.StartDlg.ui.start_Btn.clicked.connect(
            self.startdlg_start_clicked_slot)
        self.StartDlg.ui.continue_Btn.clicked.connect(
            self.startdlg_continue_clicked_slot)
        self.ParmasDlg.ui.startBtn.clicked.connect(
            self.parmasdlg_start_clicked_slot)
        self.DataDlg.ui.reflush_Btn.clicked.connect(self.data_slot)

        self.ctrl_init_signal.connect(self.Ctrler.init)
        self.ctrl_run_signal.connect(self.Ctrler.run)
        self.ctrl_save_signal.connect(
            self.Ctrler.save, QtCore.Qt.BlockingQueuedConnection)
        self.Ctrler.serial_open_failed_signal.connect(
            self.ctrl_serial_open_failed_slot)
        self.Ctrler.data_show_signal.connect(self.data_show_slot)
        self.Ctrler.init_finish_signal.connect(self.ctrl_init_finish_slot)
        self.Ctrler.task_finish_signal.connect(self.task_finish_slot)

        self.ui.stop_Btn.clicked.connect(self.stop_clicked_slot)
        self.ui.start_Btn.clicked.connect(self.start_clicked_slot)
        self.ui.data_Btn.clicked.connect(self.data_slot)

    def start(self):
        self.StartDlg.show()

    def mppc_config(self):
        self.DeviceHandle = mppcum1a.MPPC_OpenDevice()
        if self.DeviceHandle == mppcum1a.INVALID_HANDLE_VALUE:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Open Device Error！")
            MsgBox.exec_()
            return False

        self.PipeHandle = mppcum1a.MPPC_OpenPipe(self.DeviceHandle)
        if self.PipeHandle == mppcum1a.INVALID_HANDLE_VALUE:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Open Pipe Error！")
            MsgBox.exec_()
            return False

        result = mppcum1a.MPPC_Initialize(self.DeviceHandle)
        if result != mppcum1a.MPPC_SUCCESS:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Device Init Error！")
            MsgBox.exec_()
            return False

        result = mppcum1a.MPPC_SetProperty(
            self.DeviceHandle, self.Parmas['gatetime']*1000, self.Parmas['datasize'])
        if result != mppcum1a.MPPC_SUCCESS:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Set Property Error！")
            MsgBox.exec_()
            return False

        if self.Parmas['threshold_index'] <= mppcum1a.VTH_75:
            result = mppcum1a.MPPC_SetThreshold(
                self.DeviceHandle, self.Parmas['threshold_index'])
        else:
            result = mppcum1a.MPPC_SetThreshold(
                self.DeviceHandle, self.mppcum1a.VTH_OVER)
        if result != mppcum1a.MPPC_SUCCESS:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Set Threshold Error！")
            MsgBox.exec_()
            return False

        flag = -1
        result = mppcum1a.MPPC_GetPeltierControl(self.DeviceHandle, flag)
        if result == mppcum1a.MPPC_SUCCESS:
            if flag == mppcum1a.ENABLE:
                mppcum1a.MPPC_SetPeltierControl(
                    self.DeviceHandle, self.mppcum1a.DISABLE)
        else:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("Get PeltierControl Error！")
            MsgBox.exec_()
            return False

        while True:
            mppcum1a.MPPC_SetPeltierControl(
                self.DeviceHandle, self.mppcum1a.ENABLE)
            result = mppcum1a.MPPC_GetPeltierStatus(self.DeviceHandle)
            if result == mppcum1a.MPPC_SUCCESS:
                return True
            time.sleep(1)

    def parmas_load(self):
        self.Parmas['row_n'] = 0
        self.Parmas['col_n'] = 0
        self.Parmas['is_continue'] = False
        self.Parmas['path'] = ''
        self.Parmas['device_handle'] = self.DeviceHandle
        self.Parmas['pipe_handle'] = self.PipeHandle
        self.Parmas['row'] = self.ParmasDlg.Parmas['pic_y_count']
        self.Parmas['col'] = self.ParmasDlg.Parmas["pic_x_count"]
        self.Parmas['x_step'] = round(
            self.ParmasDlg.Parmas['pic_x_len']*400.0/(self.ParmasDlg.Parmas['pic_x_count'] - 1.0))
        self.Parmas['y_step'] = round(
            self.ParmasDlg.Parmas['pic_y_len']*400.0/(self.ParmasDlg.Parmas['pic_y_count'] - 1.0))
        self.Parmas['x_speed'] = self.ParmasDlg.Parmas['mt_x_speed']
        self.Parmas['y_speed'] = self.ParmasDlg.Parmas['mt_y_speed']
        self.Parmas['gatetime'] = int(
            self.ParmasDlg.ui.gatetime_Cmb.currentText())
        self.Parmas['datasize'] = round(
            self._CYCLE_TIME/self.Parmas['gatetime'])
        self.Parmas['threshold_index'] = self.ParmasDlg.Parmas['threshold_index']
        self.Parmas['serial_name'] = self.ParmasDlg.ui.serial_Cmb.currentText()

    @QtCore.Slot()
    def startdlg_start_clicked_slot(self):
        self.ParmasDlg.exec_()

    @QtCore.Slot()
    def startdlg_continue_clicked_slot(self):
        self.ListDlg.exec_()

    def app_quit(self):
        self.CtrlThread.quit()
        self.CtrlThread.wait()
        self.quit_signal.emit()

    @QtCore.Slot()
    def stop_clicked_slot(self):
        if self.ui.start_Btn.text() == "暂停":
            self.start_clicked_slot()
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setWindowTitle("！")
        MsgBox.setText("程序即将退出")
        MsgBox.setInformativeText("是否保存运行信息，等待下次自动运行？")
        MsgBox.setStandardButtons(
            QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Save)
        MsgBox.setDefaultButton(QtWidgets.QMessageBox.Save)
        result = MsgBox.exec_()
        if result == QtWidgets.QMessageBox.Discard:
            self.app_quit()
        elif result == QtWidgets.QMessageBox.Save:
            self.ctrl_save_signal.emit()
            self.app_quit()
        else:
            if self.ui.start_Btn.text() == "继续":
                self.start_clicked_slot()
            return

    @QtCore.Slot()
    def start_clicked_slot(self):
        name = self.ui.start_Btn.text()
        if name == "开始" or name == "继续":
            self.ctrl_run_signal.emit()
            self.ui.start_Btn.setText("暂停")
            if name == "开始":
                self.DataDlg.init(self.Parmas['row'], self.Parmas['col'])
        elif name == "暂停":
            self.Ctrler.isPause = True
            self.ui.start_Btn.setText("继续")

    @QtCore.Slot()
    def ctrl_serial_open_failed_slot(self):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setWindowTitle("！")
        MsgBox.setText("串口打开失败！")
        MsgBox.exec_()
        self.app_quit()

    @QtCore.Slot()
    def parmasdlg_start_clicked_slot(self):
        if len(self.ParmasDlg.ui.serial_Cmb.currentText()) == 0:
            MsgBox = QtWidgets.QMessageBox()
            MsgBox.setWindowTitle("！")
            MsgBox.setText("串口未找到，请刷新后再试！")
            MsgBox.exec_()
        else:
            self.StartDlg.hide()
            self.ParmasDlg.hide()
            self.ParmasDlg.parmas_save()
            self.parmas_load()
            self.show()
            self.CoolingDlg.show()
            if self.mppc_config() == False:
               self.app_quit()
               return
            self.CtrlThread.start()
            self.ctrl_init_signal.emit(self.Parmas)
            self.CoolingDlg.hide()

    @QtCore.Slot()
    def listdlg_ok_clicked_slot(self):
        self.StartDlg.hide()
        self.ListDlg.hide()
        path = "Cache/" + self.ListDlg.ui.listWidget.currentItem().text()
        with open(path + "/parmas.json", "r", encoding='utf-8') as file: 
            self.Parmas = json.load(file)
        self.show()
        self.CoolingDlg.show()
        if self.mppc_config() == False:
           self.app_quit()
           return
        self.CtrlThread.start()
        self.ctrl_init_signal.emit(self.Parmas)
        self.CoolingDlg.hide()

    @QtCore.Slot(list)
    def data_show_slot(self, data):
        self.ui.row_LB.setText(str(data[0]+1))
        self.ui.col_LB.setText(str(data[1]+1))
        self.ui.count_LB.setText(str(data[2]))

    @QtCore.Slot()
    def ctrl_init_finish_slot(self):
        self.ui.data_Btn.setEnabled(True)
        self.ui.start_Btn.setEnabled(True)
        self.ui.stop_Btn.setEnabled(True)
    
    @QtCore.Slot()
    def task_finish_slot(self):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setWindowTitle("！")
        MsgBox.setText("图像扫描完成:")
        MsgBox.setInformativeText("数据以保存在Data文件夹下")
        MsgBox.exec_()
        self.app_quit()

    @QtCore.Slot()
    def data_slot(self):
        self.DataDlg.show()
        self.DataDlg.update(self.Ctrler.Data) 