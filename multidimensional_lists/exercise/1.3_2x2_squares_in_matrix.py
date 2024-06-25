rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

sqr_matrices = 0

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        char = matrix[row_idx][col_idx]

        if char == matrix[row_idx + 1][col_idx] \
                and char == matrix[row_idx][col_idx + 1] \
                and char == matrix[row_idx + 1][col_idx + 1]:
            sqr_matrices += 1

print(sqr_matrices)
