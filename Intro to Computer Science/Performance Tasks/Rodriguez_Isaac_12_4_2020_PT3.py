import json
import urllib.request
import urllib.error
from tkinter import *
import tkinter.messagebox

Walmart = tkinter.Tk()
Walmart.title("Walmart Item Lookup")
Walmart.geometry("+450+300")
Walmart.configure(bg = "gainsboro")


Gimme = Label(Walmart, text = "Provide a Product ID", font = ("Times New Roman", 12, "bold"))
Gimme.grid(row = 0, column = 0)
Gimme.configure(bg = "gainsboro")
ID_Entry = Entry(Walmart, bd = 5)
ID_Entry.grid(row = 1, column = 0)

Name_Label = Label(Walmart)

def Product():
    ID = Entry.get(ID_Entry)

    try:

        #set url variable as openweathermap api query
        Inventory = f"http://api.walmartlabs.com/v1/items/{ID}?format=json&apiKey=f6cb7cqjzekh894ec7gaunus"
        #opens the specifed url
        requestURL = urllib.request.urlopen(Inventory)
        #read the information from the website and store as a variable
        data = requestURL.read()
        #encodes the data in UTF 8 format
        encoding = requestURL.info().get_content_charset('utf-8')
        #converts the data that is read to a json object
        MyStore = json.loads(data.decode(encoding))

        global Name_Label
        Name_Label.destroy()


        Name = MyStore["name"]
        Name_Label = Label(Walmart, text = f"\nProduct: {Name}", font = ("Times New Roman", 12, "bold"))
        Name_Label.grid(row = 3, column = 0)
        Name_Label.configure(bg="gainsboro")

        Item_ID = MyStore["itemId"]
        Item_ID_Label = Label(Walmart, text = f"\nItem ID: {Item_ID}", font = ("Times New Roman", 12, "bold"))
        Item_ID_Label.grid(row = 4, column = 0)
        Item_ID_Label.configure(bg="gainsboro")

        UPC = MyStore["upc"]
        UPC_Label = Label(Walmart, text = f"UPC: {UPC}", font = ("Times New Roman", 12, "bold"))
        UPC_Label.grid(row = 5, column = 0)
        UPC_Label.configure(bg="gainsboro")

        Price = MyStore["salePrice"]
        Price_Label = Label(Walmart, text=f"\nSale Price: ${Price}", font=("Times New Roman", 12, "bold"))
        Price_Label.grid(row = 6, column=0)
        Price_Label.configure(bg="gainsboro")

        MSRP = MyStore["msrp"]
        MSRP_Label = Label(Walmart, text = f"MSRP: ${MSRP}", font = ("Times New Roman", 12, "bold"))
        MSRP_Label.grid(row = 7, column = 0)
        MSRP_Label.configure(bg="gainsboro")
    except KeyError:
        Not_Found = Label(Walmart, text = "\nNO MSRP AND/OR SALE PRICE FOUND", font = ("Times New Roman", 12, "bold"))
        Not_Found.grid(column = 0)
        Not_Found.configure(bg = "gainsboro")
    except urllib.error.HTTPError:
        TryAgain = tkinter.Tk()
        TryAgain.title("Mistakes Happen")
        TryAgain.geometry("375x75+775+400")
        TAlabel = Label(TryAgain, text="ID PROVIDED IS INVALID/NO ID WAS ENTERED\n\nPLEASE TRY AGAIN", font = ("Times New Roman", 12, "bold"))
        TAlabel.grid(row=1, column=1)


Search = tkinter.Button(Walmart, text = "Search", font = ("Times New Roman", 10, "bold"), command = Product)
Search.grid(row = 2, column = 0)


Walmart.mainloop()