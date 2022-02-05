import pygame, copy
from .buttons import Piece_entry, Piece_button
from .init import screen
from .game_over import gg
from .possible_positions import get_pos_moves


def opposite_turn(turn):
    if turn == 'white':
        turn_1 = 'black'
    else:
        turn_1 = 'white'
    return turn_1


def move_black_pieces(pic, x, y, delta, pieces, occupied, x_init, y_init, piece, pic_mini, side=None):
    temp = Piece_button((x, y), pic, delta, x_init, y_init, piece, 'black', pic_mini)
    temp.pieces = pieces
    temp.side = side
    occupied[(temp.x, temp.y, 'black')] = temp
    pieces.append(temp)
    temp.show()
    return temp


def move_white_pieces(pic, x, y, delta, pieces, occupied, x_init, y_init, piece, pic_mini, side=None):
    temp = Piece_button((x, y), pic, delta, x_init, y_init, piece, 'white', pic_mini)
    temp.pieces = pieces
    temp.side = side
    occupied[(temp.x, temp.y, 'white')] = temp
    pieces.append(temp)
    temp.show()
    return temp


def got_you(occupied_spaces, piece_moving, turn, black_pieces, white_pieces, background, main_menu,
            rocade, dead_pieces_black, dead_pieces_white, surface_black, surface_white,
            possible_pos):
    turn = opposite_turn(turn)
    try:
        a = occupied_spaces[(piece_moving.x, piece_moving.y, turn)]
    except:
        a = None
    running = True
    command = None
    if a is not None:
        if a.type_piece == 'rook':
            try:
                del rocade[turn][a.side]
            except:
                pass
        dead_pieces(a, dead_pieces_black, dead_pieces_white, turn)
        del possible_pos[turn][(a, a.type_piece)]
        a.delete()
        del occupied_spaces[(piece_moving.x, piece_moving.y, turn)]
        capture_state = True
    else:
        capture_state = False

    current_pos_reset(black_pieces, white_pieces, background,
                      main_menu, dead_pieces_black, dead_pieces_white,
                      surface_black, surface_white)
    if len(black_pieces) == 1 and len(white_pieces) == 1:
        pygame.display.update()
        running = False
        command = gg('draw')

    return running, command, capture_state


def dead_pieces(a, dead_pieces_black, dead_pieces_white, turn):
    if turn == 'white':
        dead_pieces_white.append(a.mini_piece)
    else:
        dead_pieces_black.append(a.mini_piece)


def current_pos_reset(black_pieces, white_pieces, background, main_menu, dead_pieces_black, dead_pieces_white,
                      surface_black, surface_white):
    delta = 82
    x_init = 1523
    y_init = 79
    y_init1 = 661
    screen.blit(background, (0, 0))
    main_menu.show()
    for piece_1 in black_pieces:
        piece_1.show()
    for piece_2 in white_pieces:
        piece_2.show()
    for i in range(len(dead_pieces_white)):
        if i <= 3:
            surface_white.blit(dead_pieces_white[i], (i * delta, 0))
        elif i <= 7:
            surface_white.blit(dead_pieces_white[i], (i * delta - 4 * delta, delta))
        elif i <= 11:
            surface_white.blit(dead_pieces_white[i], (i * delta - 8 * delta, 2 * delta))
        else:
            surface_white.blit(dead_pieces_white[i], (i * delta - 12 * delta, 3 * delta))

    for i in range(len(dead_pieces_black)):
        if i <= 3:
            surface_black.blit(dead_pieces_black[i], (i * delta, 0))
        elif i <= 7:
            surface_black.blit(dead_pieces_black[i], (i * delta - 4 * delta, delta))
        elif i <= 11:
            surface_black.blit(dead_pieces_black[i], (i * delta - 8 * delta, 2 * delta))
        else:
            surface_black.blit(dead_pieces_black[i], (i * delta - 12 * delta, 3 * delta))
    screen.blit(surface_white, (x_init, y_init))
    screen.blit(surface_black, (x_init, y_init1))


def check_king(turn, possible_pos_black, possible_pos_white, occupied_spaces, possible_next_entry, black_pieces,
               white_pieces, king_black, king_white, piece_moving, chessboard, pic_cicle, delta, x_init, y_init,
               rocade_black, rocade_white, checkmate_stat):
    delete_list = []
    original_x, original_y = piece_moving.x, piece_moving.y
    del occupied_spaces[(piece_moving.x, piece_moving.y, turn)]
    if turn == 'white':
        white_check = king_white.check
        king_white.check = []
        for ent in possible_next_entry:
            occupied_spaces[(ent.x, ent.y, turn)] = piece_moving
            piece_moving.x, piece_moving.y = ent.x, ent.y
            piece_moving.update_pos()
            if ent.enemy is not None:
                ent.enemy.skip = True
                get_new_possible_pos_black(black_pieces, possible_pos_black, chessboard, pic_cicle,
                                           delta, x_init,
                                           y_init, occupied_spaces, rocade_black, rocade_white)
                ent.enemy.skip = False

            else:
                get_new_possible_pos_black(black_pieces, possible_pos_black, chessboard, pic_cicle,
                                           delta, x_init,
                                           y_init, occupied_spaces, rocade_black, rocade_white)
            del occupied_spaces[(ent.x, ent.y, turn)]
            if len(king_white.check) != 0:
                delete_list.append(ent)
                king_white.check = []
            else:
                checkmate_stat = False
        for ent in delete_list:
            possible_next_entry.remove(ent)
        king_white.check = white_check
    else:
        black_check = king_black.check
        king_black.check = []
        for ent in possible_next_entry:
            occupied_spaces[(ent.x, ent.y, turn)] = piece_moving
            piece_moving.x, piece_moving.y = ent.x, ent.y
            piece_moving.update_pos()
            if ent.enemy is not None:
                ent.enemy.skip = True
                get_new_possible_pos_white(white_pieces, possible_pos_white, chessboard, pic_cicle,
                                           delta, x_init,
                                           y_init, occupied_spaces, rocade_black, rocade_white)
                ent.enemy.skip = False
            else:
                get_new_possible_pos_white(white_pieces, possible_pos_white, chessboard, pic_cicle,
                                           delta, x_init,
                                           y_init, occupied_spaces, rocade_black, rocade_white)
            del occupied_spaces[(ent.x, ent.y, turn)]
            if len(king_black.check) != 0:
                delete_list.append(ent)
                king_black.check = []
            else:
                checkmate_stat = False
        for ent in delete_list:
            possible_next_entry.remove(ent)
        king_black.check = black_check
    delete_list.clear()
    occupied_spaces[(original_x, original_y, turn)] = piece_moving
    piece_moving.x, piece_moving.y = original_x, original_y
    piece_moving.update_pos()
    return checkmate_stat


def get_new_possible_pos_white(white_pieces, possible_pos_white, chessboard, pos_move,
                               delta, start_posX_entry,
                               start_posY_entry, occupied_spaces, rocade_black, rocade_white):
    for piece in white_pieces:
        possible_pos_white[(piece, piece.type_piece)] = get_pos_moves(piece, chessboard,
                                                                      pos_move,
                                                                      delta, start_posX_entry,
                                                                      start_posY_entry,
                                                                      occupied_spaces,
                                                                      'white', rocade_black,
                                                                      rocade_white)


def get_new_possible_pos_black(black_pieces, possible_pos_black, chessboard, pos_move,
                               delta, start_posX_entry,
                               start_posY_entry, occupied_spaces, rocade_black, rocade_white):
    for piece in black_pieces:
        possible_pos_black[(piece, piece.type_piece)] = get_pos_moves(piece, chessboard,
                                                                      pos_move,
                                                                      delta, start_posX_entry,
                                                                      start_posY_entry,
                                                                      occupied_spaces,
                                                                      'black', rocade_black,

                                                                      rocade_white)


def reset_king_rocade(king_white, king_black):
    king_white.rocade = None
    king_white.rocade_add = None
    king_black.rocade = None
    king_black.rocade_add = None


def check_stalemate(turn, possible_pos_black, possible_pos_white, running, command):
    stalemate_state = True
    if turn == 'white':
        for pos in possible_pos_white.values():
            if len(pos) != 0:
                stalemate_state = False
                break
    else:
        for pos in possible_pos_black.values():
            if len(pos) != 0:
                stalemate_state = False
                break
    if stalemate_state:
        running = False
        command = gg(opposite_turn(turn))
    return running, command
