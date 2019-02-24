#!/usr/bin/python

ipstackKey = 'dda3662f819f46b239b617b56206ae17'
openWeather_key = '8c8af1132f7ae0f0b26f7fa6c06d7f71'

degree_sign= u'\N{DEGREE SIGN}'

from urllib.request import urlopen
import json


"""Obtain and print my current IP"""
from requests import get
myIP = get('https://ipapi.co/ip/').text
#print(myIP)


def load_json_by_URL(full_URL):
    myapiResponse = urlopen(full_URL)

    myloadedJson = json.load(myapiResponse)

    return(myloadedJson)


def url_for_ipstack():
    ipstack_URL_base = 'http://api.ipstack.com/'
    ipstack_URL = ipstack_URL_base + myIP + "?access_key=" + ipstackKey
#    print('ipstack_request is',ipstack_URL)
    return(ipstack_URL)

"""Obtain my location by IP from ipstack"""

location = load_json_by_URL(url_for_ipstack())
myCountryCode = location['country_code']
myCity = location['city']
#print("My Country Code = ",myCountryCode)
#print("My City = ",myCity)


"""Obtain current weather on my location"""

openWeather_URL_base = 'http://api.openweathermap.org/data/2.5/weather?q='
openWeather_URL = openWeather_URL_base + myCity + ',' + myCountryCode + '&units=metric&APPID=' + openWeather_key
#print(openWeather_URL)


myWeather = load_json_by_URL(openWeather_URL)
mainWeather = myWeather['main']
temperature = mainWeather['temp']
descriptionWeather = myWeather['weather']
descText = descriptionWeather[0]['description']
fo = open('myWeather','w')
print("Session 1 - Exercise2 ")
string1 = "At my IP current location " + myIP + " in " + str(myCity) + " " + str(myCountryCode) + " the temperature is " + str(temperature) + degree_sign +" with "+descText


print(string1)
fo.write(string1)
fo.close()

### create list of cities

city_list = ['London','Moscow','New York','Jerusalem','Milano','Cairo','Madrid']
for city in city_list:
    openWeather_URL = openWeather_URL_base + city + '&units=metric&APPID=' + openWeather_key
    cityWeather = load_json_by_URL(openWeather_URL)
    mainWeather = cityWeather['main']
    temperature = mainWeather['temp']
    sysWeather = cityWeather['sys']
    countryCode = sysWeather['country']
    restcountries_URL = 'https://restcountries.eu/rest/v2/alpha/' + countryCode
    countryInfo = load_json_by_URL(restcountries_URL)
    countryName = countryInfo['name']

    print('Current temperature in ', city, countryName, 'is', str(temperature),degree_sign)
