row_num, col_num = [int(element) for element in input().split(', ')]

matrix = [[int(element) for element in input().split()]for row in range(row_num)]

# for row_index in range(row_num):
#     row_data = [int(element) for element in input().split(' ')]
#     matrix.append(row_data)

for col_index in range(col_num):
    col_sum = 0
    for row_index in range(row_num):
        col_sum += matrix[row_index][col_index]
    print(col_sum)

