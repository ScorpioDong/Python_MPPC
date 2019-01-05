# -*- coding:utf-8 -*-

import ctypes

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

dll = ctypes.WinDLL("MPPCModule/mppcum1a.dll")


def MPPC_OpenDevice():
    return dll.MPPC_OpenDevice()


def MPPC_OpenTargetDevice(UnitID):
    return dll.MPPC_OpenTargetDevice(UnitID)


def MPPC_CloseDevice(DeviceHandle):
    dll.MPPC_CloseDevice(DeviceHandle)


def MPPC_CheckDevice(DeviceHandle):
    return dll.MPPC_CheckDevice(DeviceHandle)


def MPPC_OpenPipe(DeviceHandle):
    return dll.MPPC_OpenPipe(DeviceHandle)


def MPPC_ClosePipe(PipeHandle):
    dll.MPPC_ClosePipe(PipeHandle)


def MPPC_ReadTypeNumber(DeviceHandle, TypeNumber):
    return dll.MPPC_ReadTypeNumber(DeviceHandle, TypeNumber)


def MPPC_ReadUnitID(DeviceHandle, UnitID):
    return dll.MPPC_ReadUnitID(DeviceHandle, UnitID)


def MPPC_Initialize(DeviceHandle):
    return dll.MPPC_Initialize(DeviceHandle)


def MPPC_GetProperty(DeviceHandle, GateTime, DataSize):
    return dll.MPPC_GetProperty(DeviceHandle, ctypes.byref(GateTime), ctypes.byref(DataSize))


def MPPC_SetProperty(DeviceHandle, GateTime, DataSize):
    return dll.MPPC_SetProperty(DeviceHandle, GateTime, DataSize)


def MPPC_GetThreshold(DeviceHandle, Level):
    return dll.MPPC_GetThreshold(DeviceHandle, ctypes.byref(Level))


def MPPC_SetThreshold(DeviceHandle, Level):
    return dll.MPPC_SetThreshold(DeviceHandle, Level)


def MPPC_GetThresholdVoltage(DeviceHandle, Voltage):
    return dll.MPPC_GetThresholdVoltage(DeviceHandle, ctypes.byref(Voltage))


def MPPC_SetThresholdVoltage(DeviceHandle, Voltage):
    return dll.MPPC_SetThresholdVoltage(DeviceHandle, Voltage)


def MPPC_GetTemperature(DeviceHandle, Temperature):
    return dll.MPPC_GetTemperature(DeviceHandle, ctypes.byref(Temperature))


def MPPC_GetPeltierControl(DeviceHandle, ControlFlags):
    return dll.MPPC_GetPeltierControl(DeviceHandle, ctypes.byref(ControlFlags))


def MPPC_SetPeltierControl(DeviceHandle, ControlFlags):
    return dll.MPPC_SetPeltierControl(DeviceHandle, ControlFlags)


def MPPC_GetPeltierStatus(DeviceHandle):
    return dll.MPPC_GetPeltierStatus(DeviceHandle)


def MPPC_GetCounterData(DeviceHandle, PipeHandle, DataSize, DataArea):
    return dll.MPPC_GetCounterData(DeviceHandle, PipeHandle, DataSize, ctypes.byref(DataArea))


def MPPC_GetCounterDataCooled(DeviceHandle, PipeHandle, DataSize, DataArea):
    return dll.MPPC_GetCounterDataCooled(DeviceHandle, PipeHandle, DataSize, ctypes.byref(DataArea))


def MPPC_GetDllVersion(Version):
    dll.MPPC_GetDllVersion(ctypes.byref(Version))


def MPPC_GetSysVersion(Version):
    dll.MPPC_GetSysVersion(ctypes.byref(Version))
