from Pieces.knight import getKnightMoves
from Pieces.pawn import getPawnMoves
from Pieces.king import getKingMoves
from Pieces.rook import getRookMoves
from Pieces.bishop import getBishopMoves
from Pieces.queen import getQueenMoves
from .buttons import Piece_entry


def get_pos_moves(piece, chessboard, pos_move,
                  delta, start_posX_entry, start_posY_entry, occupied_spaces, turn, rocade_black, rocade_white):
    entry_delete = []
    possible_next_entry = []

    # Here i made it possible to skip some pieces, so i dont need to delete them and creating them every time.
    if piece.skip is False:
        if piece.type_piece == 'knight' or piece.type_piece == 'king':
            if piece.type_piece == 'knight':
                possible_pos = getKnightMoves((piece.x, piece.y), chessboard)
            else:
                possible_pos = getKingMoves((piece.x, piece.y), chessboard)
                if turn == 'black':
                    check_rocade(piece, rocade_black, occupied_spaces, turn, possible_pos)
                else:
                    check_rocade(piece, rocade_white, occupied_spaces, turn, possible_pos)

            # Creating buttons for possible entry's(positions).
            create_pos_entry(possible_pos, possible_next_entry, pos_move,
                             delta, start_posX_entry, start_posY_entry)

            # Checking if an enemy piece is on the possible positions.
            for entry in possible_next_entry:
                try:
                    a = occupied_spaces[(entry.x, entry.y, opposite_turn(turn))]
                except:
                    a = None
                if a is not None:
                    # Marking the enemy piece
                    entry.enemy = a
                else:
                    try:
                        a = occupied_spaces[(entry.x, entry.y, turn)]
                    except:
                        a = None
                    # Checking if a friendly piece is on the possible positions.
                    if a is not None:
                        entry_delete.append(entry)
                    else:
                        pass

        elif piece.type_piece == 'pawn':
            possible_pos, possible_kills = getPawnMoves((piece.x, piece.y), chessboard, piece)

            # Creating the buttons for possible next entry.
            create_pos_entry(possible_pos, possible_next_entry, pos_move,
                             delta, start_posX_entry, start_posY_entry)

            # Checking if an enemy piece is on the possible positions.
            for entry in possible_next_entry:
                try:
                    a = occupied_spaces[(entry.x, entry.y, opposite_turn(turn))]
                except:
                    state1 = True
                    for pos in possible_kills:
                        # Checking if the position without a enemy piece is one of the possible kill positions.
                        if entry.x == pos[0] and entry.y == pos[1]:
                            # Here i am checking if there is en passant.
                            try:
                                enemy = occupied_spaces[entry.x, piece.y, opposite_turn(turn)]
                                if len(enemy.en_passant) == 1 and enemy.en_passant[0] is True:
                                    entry.passant = enemy
                                else:
                                    entry_delete.append(entry)
                            except:
                                entry_delete.append(entry)
                            state1 = False
                            break
                    if state1:
                        a = None
                    else:
                        continue

                if a is not None:
                    state = True
                    # Checking if the enemy piece is on one of the possible kill positons.
                    for pos in possible_kills:
                        if entry.x == pos[0] and entry.y == pos[1]:
                            entry.enemy = a
                            state = False
                    if state:
                        entry_delete.append(entry)
                        continue
                else:
                    # Checking if a friendly piece is on the possible positions.
                    try:
                        a = occupied_spaces[(entry.x, entry.y, turn)]
                    except:
                        a = None
                    if a is not None:
                        entry_delete.append(entry)
                    else:
                        pass

            temp_ent = []
            for ent in entry_delete:
                possible_next_entry.remove(ent)
            entry_delete.clear()

            for ent in possible_next_entry:
                if ent.enemy is None:
                    temp_ent.append(ent)
            if len(temp_ent) == 2 or len(temp_ent) == 0:
                pass
            else:
                if abs(temp_ent[0].y - piece.y) == 2:
                    possible_next_entry.remove(temp_ent[0])

        elif piece.type_piece == 'rook':
            possible_pos = getRookMoves((piece.x, piece.y), chessboard)

            # Creating buttons for possible entry's.
            create_pos_entry(possible_pos, possible_next_entry, pos_move,
                             delta, start_posX_entry, start_posY_entry)

            for entry in possible_next_entry:
                # Checking if an enemy piece is on the possible positions.
                try:
                    a = occupied_spaces[(entry.x, entry.y, opposite_turn(turn))]
                except:
                    a = None
                if a is not None:
                    entry.enemy = a
                    entry_delete.append(entry)
                else:
                    # Checking if a friendly piece is on the possible positions.
                    try:
                        a = occupied_spaces[(entry.x, entry.y, turn)]
                    except:
                        continue
                    entry_delete.append(entry)

            temp_list = []
            entry_parts = [[], [], [], []]

            # Finding possible moves in the x-direction and y-direction.
            for ent in entry_delete:
                if ent.x == piece.x:
                    if (ent.y - piece.y) > 0:
                        entry_parts[2].append(ent)
                    else:
                        entry_parts[3].append(ent)
                else:
                    if (ent.x - piece.x) > 0:
                        entry_parts[0].append(ent)
                    else:
                        entry_parts[1].append(ent)

            min_pos_ents = []
            try:
                min_pos_ents.append(max(entry_parts[1], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[0], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(max(entry_parts[3], key=lambda obj: obj.y - piece.y))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[2], key=lambda obj: obj.y - piece.y))
            except:
                min_pos_ents.append(None)

            for ent in possible_next_entry:
                if ent not in entry_delete:
                    if ent.x == piece.x:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[2]) != 0:
                                if (ent.y - piece.y) > (min_pos_ents[3].y - piece.y):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[3]) != 0:
                                if (ent.y - piece.y) < (min_pos_ents[2].y - piece.y):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

                    elif ent.y == piece.y:
                        if (ent.x - piece.x) > 0:
                            if len(entry_parts[0]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[1].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[1]) != 0:
                                if (ent.x - piece.x) < (min_pos_ents[0].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

            for ent in min_pos_ents:
                if ent is not None:
                    if ent.enemy is not None:
                        entry_delete.remove(ent)
                    else:
                        pass
                else:
                    pass
            entry_delete = entry_delete + temp_list
            entry_parts.clear()
            temp_list.clear()

        elif piece.type_piece == 'bishop':
            possible_pos = getBishopMoves((piece.x, piece.y), chessboard)

            # Creating buttons for possible entry's.
            create_pos_entry(possible_pos, possible_next_entry, pos_move,
                             delta, start_posX_entry, start_posY_entry)

            for entry in possible_next_entry:
                # Checking if an enemy piece is on the possible positions.
                try:
                    a = occupied_spaces[(entry.x, entry.y, opposite_turn(turn))]
                except:
                    a = None
                if a is not None:
                    entry.enemy = a
                    entry_delete.append(entry)
                else:
                    # Checking if a friendly piece is on the possible positions.
                    try:
                        a = occupied_spaces[(entry.x, entry.y, turn)]
                    except:
                        continue
                    entry_delete.append(entry)

            temp_list = []
            entry_parts = [[], [], [], []]

            # Finding possible moves in the x-direction and y-direction.
            for ent in entry_delete:
                if ent.x - piece.x > 0:
                    if (ent.y - piece.y) > 0:
                        entry_parts[2].append(ent)
                    else:
                        entry_parts[3].append(ent)
                else:
                    if (ent.y - piece.y) > 0:
                        entry_parts[0].append(ent)
                    else:
                        entry_parts[1].append(ent)

            min_pos_ents = []
            try:
                min_pos_ents.append(max(entry_parts[1], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(max(entry_parts[0], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[3], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[2], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)

            for ent in possible_next_entry:
                if ent not in entry_delete:
                    if (ent.x - piece.x) > 0:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[2]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[3].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[3]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[2].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

                    else:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[0]) != 0:
                                if abs(ent.x - piece.x) > abs(min_pos_ents[1].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[1]) != 0:
                                if abs(ent.x - piece.x) > abs(min_pos_ents[0].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

            for ent in min_pos_ents:
                if ent is not None:
                    if ent.enemy is not None:
                        entry_delete.remove(ent)
                    else:
                        pass
                else:
                    pass
            entry_delete = entry_delete + temp_list
            entry_parts.clear()
            temp_list.clear()

        elif piece.type_piece == 'queen':
            possible_pos = getQueenMoves((piece.x, piece.y), chessboard)

            # Creating buttons for possible next entry's.
            create_pos_entry(possible_pos, possible_next_entry, pos_move,
                             delta, start_posX_entry, start_posY_entry)

            for entry in possible_next_entry:
                # Checking if an enemy piece is on the possible positions.
                try:
                    a = occupied_spaces[(entry.x, entry.y, opposite_turn(turn))]
                except:
                    a = None
                if a is not None:
                    entry.enemy = a
                    entry_delete.append(entry)
                else:
                    # Checking if a friendly piece is on the possible positions.
                    try:
                        a = occupied_spaces[(entry.x, entry.y, turn)]
                    except:
                        continue
                    entry_delete.append(entry)

            temp_list = []
            entry_parts = [[], [], [], [], [], [], [], []]

            # Finding possible moves in the x-direction and y-direction.
            for ent in entry_delete:
                if ent.x - piece.x > 0:
                    if (ent.y - piece.y) > 0:
                        entry_parts[2].append(ent)
                    elif ent.y == piece.y:
                        # Right
                        entry_parts[4].append(ent)
                    else:
                        entry_parts[3].append(ent)
                elif ent.x == piece.x:
                    if (ent.y - piece.y) > 0:
                        # Down
                        entry_parts[5].append(ent)
                    else:
                        # Up
                        entry_parts[6].append(ent)
                else:
                    if (ent.y - piece.y) > 0:
                        entry_parts[0].append(ent)
                    elif ent.y == piece.y:
                        # Left
                        entry_parts[7].append(ent)
                    else:
                        entry_parts[1].append(ent)

            min_pos_ents = []
            try:
                min_pos_ents.append(max(entry_parts[1], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(max(entry_parts[0], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[3], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[2], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[4], key=lambda obj: obj.x - piece.x))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[5], key=lambda obj: obj.y - piece.y))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[6], key=lambda obj: abs(obj.y - piece.y)))
            except:
                min_pos_ents.append(None)
            try:
                min_pos_ents.append(min(entry_parts[7], key=lambda obj: abs(obj.x - piece.x)))
            except:
                min_pos_ents.append(None)
            test_list = []
            for ent in possible_next_entry:
                if ent not in entry_delete:
                    if (ent.x - piece.x) > 0:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[2]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[3].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        elif ent.y == piece.y:
                            if len(entry_parts[4]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[4].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[3]) != 0:
                                if (ent.x - piece.x) > (min_pos_ents[2].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

                    elif ent.x == piece.x:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[5]) != 0:
                                if (ent.y - piece.y) > (min_pos_ents[5].y - piece.y):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[6]) != 0:
                                if abs(ent.y - piece.y) > abs(min_pos_ents[6].y - piece.y):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                    else:
                        if (ent.y - piece.y) > 0:
                            if len(entry_parts[0]) != 0:
                                if abs(ent.x - piece.x) > abs(min_pos_ents[1].x - piece.x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        elif ent.y == piece.y:
                            test_list.append(ent)
                            if len(entry_parts[7]) != 0:
                                if (piece.x - ent.x) > (piece.x - min_pos_ents[7].x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if len(entry_parts[1]) != 0:
                                if (piece.x - ent.x) > (piece.x - min_pos_ents[0].x):
                                    temp_list.append(ent)
                                else:
                                    pass
                            else:
                                pass

            for ent in min_pos_ents:
                if ent is not None:
                    if ent.enemy is not None:
                        entry_delete.remove(ent)
                    else:
                        pass
                else:
                    pass
            entry_delete = entry_delete + temp_list
            entry_parts.clear()
            temp_list.clear()
        else:
            pass

        for ent in entry_delete:
            possible_next_entry.remove(ent)
        entry_delete.clear()

        for ent in possible_next_entry:
            if ent.enemy is not None:
                if ent.enemy.type_piece == 'king':
                    ent.enemy.check.append(ent.enemy)

        return possible_next_entry
    else:
        return possible_next_entry


def show_pos_moves(possible_next_entry):
    for e in possible_next_entry:
        if e.enemy is not None:
            e.enemy.select_enemy()
        elif e.passant is not None:
            e.change_background_color()
            e.show()
        else:
            e.show()


def create_pos_entry(possible_pos, possible_next_pos, piece, delta, x_init, y_init):
    for move in possible_pos:
        possible_next_pos.append(Piece_entry((move[0], move[1]), piece, delta, x_init, y_init))


def check_rocade(piece, rocade, occupied_spaces, turn, possible_pos):
    if piece.moved is False and len(rocade) != 0:
        try:
            roc = rocade['left'].moved
        except:
            roc = True
        if roc is False:
            temp = None
            for i in range(1, piece.x):
                try:
                    temp = occupied_spaces[(i, piece.y, turn)]
                    break
                except:
                    pass
                try:
                    temp = occupied_spaces[(i, piece.y, opposite_turn(turn))]
                    break
                except:
                    pass
            if temp is None:
                possible_pos.append((piece.x - 2, piece.y))
                piece.rocade = rocade['left']
                piece.rocade_add = 1
        try:
            roc = rocade['right'].moved
        except:
            roc = True
        if roc is False:
            temp = None
            for i in range(piece.x + 1, rocade['right'].x):
                try:
                    temp = occupied_spaces[(i, piece.y, turn)]
                    break
                except:
                    pass
                try:
                    temp = occupied_spaces[(i, piece.y, opposite_turn(turn))]
                    break
                except:
                    pass
            if temp is None:
                possible_pos.append((piece.x + 2, piece.y))
                piece.rocade = rocade['right']
                piece.rocade_add = -1
        else:
            pass
    else:
        pass


def opposite_turn(turn):
    if turn == 'white':
        turn_1 = 'black'
    else:
        turn_1 = 'white'
    return turn_1
