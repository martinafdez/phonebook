# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:37 2019

@author: mluci
""" 

import unittest
from unittest import mock
from database_functions_to_test import *



class DatabaseTest(unittest.TestCase):            
    #unit test for connecting#
    def test_connect_db(self):
        self.assertTrue(getdb('phonebook.db'))
    #unit test for whether database exists#
    def test_check_db(self):
        self.assertTrue(check_db("phonebook.db"))
    #check if database is empty#
    def test_empty_db(self):
        self.assertTrue(checkIfTables('phonebook.db'))  
    #check if tables in database are empty#
    def test_empty_table(self):
        self.assertTrue(checkIfTableEmpty('phonebook.db')) 
  
#comment
   
    
    
if __name__ == '__main__':   
    unittest.main()