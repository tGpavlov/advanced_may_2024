rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

index = []
sqr_sum = float('-inf')

for i in range(rows - 2):
    for j in range(columns - 2):
        num_sum = sum([
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        ])

        if num_sum > sqr_sum:
            sqr_sum = num_sum
            index = [i, j]
 
print(f"Sum = {sqr_sum}")

for i in range(index[0], index[0] + 3):
    for j in range(index[1], index[1] + 3):
        print(matrix[i][j], end=' ')
    print()