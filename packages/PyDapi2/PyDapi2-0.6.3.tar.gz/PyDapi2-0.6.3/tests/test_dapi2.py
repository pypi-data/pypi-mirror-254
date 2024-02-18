'''
:date: 2021-02-28
:author: F. Voillat
'''

import sys
# import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__),'src'))
import unittest

import logging 
import dapi2
from dapi2 import dmsg, dboard




logfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)



class TestDapi2(unittest.TestCase):
    
    #===========================================================================
    # def traceRaw(self, time, direction, buf, msg):
    #     if direction == dapi2.DComTracingDirection.INGOING:
    #         print(dapi2.TRACE_INGOING_RAW_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
    #     else:
    #         print(dapi2.TRACE_OUTGOING_RAW_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
    #         
    # def traceNormal(self, time, direction, buf, msg):
    #     if direction == dapi2.DComTracingDirection.INGOING:
    #         print(dapi2.TRACE_INGOING_NORMAL_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
    #     else:
    #         print(dapi2.TRACE_OUTGOING_NORMAL_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg))
    #         
    # def traceDapi(self, time, direction, buf, msg):
    #     
    # 
    #     if msg.type() in (dapi2.MsgType.READ, dapi2.MsgType.WRITE):
    #         regs =  self.api.regs[msg.getAddr():msg.getAddr()+msg.getLength()//dapi2.REG_SIZE]
    #     elif msg.type() == dapi2.MsgType.COMMAND:
    #         self.traceNormal(time, direction, buf, msg)
    #     else:
    #         return #self.traceNormal(time, direction, buf, msg)
    #     
    #     
    #     
    #     if direction == dapi2.DComTracingDirection.INGOING:
    #         if msg.isError():
    #             print(dapi2.TRACE_INERROR_COLOR, end='')
    #             regs = str(msg)
    #         else:
    #             print(dapi2.TRACE_INGOING_COLOR, end='')
    #             if isinstance(msg, (dmsg.WrittenRegMessage, dmsg.ValueRegMessage)) :
    #                 regs = ', '.join('{reg.name:s}=0x{v:04x} ({v:d})'.format(reg=r, v=msg.getRegValue(i), i=i) for i, r in enumerate(regs))
    #             else:
    #                 regs = '???'
    #         print(TRACE_INGOING_DAPI_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg, regs=regs), end='')
    #     else:
    #         if msg.isError():
    #             print(dapi2.TRACE_OUTERROR_COLOR, end='')
    #             regs = str(msg)
    #         else:
    #             print(dapi2.TRACE_OUTGOING_COLOR, end='')
    #             if isinstance(msg, dmsg.WriteRegMessage) :
    #                 regs = ', '.join('0x{v:04x}({v:d})=>{reg.name:s}'.format(reg=r, v=msg.getRegValue(i), i=i) for i, r in enumerate(regs))
    #             elif isinstance(msg, dmsg.ReadRegMessage):
    #                 regs = ', '.join('{reg.name:s}?'.format(reg=r) for r in regs)
    #             else:
    #                 regs = '???'
    #         print(TRACE_OUTGOING_DAPI_FMT.format(time=time, buf=dapi2.buffer2str(buf), msg=msg, regs=regs), end='')
    #     
    #     print(dapi2.TRACE_RESET_COLOR)
    #===========================================================================
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        self.log.debug('setUp')
        
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)




    
