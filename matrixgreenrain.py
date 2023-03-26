#This creates green rain as in the matrix rain from the movie. 
#It has more characters and more drops.
#This is written in Python 3.
#Make sure to install pygame before trying this.

import pygame
from pygame.locals import *
import sys
import string
from random import randint

#Initialise screen
pygame.init()
#Set size for pygame screen
res = (700, 500)
#This sets the res 
set_screen = pygame.display.set_mode(res)
#Name the screen
pygame.display.set_caption('Name My Screen')

#Create letter grid lists
font_letters = pygame.font.Font('matrix code nfi.otf', 12) #12 is the font size, you can make it any size
#This sets the size, I have tried every letter, does not change much
font_letters_size = font_letters.size('A')

#calculates the number of "tiles" or "cells" in a grid based on a given resolution and the size of each tile or cell.
grid_res = (int((res[0] - res[0]%font_letters_size[0]) / font_letters_size[0]),
            int((res[1] - res[1]%font_letters_size[1]) / font_letters_size[1]))
            
#This uses import string to create the characters that are seen on the screen
letter_list = string.printable

#generates a two-dimensional grid of random letters, where each cell of the 
#grid contains one letter randomly chosen from a given list of letters.
letter_grid = [[random.choice(letter_list) for _ in range(grid_res[1])] for _ in range(grid_res[0])]

#generates a two-dimensional grid of black color values, where each cell of the grid 
#contains an RGB color value represented as a list of three integers: [R, G, B].
color_grid = [[[0, 0, 0] for _ in range(grid_res[1])] for _ in range(grid_res[0])]

column_state = []
column_speeds = []
column_timer = []

#Fill grid lists
for x in range(0, grid_res[0]):
  column_state = {x:randint(0, 7) for x in range(grid_res[0])}
  column_speeds.append(randint(4, 10))
  column_timer.append(0)
  for y in range(0, grid_res[1]):
    letter_grid[x].append(random.choice(letter_list))
    color_grid[x].append([0, 0, 0])

#Main Loop
while True:
  animation_speed = 10
  speed_increment = 1
  #This is not neccesary, I tried to add away to control the speed of the rain 
  #Does not work well, perhaps someone could figure it out
  for event in pygame.event.get():
      if event.type == KEYDOWN:
          if event.key == K_UP:
              animation_speed += speed_increment
          elif event.key == K_DOWN:
              animation_speed -= speed_increment
          elif event.key == K_ESCAPE:
              sys.exit()
              
      for i in range(len(column_speeds)):
          column_speeds[i] = randint(animation_speed // 2, animation_speed)
          
  #Randomly replace letters
  #This lets you set how many letters
  for n in range(0, 300):
    x = randint(0, grid_res[0] -1)
    y = randint(0, grid_res[1] -1)
    letter_grid[x][y] = random.choice(letter_list)
  
  #Randomly increase column_state
  for n in range(0, 2):
      column_state[randint(0, grid_res[0] - 1) += 1
      
  #Rain Logic
  for x in range(0, grid_res[0]):
  
    #Change the speed of raindrops
    for z in range(1, 7):
      if column_timer[x] == column_speeds[x]:
        column_timer[x] = 0
        for y in range(grid_res[1] - 1, -1, -1):
        
          #Move all colors down 1 letter
          if y != 0:
            color_grid[x][y] = color_grid[x][y - 1][:]
            
          # Start raindrop
                    elif column_state[x] >= 9:
                        # White tip
                        if color_grid[x][y] == [0, 0, 0]:
                            color_grid[x][y] = [240, 240, 240]
                            
                        # Fading white to green
                        elif color_grid[x][y][0] != 0:
                            color_grid[x][y][0] -= 40
                            color_grid[x][y][2] -= 40
                            
                        # Account for RGB value > 255
                        else:
                            if color_grid[x][y][1] >= 235:
                                color_grid[x][y][1] -= 20
                                
                            # Fading green to black
                            else:
                                color_grid[x][y][1] -= randint(-20, 60)
                                
                            # Account for RGB value < 0
                            if color_grid[x][y][1] <= 0:
                                color_grid[x][y][1] = 0
                                columnstate[x] = -999
                                
                    # Reset for new raindrop
                    elif (column_state[x] < 0 and color_grid[x][grid_res[1]-1][1] == 0):
                        column_state[x] = 0
                        column_speeds[x] = randint(3, 18)
                        
            else: column_timer[x] += 1

    # Erase old letters
    set_screen.fill((0, 0, 0))

    # Blit new letters
    for x, y in [(x, y) for x in range(0, gridres[0]) for y in range(0, grid_res[1])]:
        set_screen.blit(font_letters.render(letter_grid[x][y], 1, color_grid[x][y]),
               (x * font_letters_size[0], y * font_letters_size[1]))

    pygame.display.update()
    pygame.time.Clock().tick(160)
    

