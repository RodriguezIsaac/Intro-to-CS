import json
import urllib.request #import libraries
import urllib.error #allows error handling for url

zipcode = input("Please provide a zipcode. ")

try:
#set url variable as openweathermap api query
    openweatherurl = "http://api.openweathermap.org/data/2.5/weather?zip=" + (zipcode) + "&appid=451053e2fdab7d955c035836578f2804"
#opens the specifed url
    requestURL = urllib.request.urlopen(openweatherurl)
#read the information from the website and store as a variable
    data = requestURL.read()
#encodes the data in UTF 8 format
    encoding =requestURL.info().get_content_charset('utf-8')
#converts the data that is read to a json object
    allthestuff = json.loads(data.decode(encoding))


    city = allthestuff['name']
    print("Your city is", city)

    weathercondition = allthestuff['weather'][0]['main']
    print("The weather condition is", weathercondition)

    kelvintemp = allthestuff['main']['temp']
    farhenheittemp = round(float(((kelvintemp - 273.15) * 9/5 + 32)), 2)
    print("The current temperature is", farhenheittemp, "degrees Farhenheit")

    windspeed = allthestuff['wind']['speed']
    print("The current windspeed is", windspeed, "mph")
except urllib.error.HTTPError:
    print("Invalid Zipcode for this Station.")