import json
import urllib.request #import libraries
import urllib.error #allows error handling for url

zipcode = input("Please provide a zipcode. ")

try:
#set url variable as openweathermap api query
    openweatherurl = "http://api.openweathermap.org/data/2.5/forecast?zip=" + (zipcode) + "&appid=451053e2fdab7d955c035836578f2804"
#opens the specifed url
    requestURL = urllib.request.urlopen(openweatherurl)
#read the information from the website and store as a variable
    data = requestURL.read()
#encodes the data in UTF 8 format
    encoding = requestURL.info().get_content_charset('utf-8')
#converts the data that is read to a json object
    allthestuff = json.loads(data.decode(encoding))


    def forecast():
        for f in range(0, 6):
            print("Day", f)
            city = allthestuff['city']['name']
            print("Your city is", city)

            weathercondition = allthestuff['list'][f]['weather'][0]['description']
            print("The weather condition is", weathercondition)

            kelvintemp = allthestuff['list'][f]['main']['temp']
            farhenheittemp = round(float((kelvintemp - 273.15) * 9/5 + 32), 2)
            print("The temperature is", farhenheittemp, "degrees Farhenheit")

            windspeed = allthestuff['list'][f]['wind']['speed']
            print("The windspeed is", windspeed, "mph\n")

    forecast()

except urllib.error.HTTPError:
    print("Invalid Zipcode for this Station.")