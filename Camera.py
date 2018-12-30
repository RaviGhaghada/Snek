# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:53:40 2018

Use a camera in a well defined boundary

Left boundary: maxw/2
Right boundary: -maxw/2
Upper boundary: maxh/2
Lower boundary: -maxh/2

Camera should teleport
@author: Ravi Ghaghada
"""

block = 5

class Camera:
    
    def __init__(self, x, y, maxdimensions):
        self.x = x
        self.y = y
        self.maxw, self.maxh = maxdimensions
        
    def move (self, diff):
        newx= self.x + diff[0]
        if (newx > self.maxw/2):
            newx = -self.maxw/2
        elif (newx < -self.maxw/2):
            newx = self.maxw/2
        self.x = newx
        
        newy = self.y + diff[1]
        if (newy > self.maxh/2):
            newy = -self.maxh/2
        elif (newy < -self.maxh/2):
            newy = self.maxh/2
        self.y = newy
        
    def point(self):
        print(self.x, " ", self.y, "\n")
        return (self.x, self.y)
    