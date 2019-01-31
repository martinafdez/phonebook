# testing git / iza

import sqlite3
import requests

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()
 
#TAKING USER INPUT  - postcode or city

#if the input is letters only, we are assuming CITY
##if city, check if a database call will return any rsults. If so, ask for the biz type. If not, ask for input again

#else we are assuming it's a POSTCODE
##if postcode, check if lenght of input matches a regular postcode if so, check if a database call will return any results. If so, ask for the biz type. If not, ask for input again
 
def typePostcodeOrCity():
    userInputPostcodeOrCity = input("Type in city or postcode: ")

    if userInputPostcodeOrCity.isalpha():
    #CITY
        userInputPostcodeOrCity = userInputPostcodeOrCity.title()
        print("it's a city!")
        print(userInputPostcodeOrCity)
        c.execute('SELECT * FROM business WHERE city = ?', (userInputPostcodeOrCity,) )
    
    
        resultsC = c.fetchall()
    
        if len(resultsC) == 0:
            print("Sorry, nothing in this city. Try again.")
            typePostcodeOrCity()
        else:
            typeBizTypeOrName(userInputPostcodeOrCity)

    else: 
        #POSTCODE
        userInputPostcodeOrCity = userInputPostcodeOrCity.upper()
        while len(userInputPostcodeOrCity) < 6 or len(userInputPostcodeOrCity)>8:
            try:
                print("Please enter full postcode or name of a city")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
    
            except  len(userInputPostcodeOrCity) == 3 or len(userInputPostcodeOrCity) == 2:
                print("Please enter both parts of the postcode")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
    
        
        c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcodeOrCity,) )
    
        resultsPC = c.fetchall()
    
        if len(resultsPC ) == 0:
            print("Sorry, nothing for this postcode! Try again.")
            typePostcodeOrCity()
        else:
            typeBizTypeOrName(userInputPostcodeOrCity)

# ask for user input BIZTYPE or BIZNAME, check if in 
def typeBizTypeOrName(userInputPostcodeOrCity):
    userInputBizTypeOrName = input("Type in name or type of business: ").title()

    c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness OR nameBusiness  = ?', (userInputPostcodeOrCity, userInputBizTypeOrName) )
    resultsFinalPc =  c.fetchall()
    if len(resultsFinalPc) != 0:
            print(resultsFinalPc)
    else:
        c.execute('SELECT * FROM business WHERE city = ? AND typeBusiness OR nameBusiness = ?', (userInputPostcodeOrCity, userInputBizTypeOrName) )
        resultsFinalC =  c.fetchall()
        
        if len(resultsFinalC) != 0:
            print(resultsFinalC)
        else:
            print("Sorry, nothing for " + userInputBizTypeOrName + " in " + userInputPostcodeOrCity + ". Try again!")
            typePostcodeOrCity()

typePostcodeOrCity()


c.close()
conn.close()


