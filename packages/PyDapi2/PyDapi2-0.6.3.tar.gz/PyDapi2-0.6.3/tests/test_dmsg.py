'''
Created on 30 janv. 2021

@author: fv
'''

import unittest

import dapi2

class TestMsgReader(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.reader = dapi2.dmsg.MsgReader(dapi2.Dapi2Side.MASTER)
    
    
    def test_00_isHexChar(self):
        self.assertTrue(self.reader.isHexChar(ord('0')))
        self.assertTrue(self.reader.isHexChar(ord('9')))
        self.assertTrue(self.reader.isHexChar(ord('A')))
        self.assertTrue(self.reader.isHexChar(ord('F')))
        self.assertFalse(self.reader.isHexChar(ord('a')))
        self.assertFalse(self.reader.isHexChar(ord('+')))
        self.assertFalse(self.reader.isHexChar(ord(' ')))
        self.assertFalse(self.reader.isHexChar(1))
        
    def test_01_hexCharToInt(self):
        self.assertEqual(self.reader.hexCharToInt(ord('0')), 0x0)
        self.assertEqual(self.reader.hexCharToInt(ord('9')), 0x9)
        self.assertEqual(self.reader.hexCharToInt(ord('A')), 0xA)
        self.assertEqual(self.reader.hexCharToInt(ord('F')), 0xF)
        
    def test_01_CRC(self):
        crc = dapi2.dmsg.CRC_INITIAL
        for c in b'011A02':
            crc = self.reader.crcChar(c, crc)
        self.assertEqual(crc,0xE467)
                            
    def test_10_ReadRegister(self):
        for c in b'\x01011A02E467':
            self.reader.putChar(c)
        #self.assertEqual(self.reader.crc(), 0xe467)
        self.assertEqual(self.reader.state, dapi2.dmsg.MsgReaderState.COMPLETE) 
        self.assertIsInstance(self.reader.getMessage(), dapi2.dmsg.ReadRegMessage)   
        self.assertEqual(self.reader.getMessage().type(), dapi2.dmsg.MsgType.READ)
        self.assertEqual(self.reader.getMessage().dataLen(), 1)
        self.assertEqual(self.reader.getMessage().addr(), 0x1A)
        self.assertEqual(self.reader.getMessage().data(0), 2)
        
        
    def test_11_WriteRegister(self):
        for c in b'\x01822B9C40C510':
            self.reader.putChar(c)
        #self.assertEqual(self.reader.crc(), 0xc510)
        self.assertEqual(self.reader.state, dapi2.dmsg.MsgReaderState.COMPLETE)   
        self.assertIsInstance(self.reader.getMessage(), dapi2.dmsg.WriteRegMessage) 
        self.assertEqual(self.reader.getMessage().type(), dapi2.dmsg.MsgType.WRITE)
        self.assertEqual(self.reader.getMessage().dataLen(), 2)
        self.assertEqual(self.reader.getMessage().addr(), 0x2B)
        self.assertEqual(self.reader.getMessage().data(0,2), 40000)
        

    def test_12_Command(self):
        for c in b'\x0122139C402D5B':
            self.reader.putChar(c)
        #self.assertEqual(self.reader.crc(), 0xc510)
        self.assertEqual(self.reader.state, dapi2.dmsg.MsgReaderState.COMPLETE)    
        self.assertIsInstance(self.reader.getMessage(), dapi2.dmsg.CommandMessage)
        self.assertEqual(self.reader.getMessage().dataLen(), 2)
        self.assertEqual(self.reader.getMessage().addr(), 0x13)
        self.assertEqual(self.reader.getMessage().data(0,2), 40000)
        
        