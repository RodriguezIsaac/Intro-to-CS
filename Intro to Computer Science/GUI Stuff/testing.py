import json
import urllib.request  # import libraries
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# Code for window layout goes here
AstronomyPic = tkinter.Tk()
AstronomyPic.title("AstronomyPic Displayer")  # Title of the Window
AstronomyPic.geometry("950x1000+375+5")


# layout of the widgets inside the window
ClickLabel = Label(AstronomyPic, text="Please enter a Date in YY-MM-DD Format\nExample: 2020-02-05\nDATE MUST BE PRESENT OR PAST",font=("Times New Roman", 12, "bold"))
ClickLabel.grid(row=0, column=0)

GimmeDate = Entry(AstronomyPic, bd=5)
GimmeDate.grid(row=1, column=0)


def Astronomy():

    DateGiven = (Entry.get((GimmeDate)))
    # set url variable as nasa apod api query
    APOD = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + str(DateGiven) + "&camera=navcam&api_key=aWkPs6DoBPPJ2pp79tf7UZt7uZiTFWW3g66ptsjU"
    # opens the specifed url
    GimmeInfo = urllib.request.urlopen(APOD)
    # read the information from the website and store as a variable
    PicData = GimmeInfo.read()
    # converts the data that is read to a json object
    AlltheInfo = json.loads(PicData)

    SpacePic = AlltheInfo['photos'][0]['img_src']


    Display = urllib.request.urlopen(SpacePic)

    Display1 = ImageTk.PhotoImage(Image.open(Display))

    Pic = Label(AstronomyPic, image = Display1)
    Pic.image = Display1
    Pic.grid(row = 4, column = 0)


Space = tkinter.Button(AstronomyPic, text = "Show Pic", command = Astronomy)
Space.grid(row = 2, column = 0)


AstronomyPic.mainloop()