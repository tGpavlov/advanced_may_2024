rows_number, column_number = [int(element) for element in input().split(', ')]

matrix = []
sum_of_nums = 0

for row_index in range(rows_number):
    row_data = [int(element) for element in input().split(', ')]
    sum_of_nums += sum(row_data)
    matrix.append(row_data)

print(sum_of_nums, matrix, sep='\n')