import pygame, sys, os
from Helpers.game import play_game
from Helpers.main_menu import menu
from Helpers.play_menu import play_menu

# Change working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def main():
    running = True

    # Title and icon
    pygame.display.set_caption("Chess")
    icon = pygame.image.load(os.path.abspath('Pictures/chess.png')).convert()
    pygame.display.set_icon(icon)
    order = menu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if order == 'Play':
            order = play_menu()
        elif order == 'Main Menu':
            order = menu()
        else:
            pygame.quit()
            sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
