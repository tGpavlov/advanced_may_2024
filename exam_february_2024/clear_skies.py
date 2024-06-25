size = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

sky = []

jet_pos = tuple()
armor_value = 300
enemy_count = 0

for row in range(size):
    sky.append(list(input()))

    enemy_count += sky[row].count('E')

    if 'J' in sky[row]:
        jet_pos = row, sky[row].index('J')

sky[jet_pos[0]][jet_pos[1]] = '-'


while True:
    command = input()

    jet_pos = jet_pos[0] + directions[command][0], jet_pos[1] + directions[command][1]
    row, col = jet_pos[0], jet_pos[1]

    curr_pos = sky[row][col]

    if curr_pos == 'E':
        enemy_count -= 1
        sky[row][col] = '-'
        armor_value -= 100

        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        if armor_value == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
            break

    elif curr_pos == 'R':
        armor_value = 300
        sky[row][col] = '-'

sky[row][col] = 'J'

[print(''.join(row)) for row in sky]








