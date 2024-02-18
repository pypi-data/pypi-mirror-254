'''
Created on 30 janv. 2021

@author: fv
'''

import unittest

import dapi2

class TestReg(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.container = dapi2.RegContainer()
