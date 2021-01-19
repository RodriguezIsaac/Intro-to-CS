#https://pandascore.co/settings <--Keeps track of how many times the api has been called (1k Limit per hour)
import json
import urllib.request
import webbrowser #allows code to interact with user's browser when made to do so
import time #Time Module

try:
    print("Welcome to the League of Legends Champion API")
#Recieves User input & uses it to continue on with the process
    RandomChamp = int(input("Choose a number from 0 to 49,included,to get stats on a champion. (NOTE:DO NOT USE DECIMALS) "))

    LeagueOfLegends = "https://api.pandascore.co/lol/champions?token=zodSVE-n0SsTKle4zFbgxLTT5oV_o60megBXxLSxvAVrPYbsyyQ"
#Opens up specified url above
    requestURL = urllib.request.urlopen(LeagueOfLegends)
#Reads the information from the website and stores it as a variable
    data = requestURL.read()
#Encodes the data in UTF 8 format
    encoding = requestURL.info().get_content_charset('utf-8')
#Converts the data that is read to a json object
    statisticalstuff = json.loads(data.decode(encoding))

    print("\nWarning: A tab in your browser is going to open & display an image of the champion blindly chosen. Rest of the info will be in the console.\n")

    time.sleep(8)  #Delays rest of code from running for 8 seconds

#Accesses specified arrays to get information on a certain character based off User input

    Legend = statisticalstuff[RandomChamp]['name']
    print ("\nYou have chosen the champion",Legend,"\n")
#Opens up a tab in the User's browser displaying the character the User has blindly chosen
    Character = statisticalstuff[RandomChamp]['big_image_url']
    webbrowser.open(Character)
#Stats for the champion blindly selected by user
    AR = statisticalstuff[RandomChamp]['attackrange']
    print("Attack Range =",AR,"\n")

    MS = statisticalstuff[RandomChamp]['movespeed']
    print("Movement Speed=",MS,"\n")

    HP = statisticalstuff[RandomChamp]['hp']
    HPS = statisticalstuff[RandomChamp]['hpperlevel']
    print("Base Health=",HP)
    print("Health gained per level=",HPS,"\n")

    Mana = statisticalstuff[RandomChamp]['mp']
    MPS = statisticalstuff[RandomChamp]['mpperlevel']
    print("Base Mana=",Mana)
    print("Mana gained per level=",MPS,"\n")

    AD = statisticalstuff[RandomChamp]['attackdamage']
    ADS = statisticalstuff[RandomChamp]['attackdamageperlevel']
    print("Base Attack Damage =",AD)
    print("Attack Damage gained per level =",ADS,"\n")

    AMR = statisticalstuff[RandomChamp]['armor']
    AMRS = statisticalstuff[RandomChamp]['armorperlevel']
    print("Base Armor=",AMR)
    print("Armor gained per level=",AMRS,"\n")

    MR = statisticalstuff[RandomChamp]['spellblock']
    MRS = statisticalstuff[RandomChamp]['spellblockperlevel']
    print("Base Magic Resistance=",MR)
    print("Magic Resistance gained per level=",MRS)

except (IndexError,ValueError): #Error handling for User inputs above or below the range of numbers or non-integers
    print("You have chosen a number or non-integer not listed in the range of limitations stated.")