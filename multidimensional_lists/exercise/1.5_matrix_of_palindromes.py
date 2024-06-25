rows, columns = [int(el) for el in input().split()]

start = ord('a')

for row in range(start, start + rows):
    for column in range(row, row + columns):
        print(chr(row), chr(column), chr(row), sep='', end=' ')
    print()

