'''
Creating the Ball class for the game of Pong!
'''
import pygame
import random
import math

class Ball:  
    COLOR = (255,255,255)
    VELOCITY = 10
    R = 8 #radius
    

    def __init__(self, x, y):
        #for resetting the ball
        self.set_x = x
        self.set_y = y

        #to get current ball position
        self.x = x
        self.y = y

        #randomize launch angle 
        if random.random() < 0.5:
            direction = 1
        else:
            direction = -1
        angle = 0
        while angle == 0:
            angle = math.radians(random.randrange(-45,45))

        self.dx = direction * abs(math.cos(angle) * self.VELOCITY)
        self.dy = math.sin(angle)

    def initialize(self):
        self.x  = self.set_x
        self.y = self.set_y
        
        angle = 0
        while angle == 0:
            angle = math.radians(random.randrange(-45,45))

        self.dx *= -1
        self.dy = math.sin(angle)


    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x,self.y), self.R)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    