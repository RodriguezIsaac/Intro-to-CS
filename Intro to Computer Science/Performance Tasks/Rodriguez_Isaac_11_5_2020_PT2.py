####################################PERFORMANCE TASK #2
#utilize openweathermap current conditions api for this asssingment   (10 points for correct setup)
#Create an interactive API application that prompts the user for their zip code and then retrieves the following information:
#city (2 points)
#pressure (2 points)
#humidity (2 points)
#visibility (2 points)
#Display the information in a turtle drawing (5 points)
#draw a weather scene using turtle (be creative) that meets the following requirements:
#at least 5 colors (5 points)
#at least one use of turtle goto (1 point)
#at least one use of pen up (1 point)
#commented code throughout the project (10 points)
######################################## 40 points total

import json
import urllib.request #import url libraries
import urllib.error #allows error handling for url related code
import turtle as t

#Asks for User Input
zipcode = input("Please provide a zipcode. ")

try:
    #Sets the URL to the Variable openweatherurl
    openweatherurl = "http://api.openweathermap.org/data/2.5/weather?zip=" + (zipcode) + "&appid=451053e2fdab7d955c035836578f2804"
    #Opens the Specifed URL
    requestURL = urllib.request.urlopen(openweatherurl)
    #Reads the Information from the Website and Stores it as a Variable
    data = requestURL.read()
    #Encodes the Data in UTF 8 Format
    encoding =requestURL.info().get_content_charset('utf-8')
    #Converts the Data that is read to a json Object
    ThisStuff = json.loads(data.decode(encoding))

    #Variables Representing the Specified Info pulled from the Arrays
    city = ThisStuff['name']

    pressure = ThisStuff['main']['pressure']

    humidity = ThisStuff['main']['humidity']

    visibility = ThisStuff['visibility']

    t.speed("fastest")#Increase the Speed at which the Turtle Draws
    #t.tracer(n = 0) #Turns off the animation for the turtle & just instantly displays the completed canvas

    #Function for Drawing the Sky
    def Sky():
        t.penup()
        t.goto(-500, 0) #Position the Turtle starts at
        t.pencolor("white")
        t.fillcolor("light blue")
        t.pendown()
        t.begin_fill()
        for s in range(4): #Loops the Turns to Enclose the Rectangle used as the Sky
            t.fd(1500)
            t.lt(90) #The Angle at which the Turtle Turns
            t.fd(1500) #The Distance at which the Turtle moves Forward
        t.end_fill()

    #Function for Drawing the Ground
    def Ground():
        t.penup()
        t.goto(-500, 0)
        t.pencolor("white")
        t.fillcolor("light green")
        t.pendown()
        t.begin_fill()
        for g in range(4): #Loops the Turns to Enclose the Rectangle used as the Ground
            t.fd(1500)
            t.rt(90) #The Angle at which the Turtle Turns
            t.fd(1500)
        t.end_fill()

    Sky()#Activating the Sky Function
    Ground()#Activating the Ground Function


    t.penup() #Takes the Turtle Pen off the Window to prevent leaving behind a mark when switching position
    t.pencolor("black") #Uses the color provided when drawing/writing the next piece

    #Displaying the Info from the Arrays in the Turtle Window
    t.setpos(-95, 135)
    t.write(('City: ' + str(city)), font=("Times New Roman", 17, "bold"))

    t.setpos(-95, 90)
    t.write(('Air Pressure: ' + str(pressure)), font=("Times New Roman", 17, "bold"))

    t.setpos(-95, 45)
    t.write(('Humidity: ' + str(humidity)), font=("Times New Roman", 17, "bold"))

    t.setpos(-95, 0)
    t.write(('Visibility: ' + str(visibility)), font=("Times New Roman", 17, "bold"))


    t. penup()

    #Drawing the Circle for the Sun
    t.goto(400, 250)
    t.pencolor("yellow")
    t.fillcolor("yellow")#Fills the shape made with the specified color given
    t.pendown()
    t.begin_fill() #Begins to fill in the area provided
    t.circle(100) #Diameter of the Circle/ The Size of the Circle
    t.end_fill() #Stops filling in the area provided

    #Function for Drawing the Beams of "Light" from the Sun
    def SunBeams(t, length, radius):
        for b in range(20): #Loops the Action for Drawing the Beams 20 Times
            t.penup()
            t.forward(radius) #Uses the radius stated to have a imaginary circle at which the beams will surround
            t.pendown()
            t.forward(length) #Uses the length stated to determine the length of the beams
            t.penup()
            t.backward(length + radius) #Tells the Turtle to go backward the distance of the length & radius stated
            t.left(11.25)


    #Utilizes the Function SunBeams, to Draw the Beams of "Light"
    t.penup()
    t.goto(400, 350) #Positioning the Beams to go around the sun
    t.pencolor("orange")
    t.pensize(5) #The size of the mark made by the turtle
    t.pendown()
    SunBeams(t, 85, 110) #Sets the length & radius for the specified function
    t.right(45)
    SunBeams(t, 85, 110)
    t.left(45)

    #Function used for Drawing the Wind
    def Wind():
        t.pencolor("white")
        t.pensize(5)
        t.pendown()
        t.rt(90)
        t.fd(115)
        #Manipulation of Circles to make the Turtle draw a bit of a Spiral
        t.circle(30, 270) #Radius, Length/Distance
        t.circle(20, 125)
        t.circle(20, 85)
        t.circle(10, 175)
        t.circle(5, 100)


    t.penup()
    t.goto(-450, 135)
    Wind()

    t.penup()
    t.goto(-250, 280)
    t.lt(55)
    Wind()

    t.penup()
    t.goto(0, 240)
    t.lt(55)
    Wind()

    #Allows the Turtle Window to Open & Draw Everything Above
    t.done()

#Error Handling for if the User Provides a Zipcode that doesn't work
except urllib.error.HTTPError:
    print("Invalid Zipcode for this Station.")