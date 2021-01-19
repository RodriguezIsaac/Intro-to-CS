import json
import urllib.request #import libraries
import urllib.error #allows error handling for url
from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
ForeCastMan = tkinter.Tk()
ForeCastMan.title("Weather Forecast") #Title of the Window
ForeCastMan.geometry("850x500+565+280") #Size of the Window
ForeCastMan.configure(bg = "gainsboro")


#layout of the widgets inside the window
wlabel = Label(ForeCastMan, text = "Provide Your Zipcode") #Label
wlabel.grid(row = 0, column = 0)
wbox = Entry(ForeCastMan, bd = 5)
wbox.grid(row = 1, column = 0)
wlabel.configure(bg = "gainsboro")


#Function to handle what happens the user presses the button
def forecast():
    try:
        for f in range(0, 5):
            # Retrieves the info from the user
            Zipcode = (Entry.get(wbox))

            # set url variable as openweathermap api query
            openweatherurl = "http://api.openweathermap.org/data/2.5/forecast?zip=" + (Zipcode) + "&appid=451053e2fdab7d955c035836578f2804"
            # opens the specifed url
            requestURL = urllib.request.urlopen(openweatherurl)
            # read the information from the website and store as a variable
            data = requestURL.read()
            # encodes the data in UTF 8 format
            encoding = requestURL.info().get_content_charset('utf-8')
            # converts the data that is read to a json object
            mystuff = json.loads(data.decode(encoding))


            city = mystuff['city']['name']

            weathercondition = mystuff['list'][f]['weather'][0]['description']

            kelvintemp = mystuff['list'][f]['main']['temp']
            farhenheittemp = round(float((kelvintemp - 273.15) * 9 / 5 + 32), 2)

            windspeed = mystuff['list'][f]['wind']['speed']

            # Displaying results of calculations goes here
            Daylabel = Label(ForeCastMan, text = "           Hour " + str((f + 1) * 3) + "           ", font = ("Times New Roman", 12, "bold"))
            Daylabel.grid(row = 3, column = f + 1)
            Daylabel.configure(bg="gainsboro")

            Citylabel = Label(ForeCastMan, text = "\n\nCity:\n\n", font = ("Times New Roman", 12, "bold"))
            Citylabel.grid(row = 4, column = 0)
            Citylabel.configure(bg="gainsboro")

            Templabel = Label(ForeCastMan, text="\n\nTemperature (F):\n\n", font = ("Times New Roman", 12, "bold"))
            Templabel.grid(row = 5, column = 0)
            Templabel.configure(bg="gainsboro")

            Windlabel = Label(ForeCastMan, text="\n\nWindspeed (mph):\n\n", font = ("Times New Roman", 12, "bold"))
            Windlabel.grid(row = 6, column = 0)
            Windlabel.configure(bg="gainsboro")

            Conditionlabel = Label(ForeCastMan, text="\n\nWeather Conditions:\n\n", font = ("Times New Roman", 12, "bold"))
            Conditionlabel.grid(row = 7, column = 0)
            Conditionlabel.configure(bg="gainsboro")

            City = Label(ForeCastMan, text = city, font = ("Times New Roman", 12, "bold"))
            City.grid(row = 4, column = f + 1)
            City.configure(bg="gainsboro")

            Temp = Label(ForeCastMan, text = farhenheittemp, font = ("Times New Roman", 12, "bold"))
            Temp.grid(row = 5, column = f + 1)
            Temp.configure(bg="gainsboro")

            Wind = Label(ForeCastMan, text = windspeed, font = ("Times New Roman", 12, "bold"))
            Wind.grid(row = 6, column = f + 1)
            Wind.configure(bg="gainsboro")

            Condition = Label(ForeCastMan, text = weathercondition, font = ("Times New Roman", 12, "bold"))
            Condition.grid(row = 7, column = f + 1)
            Condition.configure(bg="gainsboro")

    except urllib.error.HTTPError:
        TryAgain = tkinter.Tk()
        TryAgain.title("UNLUCKY")
        TryAgain.geometry("300x75+775+400")
        TAlabel = Label(TryAgain, text="THE ZIPCODE ENTERED IS INVALID FOR THIS STATION\n\nPLEASE TRY ANOTHER ZIPCODE")
        TAlabel.grid(row=1, column=1)


B = tkinter.Button(ForeCastMan, text ="Find Weather Conditions", command = forecast)
B.grid(row  = 2, column = 0)
B.configure(bg = "gainsboro")


#Loop
ForeCastMan.mainloop()