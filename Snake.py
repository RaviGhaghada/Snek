import pygame
import math

# Define some colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

# Define screen width and height

block=5
class Snake:
    
    def __init__(self, coord, color, angle, size):
        # states of the snake
        
        self.isAlive = True
        self.speed = block
        self.angle = int(angle)
        self.color = color
        self.coord = [coord,]*size
        self.boostlim = float(len(self.coord)-3)
        self.isBoost = False
        
    def changeDirection(self, angle):
        self.angle += angle
        
    # I love/hate this function
    def updateCoord(self):
        
        head = self.coord[0].copy()
        camera_rel = head.copy()
        
        # shift everything to the right
        self.coord.insert(0, self.coord.pop())
        # overwrite head with ... erm head
        self.coord[0] = head.copy()
        
        # if we're boosting...then go faster! 
        if (self.isBoost):
            self.speed = 2*block
        else:
            self.speed = block 
            
        # add x-component (v*cosA)
        self.coord[0][0] = int(self.coord[0][0] + self.speed*math.cos(math.radians(self.angle)))
        # add y-component (v*sinA)
        self.coord[0][1] = int(self.coord[0][1] + self.speed*math.sin(math.radians(self.angle)))
        
        # calculate the difference 
        x_diff = camera_rel[0] - self.coord[0][0]
        y_diff = camera_rel[1] - self.coord[0][1]
        
        camera_rel = [x_diff, y_diff]
        
        # shift the snake's body so that it maintains the same position on the player's window
        for i in range(len(self.coord)):
            self.coord[i] = [self.coord[i][0] + x_diff, self.coord[i][1] + y_diff]
        
        # tells us how much the camera is supposed to move
        return camera_rel
    
    def drawSnake(self, pyscreen):
        for i in range(0, len(self.coord)):
            pygame.draw.circle(pyscreen, self.color + [max(50, 255-10*i)], self.coord[i], 2*block, 0)

    def activateBoost(self, boostOn):
        if self.boostlim >= 0.01 and boostOn:
            self.boostlim = self.boostlim-0.25
            if (self.boostlim == int(self.boostlim)):
                self.coord.pop()
            self.isBoost = True
        else:
            self.isBoost = False