import unittest
import socket
import logging 
import time

import dapi2
import dboard
from dapi2.dcom.dsocket import DSocketExceptionNoAvailableConnection, DSocketExceptionNoConnectionSet


class TestDSocket(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        self.log.debug('setUp')
        self.board = None
        
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.connect(('sav.dassym.com', 30443))
        
        self.comm = dapi2.DSocket(self.mySocket)
        
        self.api = dapi2.DApi2(self.comm)
        
    def testBoard(self):
        data = self.comm.get_ext_conn()
        self.assertEqual(isinstance(data, list), True)
        self.assertEqual(len(data) > 0, True)
        self.assertEqual(isinstance(data[0], tuple), True)
        self.assertEqual(data[0][0], '0')
        #self.assertRegex(data, '([0-9]\/[a-zA-Z0-9]*\ [a-zA-Z0-9]*\ [a-zA-Z0-9]*\:)')
        res = self.comm.select_ext_conn(0)
        
        # self.api.readReg(self.api.regs.msr)
        self.board = dboard.DBoardFactory(self.api)
        self.assertIn(self.board.number, ['30', '92'])
        

         
        self.api.cmd.connect()
        
        print( ':'.join('{0:02x}'.format(b) for b in self.board.getMicrocontrollerID() ) )
         
        self.api.readRegGroup(self.api.regs.state)
        
        self.api.writeReg(self.api.regs.par, 1)
        
        self.api.readRegs(self.api.regs.ssr1, length=2)
        
        with self.assertRaises(dapi2.derror.DApiComError):
            self.api.cmd.flashBegin(1234)
        
        
        self.api.writeReg(self.api.regs.scr, 0xffff)
        
        self.api.writeReg(self.api.regs.smr, 1)
        
        time.sleep(1)
        
        self.api.readReg(self.api.regs.msr)
        
        self.board.setRegisters(smr=1, scr=8000, ccr=4000, acr=5, lir=120, ldr=1500, synchronous=True)
        
        time.sleep(3)
        
        self.api.cmd.motorReverse()
        
        time.sleep(3)
        
        self.board.setRegisters(smr=0, scr=0)

        self.api.readRegs(self.api.regs.ssr1, length=2)
        self.api.syncRegs()
        
    def testErrorNoAvailableConnexion(self):
        with self.assertRaises(DSocketExceptionNoAvailableConnection):
            self.comm.get_ext_conn()
        
    def testErrorNoPatchSet(self):
        with self.assertRaises(DSocketExceptionNoConnectionSet):
            self.comm.sendMessage("hello")
        with self.assertRaises(DSocketExceptionNoConnectionSet):
            self.comm.receiveMessage()
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        try:
            self.board.disconnect()
        except:
            pass
        del self.board
        self.comm.close()
        