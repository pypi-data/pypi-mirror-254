'''

:author:  F. Voillat
:date: 2021-09-13 Creation
:copyright: Dassym SA 2021
'''
from .common import BaseBoardItem
from dapi2.dreg.base import DRegAccess




class DebugValue(BaseBoardItem):

    def __init__(self, board, reg, index=None, size=16):
        BaseBoardItem.__init__(self, board, name=reg.name)
        self._reg = reg
        self._index = index if index != None else reg.index
        self._size = size
        self.values = []
        self._callback_list = []
        self._reg.changed.connect(self.onRegisterChange)
        if self._reg.isDefined():
            self.onRegisterChange(self._reg, self._reg.value, self._reg.value)

    def __getitem__(self, index):
        return self.values[index]

    def __len__(self):
        return len(self.values)

    def setSize(self, size):
        self._size = size
        if self._size < len(self):
            self.values = self.values[:self._size]

    def connect(self, callback):
        if all(x != callback for x in self._callback_list):
            self._callback_list.append(callback)

    def disconnect(self, callback):
        self._callback_list.remove(callback)

    def onRegisterChange(self, reg, old_value=None, new_value=None):
        self.board.log.debug('DebugValue.onRegisterChange')
        if new_value is None:
            new_value = reg.value
        self.values = ([new_value]+self.values)[:self._size]

        for func in self._callback_list:
            func(self)

    def setValue(self, value):
        self._reg.internalSet(value, True)
        self.board.dapi.syncRegs()

    @property
    def reg(self):
        return self._reg

    @property
    def writable(self):
        return self._reg.access >= DRegAccess.WRITE

    @property
    def index(self):
        return self._index


    @property
    def value(self):
        try:
            return self.values[0]
        except IndexError:
            return None

    @value.setter
    def value(self, value):
        self.setValue(value)



