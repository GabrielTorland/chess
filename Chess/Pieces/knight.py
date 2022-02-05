
def getKnightMoves(pos, chessboard):
    x, y = pos
    solution_moves = []
    try:
        temp = chessboard[y-2][x+1]
        solution_moves.append((x+1, y-2))
    except:
        pass
    try:
        temp = chessboard[y-1][x+2]
        solution_moves.append((x+2, y-1))
    except:
        pass
    try:
        temp = chessboard[y+1][x+2]
        solution_moves.append((x+2, y+1))
    except:
        pass
    try:
        temp = chessboard[y+2][x+1]
        solution_moves.append((x+1, y+2))
    except:
        pass
    try:
        temp = chessboard[y+2][x-1]
        solution_moves.append((x-1, y+2))
    except:
        pass
    try:
        temp = chessboard[y+1][x-2]
        solution_moves.append((x-2, y+1))
    except:
        pass
    try:
        temp = chessboard[y-1][x-2]
        solution_moves.append((x-2, y-1))
    except:
        pass
    try:
        temp = chessboard[y-2][x-1]
        solution_moves.append((x-1, y-2))
    except:
        pass
    abs_solution_moves = [tup for tup in solution_moves if (tup[0] >= 0) & (tup[1] >= 0)]
    return abs_solution_moves
