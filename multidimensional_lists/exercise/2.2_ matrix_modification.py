n = int(input())

matrix = [[int(num) for num in input().split()] for r in range(n)]

while True:
    command, *coordinates = input().split()

    if command == 'END':
        break

    row, col, value = int(coordinates[0]), int(coordinates[1]), int(coordinates[2])

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    elif command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

[print(*row) for row in matrix]
