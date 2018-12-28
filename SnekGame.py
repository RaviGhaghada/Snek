# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 12:19:23 2018

Main Snek game

@author: Ravi Ghaghada

"""
import pygame
import Snake

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
player = Snake.Snake([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)], RED, 0, 50  )
camera_pos = [100, 100]
world = pygame.Surface((1000,1000))
        
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
    
    camera_pos[0] = move_pos[0] + camera_pos[0] 
    camera_pos[1] = move_pos[1] + camera_pos[1]
    # Do all the graphics stuff now
    screen.fill(WHITE)

    world.fill(BLACK)
    for x in range(10):
        pygame.draw.rect(world, GREEN,((x*100,x*100), (20,20)))

    screen.blit(world, camera_pos)
    player.drawSnake(screen)
    pygame.display.flip()

    clock.tick(60)
    
pygame.quit()
    