'''

:author: fv
:date: Created on 16 juin 2021
'''
from .common import BaseBoardItem, CalibrationProcessState
from ..dreg.register import Register



class BaseAnalogInput(BaseBoardItem):
    CAL_NEEDED = False
    FMT = '{0:0.0f}%'
    FACTOR = 1/100

    def __init__(self, board, name, reg, maximum=100):
        super().__init__(board, name)
        self.maximum = maximum
        if not isinstance(reg, Register):
            self._reg = self.board.regs.getRegister(reg)
        else:
            self._reg = reg
        self.cal_process_state = CalibrationProcessState.IDLE

    def isCalibrated(self):
        return self._board.regs.sfr.value & (1<<(1+self.CAL_INDEX))

    def getRawValue(self, refresh=False):
        if refresh:
            self._board.readReg(self.reg)
        return self._reg.value


    def getValue(self, refresh=False):
        return float(self.getRawValue(refresh)) * self.FACTOR

    def calibration(self, phase, param=None):
        assert False, 'TODO:calibration'

    @property
    def reg(self):
        return self._reg
    @property
    def rawValue(self):
        return self.getRawValue()
    @property
    def value(self):
        return self.getValue()

class PercentSensor(BaseAnalogInput):
    pass

class PressureSensor(BaseAnalogInput):
    CAL_NEEDED = True
    CAL_INDEX = 1

    def __init__(self, board, name, reg, maximum=4.0):
        super().__init__(board, name, reg, maximum)


class VoltageSensor(BaseAnalogInput):
    FACTOR = 1/1000
    FMT = '{0:0.02f}V'

    def __init__(self, board, name, reg, maximum=5.0):
        super().__init__(board, name, reg, maximum)

class PowerSupplySensor(VoltageSensor):
    def __init__(self, board, name, reg, maximum=42):
        super().__init__(board, name, reg, maximum)

class CurrentSensor(BaseAnalogInput):
    FACTOR = 1/1000
    FMT = '{0:0.02f}A'

    def __init__(self, board, name, reg, maximum=8.0):
        super().__init__(board, name, reg, maximum)


