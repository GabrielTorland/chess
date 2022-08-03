import pygame, os
from .init import screen
from .buttons import Button
from .game import play_game


def play_menu():
    # Background
    background = pygame.image.load(os.path.abspath('Pictures/game_menu.png')).convert()
    screen.blit(background, (0, 0))

    # Buttons
    co_op = Button(text="1v1", pos=(840, 350), font=60, bg="black")
    ai = Button(text="Ai", pos=(840, 450), font=60, bg="black")
    main_menu = Button(text="Main Menu", pos=(840, 550), font=60, bg="black")

    # Sound
    start_game_sound = pygame.mixer.Sound(os.path.abspath('Sounds/start_game.wav'))

    running = True
    command = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu.click() == 'Main Menu':
                    command = 'Main Menu'
                    running = False
                elif co_op.click() == '1v1':
                    start_game_sound.play()
                    command = play_game()
                    running = False
                else:
                    pass
            co_op.show()
            main_menu.show()
            ai.show()
        pygame.display.update()
    return command
