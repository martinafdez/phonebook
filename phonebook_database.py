# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:22:03 2019

@author: mluci
"""

import sqlite3 
import json
import random
import requests


############### Database connection #####################
conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

############### BUSINESS TABLE ##########################
def create_table_business():
    c.execute('CREATE TABLE IF NOT EXISTS business(businessId REAL, nameBusiness TEXT, typeBusiness TEXT, addressLine1 VARCHAR(255), city TEXT, country TEXT, postcode VARCHAR(10), phoneNumber REAL)')
    

def populate_table_business():
    with open('data_business.json') as f:
        dataBusiness = json.load(f)
        for row in dataBusiness:
            businessId = random.randint(0,100000)
            nameBusiness = row["business name"]
            typeBusiness = row["business_category"]
            addressLine1 = row["address_line_1"]
            city = row["address_line_2"]
            country = row["address_line_3"]
            postcode = row["postcode"]
            phoneNumber = row["telephone_number"]
            c.execute("INSERT INTO business(businessId, nameBusiness, typeBusiness, addressLine1, city, country, postcode, phoneNumber) VALUES(?,?,?,?,?,?,?,?)", (businessId, nameBusiness, typeBusiness, addressLine1, city, country, postcode, phoneNumber))
    conn.commit()  


###############PEOPLE TABLE#######################
    
def create_table_people():
    c.execute('CREATE TABLE IF NOT EXISTS people(personId REAL, name TEXT, surname TEXT, addressLine1 VARCHAR(255), city TEXT, country TEXT, postcode VARCHAR(10), phoneNumber REAL)')
    
def populate_table_people():
    with open('data_people.json') as p:
        dataPeople = json.load(p)
        for row in dataPeople:
            personId = random.randint(0,100000)
            name = row["first_name"]
            surname = row["last_name"]
            addressLine1 = row["address_line_1"]
            city = row["address_line_2"]
            country = row["address_line_3"]
            postcode = row["postcode"]
            phoneNumber = row["telephone_number"]
            c.execute("INSERT INTO people(personId, name, surname, addressLine1, city, country, postcode, phoneNumber) VALUES(?,?,?,?,?,?,?,?)", (personId, name, surname, addressLine1, city, country, postcode, phoneNumber))
    conn.commit() 
    

############### POSTCODE TABLE #######################
def create_table_coordinates():
    c.execute('CREATE TABLE IF NOT EXISTS coordinates(postcode VARCHAR(10), latitude DECIMAL(10,8), longitude DECIMAL (11,8) ) ')
    

def populate_table_coordinates_people():
     endpoint="https://api.postcodes.io/postcodes/"
     c.execute('SELECT postcode FROM people')
     for row in c.fetchall():
        currentpostcode = row[0]
        
        c.execute('SELECT * FROM coordinates WHERE postcode = ?', (currentpostcode,))
        results = c.fetchall()
        if len(results) == 0: 
            postcode = str(currentpostcode).replace(' ', '')
            postcode = postcode.strip("'(),'")    
           # print("NOT DUPLICATE")
            postcode_response = requests.get(endpoint + postcode)
    
            data_postcode = postcode_response.json()
            if data_postcode['status'] == 200:
                longitude = data_postcode['result']['longitude']
                latitude = data_postcode['result']['latitude']
              #  print(longitude)
              #  print(latitude)
                
                c.execute("INSERT INTO coordinates(postcode, latitude, longitude) VALUES(?,?,?)", (currentpostcode, latitude, longitude))
        else:         
              print("DUPLICATE") 
        conn.commit()
        



create_table_business()
populate_table_business()

create_table_people()  
populate_table_people()  

create_table_coordinates()
populate_table_coordinates_people()


c.close()
conn.close()
