def is_in_board(x, y, n):
    return 0 <= x < n and 0 <= y < n

def op_dir(dir):
    return (-dir[0], -dir[1])

def getAntiColor(color):
    return 1 - color

def draw_board(board):
    for i in range(GIRD_SIZE):
        for j in range(GIRD_SIZE):
            if board[i][j] == yourColor:
                print("X", end=" ")
            elif board[i][j] == AI_color:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()

GIRD_SIZE = 15
CELL_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARD_COLOR = (200, 200, 200)
LINE_COLOR = (50, 50, 50)
yourColor = 0
AI_color = 1
emptyGrid = -1
gamma = 1.2