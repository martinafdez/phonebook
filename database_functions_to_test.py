# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:14:35 2019

@author: mluci
"""

import sqlite3
import os


####connect to the database####
def getdb(db_file):
    try: 
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        return c
    except: 
        return False

###check if database exists###
def check_db(db_file):
    if os.path.exists(db_file):
        return True 
    else:
        return False
    
    
###Check if database is empty####
def checkIfTables(db_file):
    c=getdb(db_file)
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablesInDb =(c.fetchall())
    print(len(tablesInDb))
    print(tablesInDb)
    if len(tablesInDb) > 0:
        print("Tables available.")
        return True
    else:
        print("table unavailable")
        return False
    dbClose(db_file)

####Check if tables in database are empty###
def checkIfTableEmpty(db_file):
    try:
        c = getdb(db_file)
        c.execute('SELECT * FROM business')
        resultsRecords = c.fetchall()
        if len(resultsRecords ) > 0:
            print("Table not empty")
            return True
        else:
            print("Table is empty")
            return False
    except sqlite3.OperationalError:
        print("Table doesn't exist. Can't run check.")
        
    
    
    dbClose(db_file)
    


####Close database####
def dbClose(db_file):
    c =getdb(db_file)
    conn = getdb(db_file)
    
    c.close()
    conn.close()        
#dbClose()  
    
    





