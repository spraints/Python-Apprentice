"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()   
turtle.up()               # Create a turtle named tina
turtle.goto(1, 100)
turtle.down()

screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji2.png") # Set the background image of the screen

from math import sin, cos

turtle.speed(0)

i = 0
while True:
    i+=1
    turtle.left(abs(sin(i*19))*22)
    turtle.forward(10)

turtle.exitonclick()  