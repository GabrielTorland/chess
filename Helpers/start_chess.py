import pygame
import os
from .init import screen
from .functions_for_game import move_white_pieces, move_black_pieces
from .buttons import Piece_button
from .possible_positions import get_pos_moves


def start_chess(delta, black_pieces, white_pieces, background, main_menu, occupied, x_init, y_init,
                rocade_black, rocade_white, pawn_op_white, pawn_op_black, possible_pos_black, possible_pos_white,
                chessboard, pos_move, start_posX_entry, start_posY_entry):
    screen.blit(background, (0, 0))
    main_menu.show()

    # pictures of pieces
    knight_pic_black = pygame.image.load(os.path.abspath('Pictures/horse_black.png')).convert_alpha()
    knight_pic_white = pygame.image.load(os.path.abspath('Pictures/horse_white.png')).convert_alpha()
    pawn_pic_white = pygame.image.load(os.path.abspath('Pictures/pawn_white.png')).convert_alpha()
    pawn_pic_black = pygame.image.load(os.path.abspath('Pictures/pawn_black.png')).convert_alpha()
    king_pic_white = pygame.image.load(os.path.abspath('Pictures/king_white.png')).convert_alpha()
    king_pic_black = pygame.image.load(os.path.abspath('Pictures/king_black.png')).convert_alpha()
    rook_pic_white = pygame.image.load(os.path.abspath('Pictures/rook_white.png')).convert_alpha()
    rook_pic_black = pygame.image.load(os.path.abspath('Pictures/rook_black.png')).convert_alpha()
    bishop_pic_white = pygame.image.load(os.path.abspath('Pictures/bishop_white.png')).convert_alpha()
    bishop_pic_black = pygame.image.load(os.path.abspath('Pictures/bishop_black.png')).convert_alpha()
    queen_pic_white = pygame.image.load(os.path.abspath('Pictures/queen_white.png')).convert_alpha()
    queen_pic_black = pygame.image.load(os.path.abspath('Pictures/queen_black.png')).convert_alpha()

    knight_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/horse_black_mini.png')).convert_alpha()
    knight_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/horse_white_mini.png')).convert_alpha()
    pawn_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/pawn_white_mini.png')).convert_alpha()
    pawn_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/pawn_black_mini.png')).convert_alpha()
    king_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/king_white_mini.png')).convert_alpha()
    king_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/king_black_mini.png')).convert_alpha()
    rook_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/rook_white_mini.png')).convert_alpha()
    rook_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/rook_black_mini.png')).convert_alpha()
    bishop_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/bishop_white_mini.png')).convert_alpha()
    bishop_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/bishop_black_mini.png')).convert_alpha()
    queen_pic_white_mini = pygame.image.load(os.path.abspath('Pictures/queen_white_mini.png')).convert_alpha()
    queen_pic_black_mini = pygame.image.load(os.path.abspath('Pictures/queen_black_mini.png')).convert_alpha()

    # Starting position
    move_white_pieces(knight_pic_white, 1, 7, delta, white_pieces, occupied, x_init, y_init, 'knight',
                      knight_pic_white_mini)
    move_white_pieces(knight_pic_white, 6, 7, delta, white_pieces, occupied, x_init, y_init, 'knight',
                      knight_pic_white_mini)
    king_white = move_white_pieces(king_pic_white, 4, 7, delta, white_pieces, occupied, x_init, y_init, 'king',
                                   king_pic_white_mini)
    rook_1_white = move_white_pieces(rook_pic_white, 0, 7, delta, white_pieces, occupied, x_init, y_init, 'rook',
                                     rook_pic_white_mini,
                                     side='left')
    rook_2_white = move_white_pieces(rook_pic_white, 7, 7, delta, white_pieces, occupied, x_init, y_init, 'rook',
                                     rook_pic_white_mini,
                                     side='right')
    move_white_pieces(bishop_pic_white, 2, 7, delta, white_pieces, occupied, x_init, y_init, 'bishop',
                      bishop_pic_white_mini)
    move_white_pieces(bishop_pic_white, 5, 7, delta, white_pieces, occupied, x_init, y_init, 'bishop',
                      bishop_pic_white_mini)
    move_white_pieces(queen_pic_white, 3, 7, delta, white_pieces, occupied, x_init, y_init, 'queen',
                      queen_pic_white_mini)
    for i in range(8):
        move_white_pieces(pawn_pic_white, i, 6, delta, white_pieces, occupied, x_init, y_init, 'pawn',
                          pawn_pic_white_mini)

    move_black_pieces(knight_pic_black, 1, 0, delta, black_pieces, occupied, x_init, y_init, 'knight',
                      knight_pic_black_mini)
    move_black_pieces(knight_pic_black, 6, 0, delta, black_pieces, occupied, x_init, y_init, 'knight',
                      knight_pic_black_mini)
    king_black = move_black_pieces(king_pic_black, 4, 0, delta, black_pieces, occupied, x_init, y_init, 'king',
                                   king_pic_black_mini)
    rook_1_black = move_black_pieces(rook_pic_black, 0, 0, delta, black_pieces, occupied, x_init, y_init, 'rook',
                                     rook_pic_black_mini,
                                     side='left')
    rook_2_black = move_black_pieces(rook_pic_black, 7, 0, delta, black_pieces, occupied, x_init, y_init, 'rook',
                                     rook_pic_black_mini,
                                     side='right')
    move_black_pieces(bishop_pic_black, 2, 0, delta, black_pieces, occupied, x_init, y_init, 'bishop',
                      bishop_pic_black_mini)
    move_black_pieces(bishop_pic_black, 5, 0, delta, black_pieces, occupied, x_init, y_init, 'bishop',
                      bishop_pic_black_mini)
    move_black_pieces(queen_pic_black, 3, 0, delta, black_pieces, occupied, x_init, y_init, 'queen',
                      queen_pic_black_mini)
    for i in range(8):
        move_black_pieces(pawn_pic_black, i, 1, delta, black_pieces, occupied, x_init, y_init, 'pawn',
                          pawn_pic_black_mini)

    rocade_black['left'] = rook_1_black
    rocade_black['right'] = rook_2_black
    rocade_white['left'] = rook_1_white
    rocade_white['right'] = rook_2_white

    pawn_op_black.append(Piece_button((0, 6), queen_pic_black, delta, x_init, y_init, 'queen', 'black',
                                      queen_pic_black_mini,
                                      pieces=black_pieces))
    pawn_op_black.append(Piece_button((1, 6), bishop_pic_black, delta, x_init, y_init, 'bishop', 'black',
                                      bishop_pic_black_mini,
                                      pieces=black_pieces))
    pawn_op_black.append(Piece_button((2, 6), rook_pic_black, delta, x_init, y_init, 'rook', 'black',
                                      rook_pic_black_mini,
                                      pieces=black_pieces))
    pawn_op_black.append(Piece_button((3, 6), knight_pic_black, delta, x_init, y_init, 'knight', 'black',
                                      knight_pic_black_mini,
                                      pieces=black_pieces))
    pawn_op_white.append(Piece_button((0, 1), queen_pic_white, delta, x_init, y_init, 'queen', 'white',
                                      queen_pic_white_mini,
                                      pieces=white_pieces))
    pawn_op_white.append(Piece_button((1, 1), bishop_pic_white, delta, x_init, y_init, 'bishop', 'white',
                                      bishop_pic_white_mini,
                                      pieces=white_pieces))
    pawn_op_white.append(Piece_button((2, 1), rook_pic_white, delta, x_init, y_init, 'rook', 'white',
                                      rook_pic_white_mini,
                                      pieces=white_pieces))
    pawn_op_white.append(Piece_button((3, 1), knight_pic_white, delta, x_init, y_init, 'knight', 'white',
                                      knight_pic_white_mini,
                                      pieces=white_pieces))

    for piece in white_pieces:
        possible_pos_white[(piece, piece.type_piece)] = get_pos_moves(piece, chessboard, pos_move, delta,
                                                                      start_posX_entry,
                                                                      start_posY_entry, occupied, 'white', rocade_black,
                                                                      rocade_white)
    for piece in black_pieces:
        possible_pos_black[(piece, piece.type_piece)] = get_pos_moves(piece, chessboard, pos_move, delta,
                                                                      start_posX_entry,
                                                                      start_posY_entry, occupied, 'black', rocade_black,
                                                                      rocade_white)
    return king_white, king_black


def add_promotions(piece, pawn_op):
    pawn_op.append(
        Piece_button((piece.x, piece.y), piece.piece, piece.delta, piece.x_init, piece.y_init,
                     piece.type_piece, piece.turn,
                     piece.mini_piece,
                     pieces=piece.pieces))
