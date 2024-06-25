size = int(input())

game_board = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

gambler_pos = tuple()
money = 100
is_jackpot = False
is_lost = False

for row in range(size):
    game_board.append(list(input()))

    if 'G' in game_board[row]:
        gambler_pos = row, game_board[row].index('G')

game_board[gambler_pos[0]][gambler_pos[1]] = '-'

command = input()

while command != 'end':

    gambler_pos = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if not (0 <= gambler_pos[0] < size and 0 <= gambler_pos[1] < size):
        is_lost = True
        break

    curr_pos = game_board[gambler_pos[0]][gambler_pos[1]]

    if curr_pos == 'W':
        money += 100

    elif curr_pos == 'P':
        money -= 200

        if money <= 0:
            is_lost = True
            break

    elif curr_pos == 'J':
        money += 100000
        is_jackpot = True
        break

    game_board[gambler_pos[0]][gambler_pos[1]] = '-'

    command = input()

if not is_lost:
    game_board[gambler_pos[0]][gambler_pos[1]] = 'G'

    print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$" if is_jackpot
          else f"End of the game. Total amount: {money}$")

    [print(''.join(row)) for row in game_board]

else:
    print("Game over! You lost everything!")