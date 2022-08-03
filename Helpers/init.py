import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((1920, 1080), 16)
