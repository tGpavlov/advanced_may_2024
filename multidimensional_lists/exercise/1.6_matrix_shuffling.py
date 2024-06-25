def is_indices_valid(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) \
        and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(action, indices):
    if len(indices) == 4 and is_indices_valid(indices) and action == 'swap':
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *coordinates = [int(el) if el.isdigit() else el for el in input().split()]

    if command == 'END':
        break

    swap_elements(command, coordinates)
