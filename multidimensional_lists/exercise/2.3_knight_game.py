board_size = int(input())

play_board = [list(input()) for _ in range(board_size)]

positions = (
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []

    for row in range(board_size):
        for col in range(board_size):
            if play_board[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < board_size and 0 <= pos_col < board_size:
                        if play_board[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [row, col]

    if knight_with_most_attacks:
        r, c = knight_with_most_attacks
        play_board[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)
