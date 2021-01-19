#IT WORKEDDDDD:)
import json
import urllib.request #import libraries
import urllib.error #allows error gandling for url
from tkinter import *
import tkinter.messagebox


#Code for window layour goes here
Chalupa = tkinter.Tk()
Chalupa.title("Walmart Item Lookup")

#layout of the widgets inside the window
Zlabel = Label(Chalupa, text="What Is The Item ID:") #Label
Zlabel.grid(row = 1, column = 1)
Zbox = Entry(Chalupa, bd=5)
Zbox.grid(row=1, column=2)



def wall():
    itemid = (Entry.get(Zbox))
    try:
#set url variable as openweathermap api query
        Walmarturl =  "http://api.walmartlabs.com/v1/items/" + str(itemid) + "?format=json&apiKey=f6cb7cqjzekh894ec7gaunus"
#opens the specifed url
        requestURL = urllib.request.urlopen(Walmarturl)
#read the information from the website and store as a variable
        data = requestURL.read()
#encodes the data in UTF 8 format
        encoding =requestURL.info().get_content_charset('utf-8')
#converts the data that is read to a json object
        allthestuff = json.loads(data.decode(encoding))

        name = allthestuff['name']

        saleprice = allthestuff["salePrice"]

        productid = allthestuff["itemId"] # Numbers do not get '

        upc = allthestuff["upc"]

        MSRP = allthestuff["msrp"]

        itemname = Label(Chalupa, text="The Item is: " + str(name))
        itemname.grid(row=3, column=2)
        price = Label(Chalupa, text="The Sale price is: " + str(saleprice) + " in Dollars")
        price.grid(row=4, column=2)
        ID = Label(Chalupa, text="The Product Id is: " + str(productid))
        ID.grid(row=5, column=2)
        upcthingy= Label(Chalupa, text="The UPC is: " + str(upc))
        upcthingy.grid(row=6, column=2)
        msrpthing = Label(Chalupa, text="The MSRP is: " + str(MSRP))
        msrpthing.grid(row=7, column=2)

    except (urllib.error.HTTPError, ValueError, NameError):
         print ("Why are you even typing this in?")

B = tkinter.Button(Chalupa, text ="Find your Item:", command = wall)
B.grid(row = 2, column = 2)

#Loop
Chalupa.mainloop()