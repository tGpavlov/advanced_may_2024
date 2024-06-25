size = int(input())

field = [[char for char in input().split()] for _ in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_eggs_sum = float('-inf')
path = []
path_direction = ''

bunny_position = []

for row in range(size):
    for col in range(size):
        if field[row][col] == 'B':
            bunny_position = row, col

for direction in directions:
    start_position = bunny_position
    path_row = start_position[0] + directions[direction][0]
    path_col = start_position[1] + directions[direction][1]

    curr_sum = 0
    curr_path = []

    while (0 <= path_row < size and 0 <= path_col < size) and (field[path_row][path_col] != 'X'):
        curr_sum += int(field[path_row][path_col])
        curr_path.append([path_row, path_col])

        path_row += directions[direction][0]
        path_col += directions[direction][1]

    if curr_sum >= max_eggs_sum:
        max_eggs_sum = curr_sum
        path = curr_path
        path_direction = direction


print(path_direction)
print(*path, sep='\n')
print(max_eggs_sum)







