'''
Creating the Player class for the game of Pong!
'''
import pygame

class Player:
    COLOR = (255,255,255)
    VELOCITY = 3.5
    WIDTH = 15
    HEIGHT = 100

    def __init__(self, x, y):
        #for resetting the players
        self.set_x = x
        self.set_y = y
        
        #to get current player position
        self.x = x
        self.y = y

    def initialize(self):
        self.x  = self.set_x
        self.y = self.set_y

    def move(self, up = True):
        if up:
            self.y -= self.VELOCITY
        else: self.y += self.VELOCITY

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x,self.y,self.WIDTH,self.HEIGHT))

