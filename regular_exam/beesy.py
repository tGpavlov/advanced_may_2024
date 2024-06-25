def move_bee(pos):
    curr_row = pos[0] + directions[command][0]
    curr_col = pos[1] + directions[command][1]

    if not 0 <= curr_row < size:
        curr_row = size - 1 if curr_row < 0 else 0

    elif not 0 <= curr_col < size:
        curr_col = size - 1 if curr_col < 0 else 0

    return curr_row, curr_col


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())

field = []

bee_pos = tuple()
energy = 15
min_nectar = 30

collected_nectar = 0
is_energy_restored = False

for row in range(size):
    field.append(list(input()))

    if 'B' in field[row]:
        bee_pos = row, field[row].index('B')

field[bee_pos[0]][bee_pos[1]] = '-'

while True:
    command = input()

    bee_pos = move_bee(bee_pos)
    curr_pos = field[bee_pos[0]][bee_pos[1]]

    energy -= 1

    if curr_pos.isdigit():
        collected_nectar += int(curr_pos)
        field[bee_pos[0]][bee_pos[1]] = '-'

    elif curr_pos == 'H':
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            break

        print("Beesy did not manage to collect enough nectar.")
        break

    if energy <= 0:

        if collected_nectar >= min_nectar and not is_energy_restored:
            energy += collected_nectar - min_nectar
            collected_nectar = min_nectar
            is_energy_restored = True

        else:
            print("This is the end! Beesy ran out of energy.")
            break

field[bee_pos[0]][bee_pos[1]] = 'B'

[print(''.join(row)) for row in field]










