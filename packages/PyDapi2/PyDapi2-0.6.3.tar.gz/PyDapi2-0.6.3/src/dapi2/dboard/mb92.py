'''Module to define the class of MB-92 Dassym's electronic board representation.

:author: F. Voillat
:date: 2021-02-24 Creation
'''
from .base import DBoard, DBoardPreferredDapiMode
from .analoginput import PressureSensor, PercentSensor, PowerSupplySensor


class Board92(DBoard):
    '''Class for MB-92 Dassym's board.

    .. inheritance-diagram:: Board92
        :parts: 1

    '''

    number = '92'
    '''Board type number (str)'''



    def __init__(self, dapi, dmode=DBoardPreferredDapiMode.REGISTER):
        '''Constructor'''
        super().__init__(dapi, dmode)
        self._analog_inputs = dict(
                ((sensor.name, sensor) for sensor in (
                    PressureSensor(self, 'Pressure', 'prcr'),
                    PercentSensor(self, 'Reference', 'elcr'),
                    PercentSensor(self, 'Analog #0', 'an0r'),
                    PercentSensor(self, 'Analog #1', 'an1r'),
                    PowerSupplySensor(self, 'Power supply', 'psvr' ),)
                    )
            )
        self.speed_range.set(100,40000)

class Board92B(Board92):
    ext = 'B'
