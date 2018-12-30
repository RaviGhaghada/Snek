# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 12:19:23 2018

Main Snek game

@author: Ravi Ghaghada

"""
import pygame
import Snake
import Camera

# Define some colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

pygame.init()
screen = pygame.display.set_mode((1250,700))
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()



notDone = True
player = Snake.Snake([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)], RED, 0, 1000)
world = pygame.Surface((int(SCREEN_WIDTH), int(SCREEN_HEIGHT))) 
camera = Camera.Camera(0, 0, screen.get_size())
        
while notDone:
    
    # Process all events    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                notDone = False
                
    # Define all game logic here
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        player.changeDirection(-5)
    if keys[pygame.K_RIGHT]:
        player.changeDirection(+5)
    player.activateBoost(keys[pygame.K_SPACE]) 
        
    move_pos = player.updateCoord()
    camera.move(move_pos)
    
    # Do all the graphics stuff now
    screen.fill(WHITE)

    world.fill(BLACK)
    pygame.draw.rect(world, GREEN,((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), (20,20)))

    screen.blit(world, camera.point())
    player.drawSnake(screen)
    pygame.display.flip()

    if not keys[pygame.K_r]:
        clock.tick(120)
    else: 
        clock.tick(5)
pygame.quit()
    