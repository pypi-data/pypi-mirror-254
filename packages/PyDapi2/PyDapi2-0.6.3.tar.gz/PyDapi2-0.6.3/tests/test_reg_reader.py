'''
Created on 7 févr. 2021

@author: fv
'''
import unittest
import os.path

import dapi2



class ReagReaderTest(unittest.TestCase):


    def setUp(self):
        self.reader = dapi2.RegContainerReader() 


    def tearDown(self):
        pass


    def testReadXml(self):
        reg_container = self.reader.readFromFile(os.path.join(os.path.dirname(__file__),'regs.xml'))
        self.assertEqual(reg_container.size, 256)
        self.assertEqual(reg_container[0x48].name, 'smr')
        self.assertEqual(reg_container.ssr1.addr, 0x24)
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()