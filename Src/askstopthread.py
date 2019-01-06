# -*- coding:utf-8 -*- 

import time
from PySide2 import QtCore

class AskStopThread(QtCore.QThread):
    def __init__(self, Serial, is_stop):
        super(AskStopThread, self).__init__()

        self.Serial = Serial
        self.is_stop = is_stop
        self.Stop = False

    def run(self):
        while not self.Stop:
            if self.Serial.isOpen() == False:
                self.quit()

            count = 0
            while True:
                num = self.Serial.inWaiting()

                if num != 0:
                    ReceiveData = self.Serial.read(num)
                    Data = ReceiveData.decode()
                    #print(Data)
                    if Data.find("ST=00") != -1:
                        self.is_stop(True)
                        break

                else:
                    if count >= 20 :
                        break 
                    count = count + 1
                    time.sleep(0.01)
        self.Stop = False

    @QtCore.Slot()
    def stop(self):
        self.Stop = True
