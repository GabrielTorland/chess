import pygame
from Helpers.buttons import Button
import os
from .game_over import gg
from .functions_for_game import got_you, current_pos_reset, check_king, get_new_possible_pos_white, \
    get_new_possible_pos_black, opposite_turn, reset_king_rocade, check_stalemate
from .possible_positions import get_pos_moves, show_pos_moves
from .start_chess import start_chess
from .gj_pawn import gj
from .init import screen


def play_game():
    # Background
    background = pygame.image.load(os.path.abspath('Pictures/board.png')).convert()
    pos_move = pygame.image.load(os.path.abspath('Pictures/possible_move.png')).convert_alpha()
    surface_black = pygame.Surface((328, 328), pygame.SRCALPHA, 32).convert_alpha()
    surface_white = pygame.Surface((328, 328), pygame.SRCALPHA, 32).convert_alpha()
    check = pygame.image.load(os.path.abspath('Pictures/check.png')).convert_alpha()
    checkmate = pygame.image.load(os.path.abspath('Pictures/checkmate.png')).convert_alpha()

    # Sound
    move_sound = pygame.mixer.Sound(os.path.abspath('Sounds/move.wav'))
    capture_sound = pygame.mixer.Sound(os.path.abspath('Sounds/capture.wav'))
    castling_sound = pygame.mixer.Sound(os.path.abspath('Sounds/castling.wav'))
    check_sound = pygame.mixer.Sound(os.path.abspath('Sounds/check.wav'))
    checkmate_sound = pygame.mixer.Sound(os.path.abspath('Sounds/checkmate.wav'))

    # Button
    main_menu = Button(text="Main Menu", pos=(50, 500), font=60, bg="black")

    # Chessboard
    chessboard = [[1] * 8 for i in range(8)]
    black_pieces = []
    white_pieces = []
    rocade_black = {}
    rocade_white = {}
    possible_next_entry = []
    dead_pieces_black = []
    dead_pieces_white = []
    pawn_op_white = []
    pawn_op_black = []
    occupied_spaces = {}
    possible_pos_black = {}
    possible_pos_white = {}

    # Constants
    delta = 128
    start_posX_entry = 461
    start_posY_entry = 12
    start_posX_piece = 462
    start_posY_piece = 13

    # Variables
    running = True
    command = None
    piece_moving = None
    turn = 'white'

    # Start of game initialization
    king_white, king_black = start_chess(delta, black_pieces, white_pieces, background, main_menu, occupied_spaces,
                                         start_posX_piece, start_posY_piece, rocade_black, rocade_white, pawn_op_white,
                                         pawn_op_black, possible_pos_black, possible_pos_white, chessboard, pos_move,
                                         start_posX_entry, start_posY_entry)
    kings = {'black': king_black,
             'white': king_white}
    pieces = white_pieces
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = True
                if main_menu.click() == 'Main Menu':
                    command = main_menu.click()
                    running = False
                elif piece_moving is not None:
                    # Getting position of mouse
                    x, y = pygame.mouse.get_pos()
                    for pos in possible_next_entry:
                        if pos.click(x, y) is not None:
                            sound_state = False
                            state = False
                            for pas in piece_moving.pieces:
                                if pas != piece_moving and len(pas.en_passant) == 1 and pas.en_passant[0] is True:
                                    pas.en_passant[0] = False
                                else:
                                    pass
                            if piece_moving.type_piece == 'pawn':
                                if pos.passant is not None:
                                    del occupied_spaces[(pos.passant.x, pos.passant.y, opposite_turn(turn))]
                                    pos.passant.x, pos.passant.x = pos.x, pos.y
                                    pos.passant.update_pos()
                                    occupied_spaces[(pos.x, pos.y, opposite_turn(turn))] = pos.passant

                                if abs(piece_moving.y - pos.y) == 2:
                                    piece_moving.en_passant.append(True)
                                else:
                                    piece_moving.en_passant.append(False)

                            # Checking if there is a possible rocade.
                            elif piece_moving.type_piece == 'king' and abs(piece_moving.x - pos.x) == 2:
                                # Changing the position of the rook in the rocade.
                                castling_sound.play()
                                sound_state = True
                                del occupied_spaces[(piece_moving.rocade.x, piece_moving.rocade.y, turn)]
                                piece_moving.rocade.pos = [(pos.x + piece_moving.rocade_add) * delta + start_posX_piece,
                                                           pos.y * delta + start_posY_piece]
                                piece_moving.rocade.x, piece_moving.rocade.y = pos.x + piece_moving.rocade_add, pos.y
                                occupied_spaces[(piece_moving.rocade.x, piece_moving.rocade.y, turn)] = \
                                    piece_moving.rocade
                                piece_moving.rocade.update_rect()
                                piece_moving.rocade.moved = True
                            else:
                                reset_king_rocade(king_white, king_black)

                            # Changing position to the piece moving.
                            del occupied_spaces[(piece_moving.x, piece_moving.y, turn)]
                            piece_moving.x, piece_moving.y = pos.x, pos.y
                            piece_moving.update_pos()
                            piece_moving.update_rect()
                            occupied_spaces[(piece_moving.x, piece_moving.y, turn)] = piece_moving
                            possible_next_entry.clear()

                            running, command, capture_state = got_you(occupied_spaces, piece_moving, turn, black_pieces,
                                                                      white_pieces,
                                                                      background,
                                                                      main_menu, {'white': rocade_white,
                                                                                  'black': rocade_black},
                                                                      dead_pieces_black, dead_pieces_white,
                                                                      surface_black,
                                                                      surface_white,
                                                                      {'black': possible_pos_black,
                                                                       'white': possible_pos_white})
                            piece_moving.moved = True

                            # Changing turn.
                            if turn == 'white':
                                if piece_moving.type_piece == 'pawn' and pos.y == 0:
                                    pygame.display.update()
                                    p = gj(pawn_op_white, turn, piece_moving, occupied_spaces, pieces,
                                           {'black': possible_pos_black,
                                            'white': possible_pos_white})
                                    possible_pos_white[(p, p.type_piece)] = get_pos_moves(p, chessboard, pos_move,
                                                                                          delta, start_posX_entry,
                                                                                          start_posY_entry,
                                                                                          occupied_spaces,
                                                                                          'white', rocade_black,
                                                                                          rocade_white)
                                    current_pos_reset(black_pieces, white_pieces, background,
                                                      main_menu, dead_pieces_black, dead_pieces_white,
                                                      surface_black, surface_white)
                                pieces = black_pieces
                                turn = 'black'

                            else:
                                if piece_moving.type_piece == 'pawn' and pos.y == 7:
                                    pygame.display.update()
                                    p = gj(pawn_op_black, turn, piece_moving, occupied_spaces, pieces,
                                           {'black': possible_pos_black,
                                            'white': possible_pos_white})
                                    possible_pos_black[(p, p.type_piece)] = get_pos_moves(p, chessboard, pos_move,
                                                                                          delta, start_posX_entry,
                                                                                          start_posY_entry,
                                                                                          occupied_spaces,
                                                                                          'black', rocade_black,
                                                                                          rocade_white)
                                    current_pos_reset(black_pieces, white_pieces, background,
                                                      main_menu, dead_pieces_black, dead_pieces_white,
                                                      surface_black, surface_white)
                                pieces = white_pieces
                                turn = 'white'

                            # Getting new possible position for all the pieces
                            get_new_possible_pos_white(white_pieces, possible_pos_white,
                                                       chessboard, pos_move, delta, start_posX_entry,
                                                       start_posY_entry, occupied_spaces, rocade_black,
                                                       rocade_white)
                            get_new_possible_pos_black(black_pieces, possible_pos_black,
                                                       chessboard, pos_move, delta, start_posX_entry,
                                                       start_posY_entry, occupied_spaces, rocade_black,
                                                       rocade_white)

                            # Check or Checkmate
                            if len(king_white.check) != 0:
                                checkmate_stat = True
                                for p in white_pieces:
                                    possible_next_entry = possible_pos_white[
                                        (p, p.type_piece)]
                                    if len(possible_next_entry) != 0:
                                        checkmate_stat = check_king('white', possible_pos_black, possible_pos_white,
                                                                    occupied_spaces,
                                                                    possible_next_entry, black_pieces, white_pieces,
                                                                    king_black,
                                                                    king_white,
                                                                    p, chessboard, pos_move, delta, start_posX_entry,
                                                                    start_posY_entry,
                                                                    rocade_black, rocade_white, checkmate_stat)

                                if checkmate_stat:
                                    screen.blit(checkmate, (0, 0))
                                    checkmate_sound.play()
                                    command = gg('black')
                                    running = False
                                else:
                                    screen.blit(check, (0, 0))
                                    check_sound.play()
                                    king_white.check = []
                                sound_state = True

                            elif len(king_black.check) != 0:
                                checkmate_stat = True
                                for p in black_pieces:
                                    possible_next_entry = possible_pos_black[
                                        (p, p.type_piece)]
                                    if len(possible_next_entry) != 0:
                                        checkmate_stat = check_king('black', possible_pos_black, possible_pos_white,
                                                                    occupied_spaces,
                                                                    possible_next_entry, black_pieces, white_pieces,
                                                                    king_black,
                                                                    king_white,
                                                                    p, chessboard, pos_move, delta, start_posX_entry,
                                                                    start_posY_entry,
                                                                    rocade_black, rocade_white, checkmate_stat)

                                if checkmate_stat:
                                    screen.blit(checkmate, (0, 0))
                                    checkmate_sound.play()
                                    command = gg('white')
                                    running = False
                                else:
                                    screen.blit(check, (0, 0))
                                    check_sound.play()
                                    king_black.check = []
                                sound_state = True
                            if sound_state is False:
                                if capture_state is False:
                                    move_sound.play()
                                else:
                                    capture_sound.play()
                            break
                    if state:
                        current_pos_reset(black_pieces, white_pieces, background,
                                          main_menu, dead_pieces_black, dead_pieces_white,
                                          surface_black, surface_white)
                    piece_moving = None

                else:
                    x, y = pygame.mouse.get_pos()
                    for piece in pieces:
                        if piece.click(x, y) is not None:
                            # Changing bg-color on the selected piece.
                            piece.selected()

                            # The piece active(moving) is set.
                            piece_moving = piece

                            # Retrieving possible positions.
                            if turn == 'black':
                                possible_next_entry = possible_pos_black[(piece_moving, piece_moving.type_piece)]
                            else:
                                possible_next_entry = possible_pos_white[(piece_moving, piece_moving.type_piece)]

                            if len(possible_next_entry) != 0 and len(king_black.check) == 0 and len(
                                    king_white.check) == 0:
                                check_king(turn, possible_pos_black, possible_pos_white, occupied_spaces,
                                           possible_next_entry, black_pieces, white_pieces, king_black, king_white,
                                           piece_moving, chessboard, pos_move, delta, start_posX_entry,
                                           start_posY_entry,
                                           rocade_black, rocade_white, checkmate_stat=False)
                            if running is True:
                                running, command = check_stalemate(turn, possible_pos_black, possible_pos_white,
                                                                   running, command)
                            show_pos_moves(possible_next_entry)
                            break
        pygame.display.update()
    else:
        pass
    return command
