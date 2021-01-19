from tkinter import *
import tkinter.messagebox

#Code for window layour goes here
Taco = tkinter.Tk()
Taco.title("Temperature Converter")


#Function to handle what happens the user presses the button
def Fahren():

    Degrees = float(Entry.get(hbox))


   #Math crnching goes here
    F = round(float(((Degrees - 32) * 5 / 9)), 2)  # Farenheit to Celsius
    FK = round(float(Degrees - 32) * 5/9 + 273.15)  # Fahrenheit to kelvin


    wbox.delete(0, "end")
    fbox.delete(0, "end")
    wbox.insert(0, FK)
    fbox.insert(0, F)


def Cel():

    Degrees = float(Entry.get(fbox))


    C = round(float((Degrees * 9 / 5) + 32), 2)  # Celcius to Farenheit
    CK = round(float(Degrees + 273.15), 2)  # Celcius to Kelvin

    wbox.delete(0, "end")
    hbox.delete(0, "end")
    wbox.insert(0, CK)
    hbox.insert(0, C)


def Kel():

    Degrees = float(Entry.get(wbox))

    K = round(float(Degrees - 273.15), 2)  # kelvin to Celsius
    KF = round(float((Degrees - 273.15) * 9 / 5 + 32), 2)  # Kelvin to Farenheit

    fbox.delete(0, "end")
    hbox.delete(0, "end")
    fbox.insert(0, K)
    hbox.insert(0, KF)


  # Displaying results of calculations goes here


#layout of the widgets inside the window
hlabel = Label(Taco, text="Temperature in Celsius:") #Fahrenheit
hlabel.grid(row = 0, column = 0)
hbox = Entry(Taco, bd=5, validate = "focusout", validatecommand = Fahren)
hbox.grid(row=0, column=1)

wlabel = Label(Taco, text="Temperature in Kelvin:") #Kelvin
wlabel.grid(row=1, column=0)
wbox = Entry (Taco, bd=5, validate = "focusout", validatecommand = Kel)
wbox.grid(row=1, column=1)

flabel = Label(Taco, text="Temperature in Fahrenheit:") #Celsius
flabel.grid(row=2, column=0)
fbox = Entry(Taco, bd=5, validate = "focusout", validatecommand = Cel)
fbox.grid(row=2,column=1)


#Loop
Taco.mainloop()