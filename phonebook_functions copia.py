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
 
def typePostcode():
    userInputPostcode = input("Type in postcode: ")

#    if userInputPostcode.isalpha():
#    #CITY
#        userInputPostcodeOrCity = userInputPostcodeOrCity.title()
#        print("it's a city!")
#        print(userInputPostcodeOrCity)
#        c.execute('SELECT * FROM business WHERE city = ?', (userInputPostcodeOrCity,) )
#    
#    
#        resultsC = c.fetchall()
#    
#        if len(resultsC) == 0:
#            print("Sorry, nothing in this city. Try again.")
#            typePostcodeOrCity()
#        else:
#            typeBizTypeOrName(userInputPostcodeOrCity)
#
#    else: 
#        #POSTCODE
    userInputPostcode = userInputPostcode.upper()
    while len(userInputPostcode) < 6 or len(userInputPostcode)>8:
        try:
            print("Please enter full postcode")
            userInputPostcode = input("Type in the postcode: ").upper()

        except  len(userInputPostcode) == 3 or len(userInputPostcode) == 2:
            print("Please enter both parts of the postcode")
            userInputPostcode = input("Type in the postcode: ").upper()

    
    c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcode,) )

    resultsPC = c.fetchall()

    if len(resultsPC ) == 0:
        print("Sorry, nothing for this postcode! Try again.")
        typePostcode()
    else:
        typeBizTypeOrName(userInputPostcode)


def businessAtLocation(userInputPostcode):
    options =[]

    c.execute('SELECT* FROM business WHERE postcode = ?', (userInputPostcode,) )
    for row in c.fetchall():
        if row[2] not in options:
            options.append(row[2])
    print(options)



# ask for user input BIZTYPE or BIZNAME, check if in 
def typeBizTypeOrName(userInputPostcode):
    print("Here are business type options for your location:")
    businessAtLocation(userInputPostcode)
    userInputBizTypeOrName = input("Type in name or type of business: ").title()

    c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness = ? OR nameBusiness  = ?', (userInputPostcode, userInputBizTypeOrName, userInputBizTypeOrName, ) )
    resultsFinalPc =  c.fetchall()
    
    if len(resultsFinalPc) != 0:
        print('Here your search result: ')
        print(sorted(resultsFinalPc, key=lambda kv : kv[1]))
#        alphabethOrder = sorted(resultsFinalPc, key=lambda kv : kv[1])
#        if 
    else:
        print("Sorry, nothing for " + userInputBizTypeOrName + " in " + userInputPostcode + ". Try again!")
        typePostcode()

typePostcode()


c.close()
conn.close()

# Comment
