import json
import urllib.request #import libraries
import urllib.error #allows error handling for url
from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
WeatherMan = tkinter.Tk()
WeatherMan.title("Your Current Weather Conditions") #Title of the Window

WeatherMan.geometry("530x150+680+400") #Size of the Window


#layout of the widgets inside the window
wlabel = Label(WeatherMan, text = "Provide Your Zipcode") #Label
wlabel.grid(row = 0, column = 0)
wbox = Entry(WeatherMan, bd = 5)
wbox.grid(row = 1, column = 0)


#Function to handle what happens the user presses the button
def ManWeather():

   #Retrieves the info from the user
   Zipcode = (Entry.get(wbox))

   try:
       # set url variable as openweathermap api query
       openweatherurl = "http://api.openweathermap.org/data/2.5/weather?zip=" + str(Zipcode) + "&appid=451053e2fdab7d955c035836578f2804"
       # opens the specifed url
       requestURL = urllib.request.urlopen(openweatherurl)
       # read the information from the website and store as a variable
       data = requestURL.read()
       # encodes the data in UTF 8 format
       encoding = requestURL.info().get_content_charset('utf-8')
       # converts the data that is read to a json object
       allthestuff = json.loads(data.decode(encoding))

       city = allthestuff['name']

       weathercondition = allthestuff['weather'][0]['description']

       kelvintemp = allthestuff['main']['temp']
       farhenheittemp = round(float(((kelvintemp - 273.15) * 9 / 5 + 32)), 2)

       windspeed = allthestuff['wind']['speed']

       # Displaying results of calculations goes here
       Witherlabel = Label(WeatherMan, text = "The City is " + str(city) + "\nTemperature is currently " + str(farhenheittemp) + " Degrees Fahrenheit" + "\nCurrent Windspeed is " + str(windspeed) + " mph" + "\nCurrent Weather Conditions is " + str(weathercondition), font = ("Times New Roman", 12, "bold"))
       Witherlabel.grid(row = 1, column = 1)
   except urllib.error.HTTPError:
       TryAgain = tkinter.Tk()
       TryAgain.title("YOU FOOL")
       TryAgain.geometry("335x100+715+400")
       TAlabel = Label(TryAgain, text="The Zipcode entered is Invalid for this Station")
       TAlabel.grid(row=1, column=1)



B = tkinter.Button(WeatherMan, text ="Find Weather Conditions", command = ManWeather)
B.grid(row  = 2, column = 0)


#Loop
WeatherMan.mainloop()