# -*- coding:utf-8 -*-

import serial
import time
import threading
from PySide2 import QtCore
from MPPCModule.MPPCModule import mppcum1a

class Control(QtCore.QObject):

    data_trans_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.Serial = serial.Serial()
        self.ReceiveThread = threading.Thread(target=self.receive_data)
        self.ReceiveThread.setDaemon(True)
        self.AskStaticThread = threading.Thread(target=self.ask_static)
        self.AskStaticThread.setDaemon(True)

        self.data_trans_signal.connect(self.data_trans_slot)

        self.serial_init()
        self._BOOL = True

    def serial_init(self):
        self.Serial.baudrate = 9600
        self.Serial.bytesize = serial.EIGHTBITS
        self.Serial.parity = serial.PARITY_NONE
        self.Serial.stopbits = serial.STOPBITS_ONE
        self.Serial.timeout = 0.5
        self.Serial.writeTimeout = 0.5

    def serial_open(self, Port):
        self.Serial.name = Port
        try:
            self.Serial.open()
        except:
            print("Serial open failed!")
            return False
        
        self.ReceiveThread.start()
        self.AskStaticThread.start()
        return True

    def ask_static(self):
        while self._BOOL:
            self.Serial.write("?ST/")
            time.sleep(0.03)

    def receive_data(self):
        while True:
            self.ReceiveData = self.Serial.readline()
            self.data_trans_signal.emit()

    @QtCore.Slot()
    def data_trans_slot(self):
        Receive = self.ReceiveData
        if Receive.find("ST=") != -1:
            pass
