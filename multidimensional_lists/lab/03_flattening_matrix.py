row_number = int(input())

# matrix = [[int(el) for el in input().split(', ')]for i in range(row_number)]
#
# flattened_matrix = [num for lists in matrix for num in lists]

flattened_matrix = []

for row_index in range(row_number):
    row_data = [int(element) for element in input().split(', ')]
    flattened_matrix.extend(row_data) # or flattened_matrix += row_data

print(flattened_matrix)


