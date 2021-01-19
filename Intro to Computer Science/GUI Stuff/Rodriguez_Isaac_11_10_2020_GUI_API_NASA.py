import json
import urllib.request  # import libraries
import urllib.error
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# Code for window layout goes here
AstronomyPic = tkinter.Tk()
AstronomyPic.title("AstronomyPic Displayer")  # Title of the Window
AstronomyPic.geometry("950x1000+375+5")

Pic = Label(AstronomyPic)

# layout of the widgets inside the window
FormatLabel = Label(AstronomyPic, text = "Please enter a Date in YY-MM-DD Format\nExample: 2020-02-05\nDATE MUST BE PRESENT OR PAST",font = ("Times New Roman", 12, "bold"))
FormatLabel.grid(row = 0, column = 0)

GimmeDate = Entry(AstronomyPic, bd = 5)
GimmeDate.grid(row = 1, column = 0)


def Astronomy():

    try:
        DateGiven = (Entry.get((GimmeDate)))
        # set url variable as nasa apod api query
        APOD = "https://api.nasa.gov/planetary/apod?date=" + str(DateGiven) + "&api_key=7q7JNX1R0O6Z6B2RwqwX898Cgh8IKKhAbKkwU2VL"
        # opens the specifed url
        GimmeInfo = urllib.request.urlopen(APOD)
        # read the information from the website and store as a variable
        PicData = GimmeInfo.read()
        # converts the data that is read to a json object
        AlltheInfo = json.loads(PicData)

        SpacePic = AlltheInfo['url']

        global Pic
        Pic.destroy() #Deletes the previous Pic before showing the next requested one

        Display = urllib.request.urlopen(SpacePic)

        Display1 = ImageTk.PhotoImage(Image.open(Display))

        Pic = Label(AstronomyPic, image = Display1)
        Pic.image = Display1
        Pic.grid(row = 4, column = 0)

    except urllib.error.HTTPError:
        TryAgain = tkinter.Tk()
        TryAgain.title("MISTAKES HAVE BEEN MADE")
        TryAgain.geometry("350x75+775+400")
        TAlabel = Label(TryAgain, text = "THE FORMAT FOR THE DATE WAS ENTERED INCORRECTLY\n\nPLEASE CHECK THE FORMAT & TRY AGAIN")
        TAlabel.grid(row=1, column=1)


Space = tkinter.Button(AstronomyPic, text = "Show Pic", command = Astronomy)
Space.grid(row = 2, column = 0)


AstronomyPic.mainloop()