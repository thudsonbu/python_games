# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:54:03 2020

@author: Tom Hudson
"""

import turtle
import random

food_eaten = 0

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

def bob_up():
    bob.setheading(90)
    y = bob.ycor()
    y += 7
    bob.sety(y)

def bob_down():
    bob.setheading(270)
    y = bob.ycor()
    y -= 7
    bob.sety(y)

def bob_left():
    bob.setheading(180)
    x = bob.xcor()
    x -= 7
    bob.setx(x)

def bob_right():
    bob.setheading(0)
    x = bob.xcor()
    x += 7
    bob.setx(x)
    
def move_food():
    x_core = random.randrange(-300,300)
    y_core = random.randrange(-300,300)
    food.setx(x_core)
    food.sety(y_core)
    
def check_food_gotten():
    if (((bob.ycor() < food.ycor() +15) and (bob.ycor() > food.ycor() -15)) and ((bob.xcor() < food.xcor() +15) and (bob.xcor() > food.xcor() -15))):
        move_food()
        global food_eaten
        food_eaten += 1
        pen.clear()
        pen.write("Bob has eaten {} food".format(food_eaten), align="center", font=("Serrif", 12, "normal"))
        
        
    
# Keyboard binding
wn.listen() # tells turtle to listen for keyboard input
wn.onkeypress(bob_up, "w") # when the user presses w run paddle_a_up
# wn.onkeyrelease(paddle_a_stop_up, "w")
wn.onkeypress(bob_down, "s")
# wn.onkeyrelease(paddle_a_stop_down, "s")
wn.onkeypress(bob_left, "a")
wn.onkeypress(bob_right, "d")


while(True):
    wn.update()
    
    check_food_gotten()