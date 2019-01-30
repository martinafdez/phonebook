# testing git / iza

import sqlite3
import requests

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()
 

def typePostcode():
    userInputPostcode = input("Type in the postcode: ").upper()

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
        typeBizType(userInputPostcode)

    
def typeBizType(userInputPostcode):
    userInputBizType = input("Type in biz type: ").title()
    c.execute('SELECT * FROM business WHERE typeBusiness = ?', (userInputBizType,) )
    resultsBT = c.fetchall()
    
    if len(resultsBT ) == 0:
        print("Sorry, we have nothing! Try again.")
        typeBizType(userInputPostcode)
    else:
        c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (userInputPostcode, userInputBizType) )
    for row in c.fetchall():
        print(row)

typePostcode()



#def typeCity():
#    userInputCity = input("Type in the city: ").title()
#    userInputBizType = input("Type in biz type: ").title()
#    c.execute('SELECT * FROM business WHERE city = ? AND typeBusiness  = ?', (userInputCity, userInputBizType) )
#    for row in c.fetchall():
#        print(row)
#        
#typeCity()   

c.close()
conn.close()