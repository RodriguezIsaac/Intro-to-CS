from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
TheOnlyWindow = tkinter.Tk()
TheOnlyWindow.title("Temperature Converter") #Title of the Window

TheOnlyWindow.geometry("400x100+680+400") #Size of the Window

#Function to handle what happens when fbox loses focus
def Fahrenheit():
    try:

    #Retrieves the info from the user
        Degrees = float(Entry.get(fbox))

    # Math crunching
        F = round(float((Degrees - 32) * 5 / 9), 2)  # Formula for Fahrenheit to Celsius
        f = round(float((Degrees - 32) * 5 / 9 + 273.15), 2)  # Formula for Fahrenheit to Kelvin

    # Displaying results of calculations
        cbox.delete(0, "end")
        kbox.delete(0, "end")
        cbox.insert(0, F)
        kbox.insert(0, f)
    except ValueError:
        YouFool = tkinter.Tk()
        YouFool.title("YOU FOOL")
        YouFool.geometry("335x100+715+400")
        YFlabel = Label(YouFool, text="You Have Entered a LETTER instead of a NUMBER\n\n OR\n\n You just didnt put anything into the box you first selected :/")
        YFlabel.grid(row=1, column=1)
        fbox.delete(0, "end")
        fbox.insert(0, 0)
        cbox.insert(0, 0)
        kbox.insert(0, 0)

    return True


#Function to handle what happens when cbox loses focus
def Celsius():
    try:

        #Retrieves the info from the user
        Degrees1 = float(Entry.get(cbox))

        # Math crunching
        C = round(float((Degrees1 * 9 / 5) + 32), 2)  # Formula for Celsius to Fahrenheit
        c = round(float((Degrees1 + 273.15)), 2)  # Formula for Celsius to Kelvin

        # Displaying results of calculations
        fbox.delete(0, "end")
        kbox.delete(0, "end")
        fbox.insert(0, C)
        kbox.insert(0, c)
    except ValueError:
        YouFool = tkinter.Tk()
        YouFool.title("YOU FOOL")
        YouFool.geometry("335x100+715+400")
        YFlabel = Label(YouFool, text="You Have Entered a LETTER instead of a NUMBER\n\n OR\n\n You just didnt put anything into the box you first selected :/")
        YFlabel.grid(row=1, column=1)
        cbox.delete(0, "end")
        cbox.insert(0, 0)
        kbox.insert(0, 0)
        fbox.insert(0, 0)

    return True


#Function to handle what happens when kbox loses focus
def Kelvin():
    try:

        #Retrieves the info from the user
        Degrees2 = float(Entry.get(kbox))

        # Math crunching
        K = round(float((Degrees2 - 273.15) * 9 / 5 + 32), 2)  # Formula for Kelvin to Fahrenheit
        k = round(float((Degrees2 - 273.15)), 2)  # Formula for Kelvin to Celsius

        # Displaying results of calculations
        fbox.delete(0, "end")
        cbox.delete(0, "end")
        fbox.insert(0, K)
        cbox.insert(0, k)
    except ValueError:
        YouFool = tkinter.Tk()
        YouFool.title("YOU FOOL")
        YouFool.geometry("335x100+715+400")
        YFlabel = Label(YouFool, text="You Have Entered a LETTER instead of a NUMBER\n\n OR\n\n You just didnt put anything into the box you first selected :/")
        YFlabel.grid(row = 1, column = 1)
        kbox.delete(0, "end")
        kbox.insert(0, 0)
        cbox.insert(0, 0)
        fbox.insert(0, 0)

    return True


#layout of the widgets inside the window
flabel = Label(TheOnlyWindow, text = "Degrees Fahrenheit")
flabel.grid(row = 0, column = 0)
fbox = Entry(TheOnlyWindow, bd = 5, validate = "focusout", validatecommand = Fahrenheit)
fbox.grid(row = 1, column = 0)


clabel = Label(TheOnlyWindow, text = "Degrees Celsius")
clabel.grid(row = 0, column = 1)
cbox = Entry(TheOnlyWindow, bd = 5, validate = "focusout", validatecommand = Celsius)
cbox.grid(row = 1, column = 1)


klabel = Label(TheOnlyWindow, text = "Degrees Kelvin")
klabel.grid(row = 0, column = 2)
kbox = Entry(TheOnlyWindow, bd= 5, validate = "focusout", validatecommand = Kelvin)
kbox.grid(row = 1, column = 2)


#Loop
TheOnlyWindow.mainloop()