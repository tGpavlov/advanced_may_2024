size = int(input())
commands = tuple(input().split())

miner_field = [input().split() for row in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

miner_position = tuple()
total_coal = 0

for row in range(size):
    if 's' in miner_field[row]:
        miner_position = row, miner_field[row].index('s')
    if 'c' in miner_field[row]:
        total_coal += miner_field[row].count('c')

for command in commands:
    miner_position = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]

    if not (0 <= miner_position[0] < size and 0 <= miner_position[1] < size):
        miner_position = miner_position[0] - directions[command][0], miner_position[1] - directions[command][1]
        continue

    if miner_field[miner_position[0]][miner_position[1]] == 'e':
        print(f"Game over! {miner_position}")
        break

    elif miner_field[miner_position[0]][miner_position[1]] == 'c':
        total_coal -= 1
        miner_field[miner_position[0]][miner_position[1]] = '*'
        if total_coal == 0:
            print(f"You collected all coal! {miner_position}")

else:
    if total_coal:
        print(f"{total_coal} pieces of coal left. {miner_position}")