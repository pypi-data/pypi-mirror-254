'''
:date: 2021-02-28
:author: F. Voillat
'''

import sys
import time
# import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__),'src'))
import unittest
import serial
import logging 
import dapi2
from dapi2 import dmsg, dboard




logfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

TRACE_INGOING_DAPI_FMT    = '{time:9.3f} | <-- | {buf:30s} | {msg.code!s}:{regs:s}'
        
        
TRACE_OUTGOING_DAPI_FMT   = '{time:9.3f} | --> | {buf:30s} | {msg.code!s}:{regs:s}'


class TestBoard(unittest.TestCase):
    
    def traceRaw(self, time, direction, buf, msg):
        if direction == dapi2.DComTracingDirection.INGOING:
            print(dapi2.TRACE_INGOING_COLOR, end='')
            print(dapi2.TRACE_INGOING_RAW_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
        else:
            print(dapi2.TRACE_OUTGOING_COLOR, end='')
            print(dapi2.TRACE_OUTGOING_RAW_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
            
    def traceNormal(self, time, direction, buf, msg):
        if direction == dapi2.DComTracingDirection.INGOING:
            if msg.isError():
                print(dapi2.TRACE_INERROR_COLOR, end='')
            else:
                print(dapi2.TRACE_INGOING_COLOR, end='')
            print(dapi2.TRACE_INGOING_NORMAL_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
        else:
            if msg.isError():
                print(dapi2.TRACE_OUTERROR_COLOR, end='')
            else:
                print(dapi2.TRACE_OUTGOING_COLOR, end='')
            print(dapi2.TRACE_OUTGOING_NORMAL_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
            
    def traceDapi(self, time, direction, buf, msg):
        if msg.type() in (dapi2.MsgType.READ, dapi2.MsgType.WRITE):
            regs =  self.api.regs[msg.getAddr():msg.getAddr()+msg.getLength()//dapi2.REG_SIZE]
        elif msg.type() == dapi2.MsgType.COMMAND:
            return self.traceNormal(time, direction, buf, msg)
        else:
            return #self.traceNormal(time, direction, buf, msg)
        
        
        
        if direction == dapi2.DComTracingDirection.INGOING:
            if msg.isError():
                print(dapi2.TRACE_INERROR_COLOR, end='')
                regs = str(msg)
            else:
                print(dapi2.TRACE_INGOING_COLOR, end='')
                if isinstance(msg, (dmsg.WrittenRegMessage, dmsg.ValueRegMessage)) :
                    regs = ', '.join('{reg.name:s}=0x{v:04x} ({v:d})'.format(reg=r, v=msg.getRegValue(i), i=i) for i, r in enumerate(regs))
                else:
                    regs = '???'
            print(TRACE_INGOING_DAPI_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg, regs=regs), end='')
        else:
            if msg.isError():
                print(dapi2.TRACE_OUTERROR_COLOR, end='')
                regs = str(msg)
            else:
                print(dapi2.TRACE_OUTGOING_COLOR, end='')
                if isinstance(msg, dmsg.WriteRegMessage) :
                    regs = ', '.join('0x{v:04x}({v:d})=>{reg.name:s}'.format(reg=r, v=msg.getRegValue(i), i=i) for i, r in enumerate(regs))
                elif isinstance(msg, dmsg.ReadRegMessage):
                    regs = ', '.join('{reg.name:s}?'.format(reg=r) for r in regs)
                else:
                    regs = '???'
            print(TRACE_OUTGOING_DAPI_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg, regs=regs), end='')
        
        print(dapi2.TRACE_RESET_COLOR)
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        self.log.debug('setUp')
        self.board = None
        self.serial = serial.Serial('/dev/ttyUSB0', timeout=1)
        
        self.comm = dapi2.DSerial(self.serial, dapi2.DApi2Side.MASTER, trace_callback=self.traceDapi)
        
        self.api = dapi2.DApi2(self.comm)
        
        
        
    def testConnect(self):      
        self.board = dboard.DBoardFactory(self.api, dboard.DBoardPreferedDapiMode.COMMAND)
        self.assertIn(self.board.number, ['30', '92'])
        
        self.api.readRegGroup(self.api.regs.state)
#         for v in self.api.regs.state:
#             print("{} ({}): {}".format(v, v.addr,v.value))

        self.api.writeReg(self.api.regs.par, 1)
        self.api.writeReg(self.api.regs.par, 2)
        
        self.api.writeReg(self.api.regs.smr, 1)
        
        self.api.writeReg(self.api.regs.scr, 1)
#         self.log.debug('testConnect')
#         self.board = dboard.DBoardFactory(self.api, dboard.DBoardPreferedDapiMode.COMMAND)
#         self.assertIn(self.board.number, ['30', '92'])
#         
#         self.api.cmd.connect()
#          
#         print( ':'.join('{0:02x}'.format(b) for b in self.board.getMicrocontrollerID() ) )
#          
#           
#         self.api.readRegGroup(self.api.regs.state)
# #         
# #         for v in self.api.regs.state:
# #             print("{} ({}): {}".format(v, v.addr,v.value))
#         
#         self.api.writeReg(self.api.regs.par, 1)
#         
#         self.api.readRegs(self.api.regs.ssr1, length=2)
#         
#         with self.assertRaises(dapi2.derror.DApiComError):
#             self.api.cmd.flashBegin(1234)
#         
#         
#         self.api.writeReg(self.api.regs.scr, 0xffff)
#         
#         self.api.writeReg(self.api.regs.smr, 1)
#         
#         time.sleep(1)
#         
#         self.api.readReg(self.api.regs.msr)
#         
#         self.board.setRegisters(smr=0, scr=8000, ccr=4000, acr=5, lir=120, ldr=1500, synchronous=True)
#         time.sleep(3)
#         
#         self.api.cmd.motorReverse()
#         
#         time.sleep(3)
#         
#         self.board.setRegisters(smr=0, scr=0)
# 
#         self.api.readRegs(self.api.regs.ssr1, length=2)
#         self.api.syncRegs()
        
    def tearDown(self):
        try:
            self.board.disconnect()
        except:
            pass
        del self.board
         
        self.serial.close() 
        unittest.TestCase.tearDown(self)




    
