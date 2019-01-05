# -*- coding:utf-8 -*-

import ctypes


class mppcum1a(object):

    INVALID_HANDLE_VALUE = -1
    MPPC_SUCCESS = 0
    MPPC_UNSUCCESS = 1
    MPPC_INVALID_HANDLE = 2
    MPPC_INVALID_VALUE = 3
    MPPC_NOT_UPDATED = 4
    MPPC_NON_SUPPORT = 5

    MPPC_UNSTABLE_STATE = 11
    MPPC_PELTIER_DISABLE = 12
    MPPC_PELTIER_TIMEOUT = 13
    MPPC_ERROR_MODULE = 14
    MPPC_ERROR_TEMP = 15

    MPPC_CHECK_NORMAL = 21
    MPPC_CHECK_INVALID = 22
    MPPC_CHECK_REMOVE = 23

    DISABLE = 0
    ENABLE = 1

    VTH_05 = 0
    VTH_15 = 1
    VTH_25 = 2
    VTH_35 = 3
    VTH_45 = 4
    VTH_55 = 5
    VTH_65 = 6
    VTH_75 = 7
    VTH_OVER = 40

    @staticmethod
    def MPPC_OpenDevice():
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_OpenDevice()

    @staticmethod
    def MPPC_OpenTargetDevice(UnitID):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_OpenTargetDevice(UnitID)

    @staticmethod
    def MPPC_CloseDevice(DeviceHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        dll.MPPC_CloseDevice(DeviceHandle)

    @staticmethod
    def MPPC_CheckDevice(DeviceHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_CheckDevice(DeviceHandle)

    @staticmethod
    def MPPC_OpenPipe(DeviceHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_OpenPipe(DeviceHandle)

    @staticmethod
    def MPPC_ClosePipe(PipeHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        dll.MPPC_ClosePipe(PipeHandle)

    @staticmethod
    def MPPC_ReadTypeNumber(DeviceHandle, TypeNumber):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_ReadTypeNumber(DeviceHandle, TypeNumber)

    @staticmethod
    def MPPC_ReadUnitID(DeviceHandle, UnitID):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_ReadUnitID(DeviceHandle, UnitID)

    @staticmethod
    def MPPC_Initialize(DeviceHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_Initialize(DeviceHandle)

    @staticmethod
    def MPPC_GetProperty(DeviceHandle, GateTime, DataSize):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetProperty(DeviceHandle, ctypes.byref(GateTime), ctypes.byref(DataSize))

    @staticmethod
    def MPPC_SetProperty(DeviceHandle, GateTime, DataSize):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_SetProperty(DeviceHandle, GateTime, DataSize)

    @staticmethod
    def MPPC_GetThreshold(DeviceHandle, Level):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetThreshold(DeviceHandle, ctypes.byref(Level))

    @staticmethod
    def MPPC_SetThreshold(DeviceHandle, Level):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_SetThreshold(DeviceHandle, Level)

    @staticmethod
    def MPPC_GetThresholdVoltage(DeviceHandle, Voltage):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetThresholdVoltage(DeviceHandle, ctypes.byref(Voltage))

    @staticmethod
    def MPPC_SetThresholdVoltage(DeviceHandle, Voltage):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_SetThresholdVoltage(DeviceHandle, Voltage)

    @staticmethod
    def MPPC_GetTemperature(DeviceHandle, Temperature):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetTemperature(DeviceHandle, ctypes.byref(Temperature))

    @staticmethod
    def MPPC_GetPeltierControl(DeviceHandle, ControlFlags):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetPeltierControl(DeviceHandle, ctypes.byref(ControlFlags))

    @staticmethod
    def MPPC_SetPeltierControl(DeviceHandle, ControlFlags):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_SetPeltierControl(DeviceHandle, ControlFlags)

    @staticmethod
    def MPPC_GetPeltierStatus(DeviceHandle):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetPeltierStatus(DeviceHandle)

    @staticmethod
    def MPPC_GetCounterData(DeviceHandle, PipeHandle, DataSize, DataArea):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetCounterData(DeviceHandle, PipeHandle, DataSize, ctypes.byref(DataArea))

    @staticmethod
    def MPPC_GetCounterDataCooled(DeviceHandle, PipeHandle, DataSize, DataArea):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        return dll.MPPC_GetCounterDataCooled(DeviceHandle, PipeHandle, DataSize, ctypes.byref(DataArea))

    @staticmethod
    def MPPC_GetDllVersion(Version):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        dll.MPPC_GetDllVersion(ctypes.byref(Version))

    @staticmethod
    def MPPC_GetSysVersion(Version):
        dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")
        dll.MPPC_GetSysVersion(ctypes.byref(Version))
