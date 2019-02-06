# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:12:22 2019

@author: mluci
"""
import requests
from math import sin, cos, sqrt, atan2, radians

#function to get business type query#

#function to get business name search query#


#function to get person search query#


#function to get users location#
def input_latlong():
    #let user input postcode and get its lat and long#
    userpostcode=input("enter postcode: ")
    endpoint_postcode="https://api.postcodes.io/postcodes/"
 
    postcode_response = requests.get(endpoint_postcode + userpostcode)
    data_postcode = postcode_response.json()
   # print(data_postcode)
    userlong=data_postcode['result']['longitude']
    userlat=data_postcode['result']['latitude']
    print(userlong)
    print(userlat)
    
    
input_latlong()

##function that caluclates distance using haversine formula##
def distance(lat1,long1,lat2,long2):

    R = 6373.0 # approximate radius of earth in km

    dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist


        
##function that calculates distance by calling the distance 
#function above and should compare distance between user's 
#latitude and longitude and all the lats/longs returned by 
#their search query#    
def get_nearest_neighbors(postcode):
    # get all postcodes in database
    query = "SELECT postcode, latitude, longitude FROM postcodes"
#    results = query_db(query)

    # get longitude and latitude of given postcode
    test = [i for i in query if i[0].lower().strip() == postcode.lower().strip()]
    if len(test) > 0:

        # select latitude and longitudes of matched postcode
        coords1 = (test[0][1],test[0][2])
    
        distances = [coords1(test[0][1],test[0][2],i[1], i[2]) for i in query]
        query = [query[i]+(distances[i],) for i in range(len(distances))]
        query.sort(key=lambda x: x[-1])
    
        return query
    else:
        print("No Postcode Match FOUND")
    
get_nearest_neighbors(postcode)    