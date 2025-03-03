"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

boing boing!! YOu canNOT run this program by clicking on ▶️ icon yarg matey🦜🏴‍☠️🗺️💰⛵⚓💀 the top of the editor
window. so DONT try it or i will find you muahahahahahahahahahahahahahahaha

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('triangle')                    # Set the shape of the turtle to a turtle
tina.speed(10)                           # Make the turtle move as fast, but not too fast.

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(130)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(130)                       # Continuie the last two steps three more times
tina.left(90)                           # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(130)
tina.left(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(130)
tina.left(90)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(5)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(5)                        # Move tina forward by 20
tina.write("this is my nono square >:(")         # Write the message "Why, hello there!"
tina.backward(10)                       # Move tina backward by 20

tina.goto(-50,0)
tina.pendown()
tina.color('green')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(100, steps=50)
tina.end_fill()

turtle.exitonclick()                    # Close the window when we click on it

# Now you can try writing your own programs. Open
# the next file 03_Turtle_Tricks.py

