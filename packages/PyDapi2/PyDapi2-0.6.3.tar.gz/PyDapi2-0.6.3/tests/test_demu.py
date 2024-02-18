import unittest
import socket
import logging 
import time

import dapi2
from demu.DEmuBaseBoard import DEmuBaseBoard
from demu.DEmuBaseMotor import DEmuBaseMotor
from dapi2.dapi2 import DApi2, DApi2Side, dmsg
from dapi2.dcom.demu import DEmu
import dboard

TRACE_INGOING_DAPI_FMT    = '{time:9.3f} | <-- | {buf:30s} | {msg.code!s}:{regs:s}'
        
        
TRACE_OUTGOING_DAPI_FMT   = '{time:9.3f} | --> | {buf:30s} | {msg.code!s}:{regs:s}'

class TestDSocket(unittest.TestCase):
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
        self.motor = DEmuBaseMotor()
        self.board = DEmuBaseBoard(self.motor)
        self.comm = DEmu(self.board, DApi2Side.MASTER, trace_callback=self.traceDapi)
        self.api = DApi2(self.comm)
        
    def testBoard(self):
        self.board = dboard.DBoardFactory(self.api, dboard.DBoardPreferedDapiMode.COMMAND)
        self.assertIn(self.board.number, ['30', '92'])
        
        self.api.readRegGroup(self.api.regs.state)
#         for v in self.api.regs.state:
#             print("{} ({}): {}".format(v, v.addr,v.value))

        self.api.writeReg(self.api.regs.par, 1)
        self.api.writeReg(self.api.regs.par, 2)
         
        self.api.writeReg(self.api.regs.smr, 1)
         
        self.api.writeReg(self.api.regs.scr, 8000)
         
        self.api.writeReg(self.api.regs.acr, 50)
         
        self.api.writeReg(self.api.regs.lir, 200)
         
        self.api.writeReg(self.api.regs.ldr, 100)
        self.board.setRegisters(smr=0, scr=8000, ccr=4000, acr=5, lir=120, ldr=1500, synchronous=True)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
        