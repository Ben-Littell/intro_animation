import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi

# Game Constants
WIDTH = 700
LENGTH = 500
SIZE = (WIDTH, LENGTH)
FPS = 60

##############################################################################
##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()

# loop variables
rect_x = 50
x_velocity = 5
rect_y = 50
y_velocity = 3
rect_side = 50
running = True
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rect_x + rect_side > WIDTH or rect_x < 0:
        x_velocity *= -1

    if rect_y + rect_side > LENGTH or rect_y < 0:
        y_velocity *= -1

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [rect_x, rect_y, rect_side, rect_side])
    rect_x += x_velocity
    rect_y += y_velocity
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()







