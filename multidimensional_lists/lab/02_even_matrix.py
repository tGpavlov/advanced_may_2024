row_number = int(input())

matrix = []

for row_index in range(row_number):
    row_data = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
    matrix.append(row_data)

print(matrix)