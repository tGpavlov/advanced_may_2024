size = int(input())

matrix = []

alice_pos = []
tea_bags_collected = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = (row, matrix[row].index('A'))

matrix[alice_pos[0]][alice_pos[1]] = '*'

while True:
    command = input()

    row, col = [
        alice_pos[0] + directions[command][0],
        alice_pos[1] + directions[command][1]
    ]

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col].isdigit():
            tea_bags_collected += int(matrix[row][col])
            matrix[row][col] = '*'

            if tea_bags_collected >= 10:
                break

        elif matrix[row][col] == 'R':
            matrix[row][col] = '*'
            break

        else:
            matrix[row][col] = '*'

    else:
        break

    alice_pos = [row, col]

if tea_bags_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row, end='\n') for row in matrix]
