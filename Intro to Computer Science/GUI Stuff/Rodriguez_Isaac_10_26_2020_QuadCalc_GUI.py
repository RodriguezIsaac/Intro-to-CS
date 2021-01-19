from tkinter import *
import tkinter.messagebox


#Code for window layout goes here
FourWheelCalc = tkinter.Tk()
FourWheelCalc.title("Quadratic Calculator") #Title of the Window

FourWheelCalc.geometry("480x100+680+400") #Size of the Window


#layout of the widgets inside the window
alabel = Label(FourWheelCalc, text = "Choose a Value for A")
alabel.grid(row = 0, column = 0)
abox = Entry(FourWheelCalc, bd = 6)
abox.grid(row = 1, column = 0)

blabel = Label(FourWheelCalc, text = "Choose a Value for B")
blabel.grid(row = 0, column = 1)
bbox = Entry(FourWheelCalc, bd = 6)
bbox.grid(row = 1, column = 1)

clabel = Label(FourWheelCalc, text = "Choose a Value for C")
clabel.grid(row = 0, column = 2)
cbox = Entry(FourWheelCalc, bd = 6)
cbox.grid(row = 1, column = 2)


#Function to handle what happens the user presses the button
def QuadCalc():

   try:
    # Retrieves the info from the user
      a = float(Entry.get(abox))
      b = float(Entry.get(bbox))
      c = float(Entry.get(cbox))

   #Math crunching goes here
      y = ((b ** 2 - 4 * a * c) ** 0.5)
      x = (-b + y)
      z = (-b - y)

      f = round((x / (2 * a)), 2)
      g = round((z / (2 * a)), 2)
   except ValueError:
        YouFool = tkinter.Tk()
        YouFool.title("YOU FOOL")
        YouFool.geometry("375x100+732+400")
        YFlabel = Label(YouFool,text="You Have Entered a LETTER instead of a NUMBER\n\n OR\n\n You just didn't put anything into the box(es) :/", font = ("Times New Roman", 12, "bold"))
        YFlabel.grid(row=1, column=1)

   except TypeError:  # Handling TypeError for Imaginary Answers
       # Displaying results of calculations goes here
       ImaginaryAnswer = Label(FourWheelCalc, text = "Answer is Imaginary\nCan't Display", font = ("Times New Roman", 12, "bold"))
       ImaginaryAnswer.grid(row = 3, column = 1)

   except ZeroDivisionError:
       No = Label(FourWheelCalc, text = "No Solution\n Division by Zero", font = ("Times New Roman", 12, "bold"))
       No.grid(row = 3, column = 1)

   else:  # Allowing Real Answers to go through
       TwoWheelAnswer = Label(FourWheelCalc,text="Answers:\n" + str(f) + " & " + str(g), font = ("Times New Roman", 12, "bold"))
       TwoWheelAnswer.grid(row = 3, column = 1)


B = tkinter.Button(FourWheelCalc, text ="Calculate", command = QuadCalc)
B.grid(row  = 1, column = 3)


#Loop
FourWheelCalc.mainloop()