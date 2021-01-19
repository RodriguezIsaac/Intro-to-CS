from tkinter import *
import tkinter.messagebox

#Code for window layour goes here
TheOnlyWindow = tkinter.Tk()
TheOnlyWindow.title("Isaac's Program")

#Function to handle what happens the user presses the button
def TheyCallMe():
   #Math crnching goes here


   #Displaying results of calculations goes here
   tkinter.messagebox.showinfo( "Hello Mr.Berta", "They call me Isaac Rodriguez")

#layout of the widgets inside the window
hlabel = Label(TheOnlyWindow, text="Height") #Label
hlabel.pack(side=LEFT)
hbox = Entry(TheOnlyWindow, bd=5) #Height
hbox.pack(side=RIGHT)




B = tkinter.Button(TheOnlyWindow, text ="Push Me", command = TheyCallMe)
B.pack(side = RIGHT)

#Loop
TheOnlyWindow.mainloop()