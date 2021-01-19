from tkinter import *
import tkinter.messagebox

MyWindow = tkinter.Tk()

def button():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(MyWindow, text ="Push Me", command = button)

B.pack()
MyWindow.mainloop()