row_num, col_num = [int(element) for element in input().split(', ')]
matrix = [[int(element) for element in input().split(', ')] for row in range(row_num)]

max_sum = float('-inf')
sub_matrix = None

for row_index in range(row_num - 1):
    for col_index in range(col_num - 1):
        current_num = matrix[row_index][col_index]
        next_num = matrix[row_index][col_index + 1]
        below_num = matrix[row_index + 1][col_index]
        diagonal_num = matrix[row_index + 1][col_index + 1]

        current_sum = sum((current_num, next_num, below_num, diagonal_num))
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_num, next_num], [below_num, diagonal_num]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)



