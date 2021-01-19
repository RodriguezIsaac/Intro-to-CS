from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
TheOnlyWindow = tkinter.Tk()
TheOnlyWindow.title("BMI Calculator") #Title of the Window

TheOnlyWindow.geometry("500x100") #Size of the Window


#layout of the widgets inside the window
hlabel = Label(TheOnlyWindow, text = "Height (in)") #Label
hlabel.grid(row = 0, column = 0)
hbox = Entry(TheOnlyWindow, bd = 5) #Height
hbox.grid(row = 0, column = 1)

wlabel = Label(TheOnlyWindow, text = "Weight (lbs)")
wlabel.grid(row = 1, column = 0)
wbox = Entry(TheOnlyWindow, bd = 5) #Weight
wbox.grid(row = 1, column = 1)


#Function to handle what happens the user presses the button
def TheyCallMe():

   #Retrieves the info from the user
   weight = float(Entry.get(wbox))
   height = float(Entry.get(hbox))

   #Math crunching goes here
   BMI = (703 * weight / height ** 2)
   BMI = round(BMI, 2)


   #Displaying results of calculations goes here


   if BMI <= 18.5:
      BMIlabel = Label(TheOnlyWindow, text=("Your BMI is " + str(BMI) + ". You're Underweight"))
      BMIlabel.grid(row=1, column=4)
   elif BMI > 18.5 and BMI < 25:
      BMIlabel = Label(TheOnlyWindow, text=("Your BMI is " + str(BMI) + ". You're Normal Weight"))
      BMIlabel.grid(row=1, column=4)
   elif BMI > 25 and BMI < 30:
      BMIlabel = Label(TheOnlyWindow, text=("Your BMI is " + str(BMI) + ". You're Overweight"))
      BMIlabel.grid(row=1, column=4)
   elif BMI > 30:
      BMIlabel = Label(TheOnlyWindow, text=("Your BMI is " + str(BMI) + ". You're Obese"))
      BMIlabel.grid(row=1, column=4)


B = tkinter.Button(TheOnlyWindow, text ="Calculate BMI", command = TheyCallMe)
B.grid(row  = 2, column = 1)


#Loop
TheOnlyWindow.mainloop()