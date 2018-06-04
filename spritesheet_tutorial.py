import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Set the height and width of the screen
screen_width = 700
screen_height = 400

#initialize pygame
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])

class spritesheet():
