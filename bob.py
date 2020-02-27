# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:54:03 2020

@author: Tom Hudson
"""

import turtle
import random

food_eaten = 0

wn = turtle.Screen()
wn.title("Pet Turtle by @thudsonbu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

bob = turtle.Turtle()
bob.speed(0) # speed of animation (max speed = 0)
bob.shape("turtle")
bob.color("green")
bob.shapesize(stretch_wid=1, stretch_len=1)
bob.penup() # does not draw a line
bob.goto(0,0)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(200,0)

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
    if (((bob.ycor() < food.ycor() +20) and (bob.ycor() > food.ycor() -20)) and ((bob.xcor() < food.xcor() +20) and (bob.xcor() > food.xcor() -20))):
        move_food()
        
        
    
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