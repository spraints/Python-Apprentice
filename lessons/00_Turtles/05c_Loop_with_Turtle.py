
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here

"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

for i in range(5):
  tina.forward(150)                       # Move tina forward by the forward distance
  tina.left(360/5)                           # Turn tina left by the left turn



turtle.exitonclick()                    # Close the window when we click on it
