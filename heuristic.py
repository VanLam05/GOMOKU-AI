import base

def checkWin(board, player):
    for r in range(base.GIRD_SIZE):
        for c in range(base.GIRD_SIZE):
            if c + 4 < base.GIRD_SIZE and \
                board[r][c] == player and \
                board[r][c + 1] == player and \
                board[r][c + 2] == player and \
                board[r][c + 3] == player and \
                board[r][c + 4] == player:
                return True
            if r + 4 < base.GIRD_SIZE and \
                board[r][c] == player and \
                board[r + 1][c] == player and \
                board[r + 2][c] == player and \
                board[r + 3][c] == player and \
                board[r + 4][c] == player:
                return True
            if r + 4 < base.GIRD_SIZE and c + 4 < base.GIRD_SIZE and \
                board[r][c] == player and \
                board[r + 1][c + 1] == player and \
                board[r + 2][c + 2] == player and \
                board[r + 3][c + 3] == player and \
                board[r + 4][c + 4] == player:
                return True
            if r + 4 < base.GIRD_SIZE and c - 4 >= 0 and \
                board[r][c] == player and \
                board[r + 1][c - 1] == player and \
                board[r + 2][c - 2] == player and \
                board[r + 3][c - 3] == player and \
                board[r + 4][c - 4] == player:
                return True
    return False


def evaluate_Lines(board, isHorizontal):
    score = int(0)
    for i in range (base.GIRD_SIZE):
        for j in range(base.GIRD_SIZE - 4):
            if isHorizontal:
                line = board[i][j:j + 5]
            else:
                line = [board[j + k][i] for k in range(5)]
            score += evaluate_Window(line)
    
    return score
def evaluate_Diagonals(board):
    score = int(0)
    for i in range(base.GIRD_SIZE - 4):
        for j in range(base.GIRD_SIZE - 4):
            diag1 = [board[i + k][j + k] for k in range(5)]
            diag2 = [board[i + 4 - k][j + k] for k in range(5)]
            score += evaluate_Window(diag1)
            score += evaluate_Window(diag2)
    
    return score

def evaluate_Window(window):
    aiCount = int(0)
    playerCount = int(0)
    emptyCount = int(0)

    for cell in window:
        if cell == base.AI_color:
            aiCount += 1
        elif cell == base.yourColor:
            playerCount += 1
        else:
            emptyCount += 1

    if (aiCount > 0 and playerCount > 0):
        return 0
    if aiCount == 4 and emptyCount == 1: return 10000
    if aiCount == 3 and emptyCount == 2: return 500
    if aiCount == 3 and emptyCount == 1: return 200
    if aiCount == 2 and emptyCount == 3: return 50

    if playerCount == 4 and emptyCount == 1: return -10000 * base.gamma
    if playerCount == 3 and emptyCount == 2: return -500 * base.gamma 
    if playerCount == 3 and emptyCount == 1: return -200 * base.gamma
    if playerCount == 2 and emptyCount == 3: return -50 * base.gamma
    return 0

def heuristicc(board):
    score = int(0)
    score += evaluate_Lines(board, True)  # Horizontal
    score += evaluate_Lines(board, False) # Vertical
    score += evaluate_Diagonals(board)     # Diagonal

    return score
