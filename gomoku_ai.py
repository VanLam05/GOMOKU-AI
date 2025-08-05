import sys
import pygame
import alpha_beta
import heuristic
import base


def draw_board(board):
    for i in range(base.GIRD_SIZE):
        for j in range(base.GIRD_SIZE):
            if board[i][j] == base.yourColor:
                print("X", end=" ")
            elif board[i][j] == base.AI_color:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()

def draw_board_pygame(screen):
    screen.fill(base.BOARD_COLOR)
    for i in range(base.GIRD_SIZE):
        pygame.draw.line(screen, base.LINE_COLOR, (i * base.CELL_SIZE, 0), (i * base.CELL_SIZE, base.GIRD_SIZE * base.CELL_SIZE))
        pygame.draw.line(screen, base.LINE_COLOR, (0, i * base.CELL_SIZE), (base.GIRD_SIZE * base.CELL_SIZE, i * base.CELL_SIZE))

def draw_caro(screen, x, y, color):
    if color == base.yourColor:
        pygame.draw.circle(screen, base.WHITE, (x * base.CELL_SIZE + base.CELL_SIZE // 2, y * base.CELL_SIZE + base.CELL_SIZE // 2), base.CELL_SIZE // 2 - 5)
    else:
        pygame.draw.circle(screen, base.BLACK, (x * base.CELL_SIZE + base.CELL_SIZE // 2, y * base.CELL_SIZE + base.CELL_SIZE // 2), base.CELL_SIZE // 2 - 5)

def get_mouse_pos(mouse_pos):
    x = mouse_pos[0] // base.CELL_SIZE
    y = mouse_pos[1] // base.CELL_SIZE
    return x, y

def choose_turn(screen):
    width, height = screen.get_size()
    font = pygame.font.SysFont("arial", 48, bold=True)
    button_font = pygame.font.SysFont("arial", 36)

    while True:
        screen.fill((245, 245, 245))  # Nền sáng

        # Tiêu đề
        title_text = font.render("Who goes first?", True, (30, 30, 30))
        title_rect = title_text.get_rect(center=(width // 2, height // 4))
        screen.blit(title_text, title_rect)

        # Nút "You go first"
        player_btn = pygame.Rect(0, 0, 250, 80)
        player_btn.center = (width // 2, height // 2)
        pygame.draw.rect(screen, (0, 153, 255), player_btn, border_radius=15)
        player_text = button_font.render("You go first", True, (255, 255, 255))
        player_text_rect = player_text.get_rect(center=player_btn.center)
        screen.blit(player_text, player_text_rect)

        # Nút "AI goes first"
        ai_btn = pygame.Rect(0, 0, 250, 80)
        ai_btn.center = (width // 2, height // 2 + 120)
        pygame.draw.rect(screen, (255, 102, 102), ai_btn, border_radius=15)
        ai_text = button_font.render("AI goes first", True, (255, 255, 255))
        ai_text_rect = ai_text.get_rect(center=ai_btn.center)
        screen.blit(ai_text, ai_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_btn.collidepoint(event.pos):
                    return True  # người chơi đi trước
                elif ai_btn.collidepoint(event.pos):
                    return False  # AI đi trước


def show_result(screen, text):
    font = pygame.font.SysFont(None, 72)
    text_render = font.render(text, True, (255, 0, 0))
    screen.blit(text_render, (base.CELL_SIZE, base.CELL_SIZE * (base.GIRD_SIZE // 2)))
    pygame.display.flip()
    pygame.time.wait(3000)  # chờ 3 giây rồi thoát

def main():
    pygame.init()
    screen = pygame.display.set_mode((base.GIRD_SIZE * base.CELL_SIZE, base.GIRD_SIZE * base.CELL_SIZE))
    pygame.display.set_caption("Gomoku AI")
    clock = pygame.time.Clock()

    board = [[base.emptyGrid for _ in range(base.GIRD_SIZE)] for _ in range(base.GIRD_SIZE)]
    list_move = []

    player_first = choose_turn(screen)

    if not player_first:
        # AI đi trước
        board[base.GIRD_SIZE // 2][base.GIRD_SIZE // 2] = base.AI_color
        list_move.append((base.GIRD_SIZE // 2, base.GIRD_SIZE // 2))

    while True:

        draw_board_pygame(screen)

        for i in range(base.GIRD_SIZE):
            for j in range(base.GIRD_SIZE):
                if board[i][j] == base.yourColor or board[i][j] == base.AI_color:
                    draw_caro(screen, i, j, board[i][j])
        
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = get_mouse_pos(event.pos)

                if board[x][y] != base.emptyGrid:
                    continue

                board[x][y] = base.yourColor
                list_move.append((x, y))

                if heuristic.checkWin(board, base.yourColor):
                    show_result(screen, "You Win!")
                    pygame.quit()
                    sys.exit()

                if base.emptyGrid not in [cell for row in board for cell in row]:
                    show_result(screen, "It's a Draw!")
                    pygame.quit()
                    sys.exit()

                ai_move = alpha_beta.alpha_beta(board, list_move, 0, base.AI_color)
                board[ai_move[0]][ai_move[1]] = base.AI_color
                list_move.append(ai_move)

                if heuristic.checkWin(board, base.AI_color):
                    show_result(screen, "AI Wins!")
                    pygame.quit()
                    sys.exit()

                if base.emptyGrid not in [cell for row in board for cell in row]:
                    show_result(screen, "It's a Draw!")
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    print("Welcome to Gomoku AI!")
    main()

        
