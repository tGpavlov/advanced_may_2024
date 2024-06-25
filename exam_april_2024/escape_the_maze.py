size = int(input())

field = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_units = 100
player_pos = tuple()

for row in range(size):
    field.append(list(input()))

    if 'P' in field[row]:
        player_pos = (row, field[row].index('P'))

field[player_pos[0]][player_pos[1]] = '-'

while True:
    command = input()

    curr_pos = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]

    if not (0 <= curr_pos[0] < size and 0 <= curr_pos[1] < size):
        curr_pos = player_pos
        continue

    position = field[curr_pos[0]][curr_pos[1]]

    if position == 'X':
        print(f"Player escaped the maze. Danger passed!\nPlayer's health: {player_units} units")
        player_pos = curr_pos
        break

    elif position == 'M':
        player_units -= 40

        if player_units <= 0:
            player_units = 0
            player_pos = curr_pos
            break

        field[curr_pos[0]][curr_pos[1]] = '-'

    elif position == 'H':
        player_units += 15

        if player_units > 100:
            player_units = 100

        field[curr_pos[0]][curr_pos[1]] = '-'

    player_pos = curr_pos

field[player_pos[0]][player_pos[1]] = 'P'

if player_units == 0:
    print(f"Player is dead. Maze over!\nPlayer's health: {player_units} units")

[print(''.join(row)) for row in field]
