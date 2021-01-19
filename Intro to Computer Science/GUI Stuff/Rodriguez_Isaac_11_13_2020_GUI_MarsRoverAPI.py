import json
import urllib.request  # import libraries
import urllib.error
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# Code for window layout goes here
MarsRoverPic = tkinter.Tk()
MarsRoverPic.title("MarsRoverPic Displayer")  # Title of the Window
MarsRoverPic.geometry("950x1000+375+5")

Pic = Label(MarsRoverPic)

# layout of the widgets inside the window
FormatLabel = Label(MarsRoverPic, text = "Please enter a Date in YY-MM-DD Format\nExample: 2020-02-05\nDATE MUST BE PRESENT OR PAST",font = ("Times New Roman", 12, "bold"))
FormatLabel.grid(row = 0, column = 0)

GimmeDate = Entry(MarsRoverPic, bd = 5)
GimmeDate.grid(row = 1, column = 0)


def MarsRover():

    try:
        DateGiven = (Entry.get((GimmeDate)))
        # set url variable as nasa Rover api query
        Rover = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + str(DateGiven) + "&camera=navcam&api_key=7q7JNX1R0O6Z6B2RwqwX898Cgh8IKKhAbKkwU2VL"
        # opens the specifed url
        GimmeInfo = urllib.request.urlopen(Rover)
        # read the information from the website and store as a variable
        RoverData = GimmeInfo.read()
        # converts the data that is read to a json object
        RoverInfo = json.loads(RoverData)

        MarsPic = RoverInfo['photos'][0]['img_src']

        global Pic
        Pic.destroy() #Deletes the previous Pic before showing the next requested one

        Display = urllib.request.urlopen(MarsPic)

        Display1 = ImageTk.PhotoImage(Image.open(Display))


        Pic = Label(MarsRoverPic, image = Display1)
        Pic.image = Display1
        Pic.grid(row = 4, column = 0)

    except urllib.error.HTTPError:
        TryAgain = tkinter.Tk()
        TryAgain.title("MISTAKES HAVE BEEN MADE")
        TryAgain.geometry("350x75+775+400")
        TAlabel = Label(TryAgain, text = "THE FORMAT FOR THE DATE WAS ENTERED INCORRECTLY\n\nPLEASE CHECK THE FORMAT & TRY AGAIN")
        TAlabel.grid(row=1, column=1)


Space = tkinter.Button(MarsRoverPic, text = "Show Pic", command = MarsRover)
Space.grid(row = 2, column = 0)




MarsRoverPic.mainloop()