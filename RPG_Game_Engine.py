"""
Devon Griffith
February 14, 2018
Copyright
"""
import pygame
import time
import sys
import random

pygame.init()


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)


def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.time.strftime("%S")


def centre_box(box_width, window_width):
    start = 0 + (window_width / 4)
    return start

create_window()

player = pygame.image.load('/Users/Devon/Desktop/DevonIcon.png')

playerX = 10
playerY = 10

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

clock = pygame.time.Clock()

counter = 0

images = ['', '', '']

isRunning = True

centre_window_w = 1 / 2
centre_window_h = 1 / 2

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    window.fill(BLACK)

    pygame.draw.rect(window, RED, [(window_width / 4), 125, (window_width / 2), (window_height /2)], 0)
    centre_box(250, window_width)

    #window.blit(player, (playerX, playerY))

    pygame.display.update()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        player = pygame.image.load(images[counter])
        counter = (counter + 1) % len(images)
        playerY = playerY + 5

    clock.tick(60)

pygame.quit()
sys.exit()
