import pygame
from .buttons import Piece_button
from .possible_positions import get_pos_moves
from .start_chess import add_promotions


def gj(pieces, turn, piece_moving, occupied_spaces, current_pieces, possible_pos):
    if turn == 'white':
        for i in range(len(pieces)):
            pieces[i].y = piece_moving.y + i
            pieces[i].x = piece_moving.x
            pieces[i].update_pos()
            pieces[i].update_rect()
            pieces[i].show_pawn_swap()
    else:
        for i in range(len(pieces)):
            pieces[i].y = piece_moving.y - i
            pieces[i].x = piece_moving.x
            pieces[i].update_pos()
            pieces[i].update_rect()
            pieces[i].show_pawn_swap()
    running = True
    p = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for piece in pieces:
                    if piece.click(x, y) is not None:
                        piece.x, piece.y = piece_moving.x, piece_moving.y
                        piece.update_pos()
                        piece.update_rect()
                        occupied_spaces[(piece.x, piece.y, turn)] = piece
                        del possible_pos[turn][(piece_moving, piece_moving.type_piece)]
                        current_pieces.remove(piece_moving)
                        current_pieces.append(piece)
                        p = piece
                        pieces.remove(piece)
                        running = False
                        break
                    else:
                        pass
        pygame.display.update()
        if p is not None:
            add_promotions(p, pieces)
        else:
            pass
    return p
