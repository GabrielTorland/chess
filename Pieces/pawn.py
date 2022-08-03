def getPawnMoves(pos, chessboard, piece):
    x, y = pos
    solution_moves = []
    kill_pos = []
    if piece.turn == 'black':
        if piece.moved is False:
            try:
                temp = chessboard[y + 2][x]
                solution_moves.append((x, y + 2))
            except:
                pass

        try:
            temp = chessboard[y + 1][x]
            solution_moves.append((x, y + 1))
        except:
            pass
        try:
            temp = chessboard[y + 1][x + 1]
            kill_pos.append((x + 1, y + 1))
            solution_moves.append((x + 1, y + 1))
        except:
            pass
        try:
            temp = chessboard[y + 1][x - 1]
            kill_pos.append((x - 1, y + 1))
            solution_moves.append((x - 1, y + 1))
        except:
            pass

    else:
        if piece.moved is False:
            try:
                temp = chessboard[y - 2][x]
                solution_moves.append((x, y - 2))
            except:
                pass

        try:
            temp = chessboard[y - 1][x]
            solution_moves.append((x, y - 1))
        except:
            pass
        try:
            temp = chessboard[y - 1][x + 1]
            kill_pos.append((x + 1, y - 1))
            solution_moves.append((x + 1, y - 1))
        except:
            pass
        try:
            temp = chessboard[y - 1][x - 1]
            kill_pos.append((x - 1, y - 1))
            solution_moves.append((x - 1, y - 1))
        except:
            pass
    abs_kill_moves = [tup for tup in kill_pos if (tup[0] >= 0) & (tup[1] >= 0)]
    abs_solution_moves = [tup for tup in solution_moves if (tup[0] >= 0) & (tup[1] >= 0)]
    return abs_solution_moves, abs_kill_moves
