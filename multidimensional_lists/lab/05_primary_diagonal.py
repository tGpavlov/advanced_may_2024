row_col_num = int(input())

matrix = [[int(el) for el in input().split(' ')] for row in range(row_col_num)]
diagonal_sum = 0

for index in range(row_col_num):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)