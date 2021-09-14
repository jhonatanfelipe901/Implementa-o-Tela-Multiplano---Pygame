# Jhonatan Felipe, 32091982, 4° J

import pygame, random
from pygame.locals import *
from sys import exit 

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600), 0, 32)
background = pygame.Surface((800, 600))

backgroundCenario = pygame.image.load('background1.png').convert()
backgroundCenario = pygame.transform.rotozoom(backgroundCenario, 0, 0.30)

angry = pygame.image.load('angry.png').convert_alpha()
angry = pygame.transform.rotozoom(angry, 0, 0.70)

angry2 = pygame.image.load('angry.png').convert_alpha()
angry2 = pygame.transform.rotozoom(angry, 0, 0.70)

background_width = 40
background_height = 0

width_angry = 500
heigth_angry = 500

width_angry2 = 40
heigth_angry2 = 350

pygame.display.flip()

while True:

  for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        exit()

  # desenhando os planos em cima da screen
  screen.blit(background, (0,0))
  screen.blit(backgroundCenario, (background_width,background_height))
  screen.blit(angry, (width_angry, heigth_angry))
  screen.blit(angry2, (width_angry2 , heigth_angry2))

  pygame.display.update()
