n = int(input())

matrix = [[int(x) for x in input().split()] for row in range(n)]
coordinates = ((int(x) for x in c.split(',')) for c in input().split())

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
    (0, 0)
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        row_dir, col_dir = row + x, col + y

        if 0 <= row_dir < n and 0 <= col_dir < n:
            matrix[row_dir][col_dir] -= matrix[row][col] if matrix[row_dir][col_dir] > 0 else 0


alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]