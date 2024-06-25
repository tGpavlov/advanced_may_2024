num = int(input())
matrix = [[char for char in input()]for row in range(num)]
symbol = input()

result = None

for row_index in range(num):
    for col_index in range(num):
        if matrix[row_index][col_index] == symbol:
            result = (row_index, col_index)
            break
    if result is not None:
        break

if result is not None:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")