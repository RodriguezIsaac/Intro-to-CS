from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
TheOnlyWindow = tkinter.Tk()
TheOnlyWindow.title("World Population Calculator") #Title of the Window

TheOnlyWindow.geometry("500x100") #Size of the Window


#layout of the widgets inside the window
ylabel = Label(TheOnlyWindow, text = "Choose a Future Year") #Label
ylabel.grid(row = 0, column = 0)
ybox = Entry(TheOnlyWindow, bd = 5) #Future Year
ybox.grid(row = 1, column = 0)


#Function to handle what happens the user presses the button
def NewYear():

   #Retrieves the info from the user
   FutureYear = int(Entry.get(ybox))

   #Math crunching goes here
   t = (FutureYear - 2020)
   P = 7800000000
   e = 2.7182818284590452353602874713527
   rt = (0.0105 * t)

   F = round((P * e ** rt), 0)


   #Displaying results of calculations goes here

   PopulationLabel = Label(TheOnlyWindow, text = "The World Population of " + str(FutureYear) + " is " + str(F) + " people.")
   PopulationLabel.grid(row = 1, column = 4)



B = tkinter.Button(TheOnlyWindow, text ="Calculate World Population", command = NewYear)
B.grid(row  = 2, column = 0)


#Loop
TheOnlyWindow.mainloop()