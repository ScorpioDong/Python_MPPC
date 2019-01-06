# -*- coding:utf-8 -*-

import serial
import time
import numpy as np
import ctypes
from Src.askstopthread import AskStopThread
from PySide2 import QtCore
from MPPCModule.MPPCModule import mppcum1a


class Control(QtCore.QObject):

    data_trans_signal = QtCore.Signal(str)
    serial_open_failed_signal = QtCore.Signal()
    askstopthread_stop_signal = QtCore.Signal()
    task_finish_signal = QtCore.Signal()
    data_show_signal = QtCore.Signal(list)

    def __init__(self):
        super().__init__()

        self._isStop = True
        self.RowN = 0
        self.ColN = 0
        self.isPause = False

    @QtCore.Slot(dict)
    def init(self, Parmas):
        self.Parmas = Parmas
        self.Data = np.zeros((self.Parmas['row'], self.Parmas['col']))
        if self.serial_init(self.Parmas['serial_name']) == False:
            self.serial_open_failed_signal.emit()
            return
        self.mt_speed_config(self.Parmas['x_speed'], self.Parmas['y_speed'])

    def serial_init(self, Port):
        self.Serial = serial.Serial(Port, 115200, timeout=0.5)

        self.AskStopThread = AskStopThread(self.Serial, self.is_stop)
        self.askstopthread_stop_signal.connect(self.AskStopThread.stop)

        if self.Serial.isOpen() == True:
            self.Serial.close()
        # self.Serial.name = Port
        # self.Serial.baudrate = 9600
        self.Serial.bytesize = serial.EIGHTBITS
        self.Serial.parity = serial.PARITY_NONE
        self.Serial.stopbits = serial.STOPBITS_ONE
        self.Serial.timeout = 0.02
        self.serial_writeTimeout = None

        try:
            self.Serial.open()
        except:
            print("Serial open failed!")
            return False

        return True

    def is_stop(self, isStop):
        self._isStop = isStop

    def serial_write(self, String):
        #print(String)
        self.Serial.write(String.encode())

    def mt_speed_config(self, XSpeed, YSpeed):
        self.serial_write("VX=%d/" % XSpeed)
        self.serial_write("VY=%d/" % YSpeed)

    def mt_x_one_step(self, isForward):
        if isForward == True:
            self.serial_write("X:%d/" % self.Parmas['x_step'])
        else:
            self.serial_write("X:-%d/" % self.Parmas['x_step'])
        self.wait_stop()

    def mt_y_one_step(self):
        self.serial_write("Y:%d/" % self.Parmas['y_step'])
        self.wait_stop()

    def mppc_get_count(self):
        return 255
        sumData = 0.0
        array = np.zeros(self.Parmas['datasize'], dtype=np.int32)
        datarray = array.tolist()
        dat = (ctypes.c_int * self.Parmas['datasize'])(*(datarray))
        while True:
            result = mppcum1a.MPPC_GetCounterData(
                self.Parmas['device_handle'], self.Parmas['pipe_handle'], self.Parmas['datasize'], dat)
            if result == mppcum1a.MPPC_NOT_UPDATED:
                time.sleep(0.02)
                continue
            elif result == mppcum1a.MPPC_SUCCESS:
                for i in range(0, self.Parmas['datasize']-1):
                    sumData = sumData + float(dat[i])
                Data = sumData / \
                    self.Parmas['datasize'] / self.Parmas['gatetime']
                return Data

    def wait_stop(self):
        self._isStop = False
        while True:
            if self._isStop == True:
                return
            self.serial_write("?ST/")
            time.sleep(0.02)

    @QtCore.Slot()
    def run(self):
        self.AskStopThread.start()
        while not self.isPause:
            if self.ColN == self.Parmas['col'] or self.ColN == -1:
                self.RowN = self.RowN + 1
                if self.RowN == self.Parmas['row']:
                    self.task_finish_signal.emit()
                    break
                else :
                    if self.ColN == self.Parmas['col']:
                        self.ColN = self.ColN - 1
                        self.mt_y_one_step()
                    else:
                        self.ColN = self.ColN + 1
                        self.mt_y_one_step()
            else:
                self.Data[self.RowN, self.ColN] = self.mppc_get_count()
                self.data_show_signal.emit([self.RowN,self.ColN,self.Data[self.RowN, self.ColN]])
                if self.RowN % 2 == 0:
                    self.ColN = self.ColN + 1
                    self.mt_x_one_step(True)
                else:
                    self.ColN = self.ColN - 1
                    self.mt_x_one_step(False)
            
        self.askstopthread_stop_signal.emit()
        self.isPause = False
