import pygame
import os
from Helpers.buttons import Button
from Helpers.init import screen


def menu():
    # Background
    background = pygame.image.load(os.path.abspath('Pictures/Main_menu.png')).convert()
    screen.blit(background, (0, 0))

    # Buttons
    play = Button(text="Play", pos=(900, 500), font=60, bg="black")
    Exit = Button(text="Exit", pos=(900, 600), font=60, bg="black")

    running = True
    command = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Exit.click() == 'Exit':
                    command = 'Exit'
                    running = False
                elif play.click() == 'Play':
                    command = 'Play'
                    running = False
                else:
                    pass
            Exit.show()
            play.show()
        pygame.display.update()
    return command

