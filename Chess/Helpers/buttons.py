import pygame
from .init import screen
import math


class Button:
    def __init__(self, text, pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)
        self.text = text

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                return self.text


class Piece_button:

    def __init__(self, pos, piece, delta, x_init, y_init, type_piece, turn, mini_piece, pieces=None):
        self.x, self.y = pos
        self.pos = [self.x*delta + x_init, self.y*delta + y_init]
        self.piece = piece
        self.mini_piece = mini_piece
        self.delta = delta
        self.y_init = y_init
        self.x_init = x_init
        self.pieces = pieces
        self.moved = False
        self.side = None
        self.skip = False
        self.turn = turn
        self.en_passant = []
        self.type_piece = type_piece
        self.rocade = None
        self.rocade_add = None
        self.check = []
        self.change_pic()

    def change_pic(self):
        self.size = self.piece.get_size()
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def show(self):
        self.update_piece()
        screen.blit(self.surface, (self.pos[0], self.pos[1]))

    def update_pos(self):
        self.pos = [self.x * self.delta + self.x_init, self.y * self.delta + self.y_init]

    def show_pawn_swap(self):
        self.surface.fill('#00b300')
        self.surface.blit(self.piece, (0, 0))
        screen.blit(self.surface, (self.pos[0], self.pos[1]))

    def delete(self):
        self.pieces.remove(self)

    def update_piece(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.surface.blit(self.piece, (0, 0))

    def select_enemy(self):
        self.surface.fill('#FF6347')
        self.surface.blit(self.piece, (0, 0))
        screen.blit(self.surface, (self.pos[0], self.pos[1]))

    def update_rect(self):
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def selected(self):
        self.surface.fill('#fcf75e')
        self.surface.blit(self.piece, (0, 0))
        screen.blit(self.surface, (self.pos[0], self.pos[1]))

    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            return x, y
        else:
            return None


class Piece_entry:

    def __init__(self, pos, piece, delta, x_init, y_init):
        self.x, self.y = pos
        self.full_pos = pos
        self.pos = [self.x*delta + x_init, self.y*delta + y_init]
        self.piece = piece
        self.delta = delta
        self.passant = None
        self.change_pic()
        self.enemy = None

    def change_pic(self):
        self.size = self.piece.get_size()
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
        self.surface.blit(self.piece, (0, 0))
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.pos[0], self.pos[1]))

    def change_background_color(self):
        self.surface.fill('#FF6347')
        self.surface.blit(self.piece, (0, 0))

    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            return x, y
        else:
            return None
