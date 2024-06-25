size = 5
matrix = []
shoot_targets = []
total_targets = 0
position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        position = [row, matrix[row].index('A')]

    total_targets += matrix[row].count('x')

for _ in range(int(input())):
    command = input().split()

    action = command[0]
    direction = command[1]

    if action == 'move':
        steps = int(command[2])

        row = position[0] + directions[direction][0] * steps
        col = position[1] + directions[direction][1] * steps

        if not (0 <= row < size and 0 <= col < size) or matrix[row][col] == 'x':
            continue
        matrix[position[0]][position[1]] = '.'
        matrix[row][col] = 'A'
        position = [row, col]

    elif action == 'shoot':
        row = position[0] + directions[direction][0]
        col = position[1] + directions[direction][1]

        while 0 <= row < size and 0 <= col < size:
            if matrix[row][col] == 'x':
                total_targets -= 1
                shoot_targets.append([row, col])
                matrix[row][col] = '.'
                break
            row += directions[direction][0]
            col += directions[direction][1]


if total_targets == 0:
    print(f"Training completed! All {len(shoot_targets)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

print(*shoot_targets, sep='\n')