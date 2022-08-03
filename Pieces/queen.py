
def getQueenMoves(pos, chessboard):
    x, y = pos
    solution_moves = []
    test_list = []

    for i in range(1, 8-x):
        try:
            temp = chessboard[y + i][x + i]
            solution_moves.append((x + i, y + i))
        except:
            pass
    for i in range(1, 8-x):
        try:
            temp = chessboard[y - i][x + i]
            solution_moves.append((x + i, y - i))
        except:
            pass
    for i in range(1, 8-y):
        try:
            temp = chessboard[y + i][x - i]
            solution_moves.append((x - i, y + i))
        except:
            pass
    for i in range(1, y+1):
        try:
            temp = chessboard[y - i][x - i]
            solution_moves.append((x - i, y - i))
        except:
            pass

    for i in range(1, 8-y):
        try:
            temp = chessboard[y + i][x]
            solution_moves.append((x, y + i))
        except:
            pass
    for i in range(1, 8-x):
        try:
            temp = chessboard[y][x + i]
            solution_moves.append((x + i, y))
        except:
            pass
    for i in range(1, y+1):
        try:
            temp = chessboard[y - i][x]
            solution_moves.append((x, y - i))
        except:
            pass
    for i in range(1, x+1):
        try:
            test_list.append((x-i, y))
            solution_moves.append((x - i, y))
        except:
            pass
    abs_solution_moves = [tup for tup in solution_moves if (tup[0] >= 0) & (tup[1] >= 0)]
    return abs_solution_moves
