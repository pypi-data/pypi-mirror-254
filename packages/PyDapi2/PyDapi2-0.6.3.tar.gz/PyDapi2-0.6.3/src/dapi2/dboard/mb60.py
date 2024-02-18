'''Module to define the class of MB-60 Dassym's electronic board representation.

:author: F. Voillat
:date: 2021-02-24 Creation
'''
from .base import DBoard, DBoardPreferredDapiMode
from .analoginput import PressureSensor, VoltageSensor, PowerSupplySensor



class Board60(DBoard):
    '''Class for MB-60 Dassym's board.

    .. inheritance-diagram:: Board60
        :parts: 1

    '''

    number = '60'
    '''Board type number (str)'''

    REG_GROUPS = tuple(list(DBoard.REG_GROUPS) + ['extended'])

    def __init__(self, dapi, dmode=DBoardPreferredDapiMode.REGISTER):
        '''Constructor'''
        super().__init__(dapi, dmode)
        self._analog_inputs = dict(
                ((sensor.name, sensor) for sensor in (
                    PressureSensor(self, 'Pressure', 'prcr'),
                    VoltageSensor(self, 'Reference', 'elcr'),
                    VoltageSensor(self, 'Analog #0', 'an0r'),
                    VoltageSensor(self, 'Analog #1', 'an1r'),
                    PowerSupplySensor(self, 'Power supply', 'psvr' ),)
                    )
            )
        self.speed_range.set(0,40000)