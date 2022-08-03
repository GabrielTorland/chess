import pygame
from Helpers.buttons import Button
from Helpers.init import screen
import os


def gg(turn):
    # Background
    if turn == 'white':
        background = pygame.image.load(os.path.abspath('Pictures/white_wins.png')).convert_alpha()
    elif turn == 'black':
        background = pygame.image.load(os.path.abspath('Pictures/black_wins.png')).convert_alpha()
    else:
        background = pygame.image.load(os.path.abspath('Pictures/draw.png')).convert_alpha()
    screen.blit(background, (0, 0))

    # Button
    play = Button(text="Play Again", pos=(840, 450), font=60, bg="black")
    main_menu = Button(text="Main Menu", pos=(840, 550), font=60, bg="black")

    command = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu.click() == 'Main Menu':
                    command = 'Main Menu'
                    running = False
                elif play.click() == 'Play Again':
                    command = 'Play'
                    running = False
                else:
                    pass
            main_menu.show()
            play.show()
        pygame.display.update()
    return command
