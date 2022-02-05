
def getKingMoves(pos, chessboard):
    x, y = pos
    solution_moves = []
    try:
        temp = chessboard[y+1][x]
        solution_moves.append((x, y+1))
    except:
        pass
    try:
        temp = chessboard[y+1][x+1]
        solution_moves.append((x+1, y+1))
    except:
        pass
    try:
        temp = chessboard[y+1][x-1]
        solution_moves.append((x-1, y+1))
    except:
        pass
    try:
        temp = chessboard[y][x+1]
        solution_moves.append((x+1, y))
    except:
        pass
    try:
        temp = chessboard[y][x-1]
        solution_moves.append((x-1, y))
    except:
        pass
    try:
        temp = chessboard[y-1][x]
        solution_moves.append((x, y-1))
    except:
        pass
    try:
        temp = chessboard[y-1][x+1]
        solution_moves.append((x+1, y-1))
    except:
        pass
    try:
        temp = chessboard[y-1][x-1]
        solution_moves.append((x-1, y-1))
    except:
        pass
    abs_solution_moves = [tup for tup in solution_moves if (tup[0] >= 0) & (tup[1] >= 0)]
    return abs_solution_moves