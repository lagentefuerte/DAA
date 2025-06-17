N = 9
def isLine (sudoku, number, index):
    x, y = index
    for i in range(N):
        if sudoku[x][i] == number:
            return False
    return True

def isColumn (sudoku, number, index):
    x, y = index
    for i in range(N):
        if sudoku[i][y] == number:
            return False
    return True

def isCell (sudoku, number, index):
    found = False
    x, y = index
    startx, starty = (x//int((N ** 0.5)) * int((N ** 0.5)), y//int((N ** 0.5)) * int((N ** 0.5)))
    for i in range(startx, startx+int(N ** 0.5)):
        for j in range(starty, starty+int(N ** 0.5)):
            if sudoku[i][j] == number:
                return False
    return True

def isFeasible(sudoku, number, index):
    return isLine(sudoku, number, index) and isColumn(sudoku, number, index) and isCell(sudoku, number, index)

def isSol (index):
    return index[0] > N-1 or index[1] > N-1

def isEmpty (num):
    return num == 0

def newPos (pos):
    return (pos[0] + 1, 0) if pos[1] == N-1 else (pos[0], pos[1] + 1)

def solveSudokuBacktracking (sudoku, pos):
    x, y = pos
    if isSol(pos):
        return True
    if isEmpty(sudoku[x][y]):
        for i in range(1, 10):
            if isFeasible(sudoku, i, pos):
                sudoku[x][y] = i
                if solveSudokuBacktracking(sudoku, newPos(pos)):
                    return True
                sudoku[x][y] = 0
    else:
        return solveSudokuBacktracking(sudoku, newPos(pos))
    return False



sudoku = []
for i in range(N):
    sudoku.append(list(map(int, input().strip().split())))
solveSudokuBacktracking(sudoku, (0, 0))
for row in sudoku:
    print(" ".join(map(str, row)))