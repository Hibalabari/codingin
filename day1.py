# importing the labraries
from math import floor
import pygame
import sys
import time
import random

# Initializing the pygame
pygame.int()
# Frames per second
clock = pygame.time.clock()
# Function to draw 
def draw floor():
    screen.blit(floor_img, (floor_x, 560))
    screen.blit(floor_img, (floor_x + 490, 560))
    # Function to create pipes
    def create_pipes():
        pipe_y = random.choice(pipe_height)
        top_pipe = pipe_img.get_rect(midbottom=(470, pipe_y))
        bottom = pipe_img.get_rect(midtop)
