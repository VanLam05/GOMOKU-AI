import base
import heuristic

MAX_DEPTH = 3

def get_candidate_moves(board, list_move):
    n = len(board)
    moves = set()

    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    for (x, y) in list_move:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if(base.is_in_board(nx, ny, n) and board[nx][ny] == base.emptyGrid):
                moves.add((nx, ny))
    return list(moves)

def minimax(board,list_move, depth, color, alpha, beta, isMaximizing):
    if heuristic.checkWin(board, base.AI_color):
        return 1000000 - depth
    if heuristic.checkWin(board, base.yourColor):
        return -1000000 + depth

    if depth == MAX_DEPTH - (len(list_move) >= 25):
        return heuristic.heuristicc(board)
    
    antiColor = base.getAntiColor(color)

    maxScore = float('-inf')
    minScore = float('inf')
    candidate_moves = get_candidate_moves(board, list_move)
    candidate_moves = reversed(candidate_moves)

    for move in candidate_moves:
        x, y = move
        board[x][y] = color
        list_move.append((x, y))
        score = minimax(board, list_move, depth + 1, antiColor, alpha, beta, not isMaximizing)
        board[x][y] = base.emptyGrid
        list_move.pop()

        if (isMaximizing):
            maxScore = max(maxScore, score)
            alpha = max(alpha, score)
            if (beta <= alpha): 
                break
        else:
            minScore = min(minScore, score)
            beta = min(beta, score)
            if (beta <= alpha):
                break

    if isMaximizing:
        return maxScore
    else:
        return minScore




def alpha_beta(board, list_move, depth, color):

    antiColor = base.getAntiColor(color)
    alpha = float('-inf')
    beta = float('inf')
    best_move = None
    maxScore = float('-inf')

    candidate_moves = get_candidate_moves(board, list_move)

    for move in candidate_moves:
        x, y = move
        board[x][y] = color
        list_move.append((x, y))
        score = minimax(board, list_move, depth + 1, antiColor, alpha, beta, 0)
        list_move.pop()
        if (maxScore < score):
            maxScore = score
            best_move = (x, y)
        alpha = max(alpha, score)
        board[x][y] = base.emptyGrid

    return best_move



        
