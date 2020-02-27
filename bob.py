# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:54:03 2020

@author: Tom Hudson
"""

import turtle
import random # for randomly placing food

food_eaten = 0 # Food gotten score

# Screen for the game
wn = turtle.Screen()
wn.title("Pet Turtle by @thudsonbu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Bob (the turtle)
bob = turtle.Turtle()
bob.speed(0) # speed of animation (max speed = 0)
bob.shape("turtle")
bob.color("green")
bob.shapesize(stretch_wid=1, stretch_len=1)
bob.penup() # does not draw a line
bob.goto(0,0)

# Food which is bobs goal
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(200,0)

# Pen to write the score at the top of the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions to move bob around the window
def bob_up(): # Moves bob up 7 pixels and points him up
    bob.setheading(90)
    y = bob.ycor()
    y += 7
    bob.sety(y)


def bob_down(): # Moves bob down 7 pixels and points him down
    bob.setheading(270)
    y = bob.ycor()
    y -= 7
    bob.sety(y)


def bob_left(): # Moves bob left 7 pixels and points him left
    bob.setheading(180)
    x = bob.xcor()
    x -= 7
    bob.setx(x)


def bob_right(): # Moves bob right 7 pixels and points him right
    bob.setheading(0)
    x = bob.xcor()
    x += 7
    bob.setx(x)
    
    
def move_food(): # Moves the food to some randome location in the window
    x_core = random.randrange(-300,300)
    y_core = random.randrange(-300,300)
    food.setx(x_core)
    food.sety(y_core)
  
    
def check_food_gotten():
    """Check if bob has gotten the food. If bob has gotten the food the food 
    is moved to another random location using move_food(). The new food score
    is then written to the top of the window"""
    if (((bob.ycor() < food.ycor() +15) and (bob.ycor() > food.ycor() -15)) and ((bob.xcor() < food.xcor() +15) and (bob.xcor() > food.xcor() -15))):
        # Move the food once bob gets it.
        move_food()
        
        # Add to the food eaten count
        global food_eaten
        food_eaten += 1
        
        # Write food eaten to top of window.
        pen.clear()
        pen.write("Bob has eaten {} food".format(food_eaten), align="center", font=("Serrif", 12, "normal"))
        
        
    
# Keyboard binding
wn.listen()
wn.onkeypress(bob_up, "w") 
wn.onkeypress(bob_down, "s")
wn.onkeypress(bob_left, "a")
wn.onkeypress(bob_right, "d")


while(True):
    wn.update()
    
    check_food_gotten()