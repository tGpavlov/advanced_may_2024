rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

sub_matrix_sum = float('-inf')
biggest_sub_matrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > sub_matrix_sum:
            sub_matrix_sum = current_sum
            biggest_sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {sub_matrix_sum}")
[print(*row) for row in biggest_sub_matrix]
