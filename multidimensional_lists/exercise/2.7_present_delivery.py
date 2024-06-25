num_of_presents = int(input())
size_neighborhood = int(input())

neighborhood = []
santa_pos = []

nice_kids = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size_neighborhood):
    neighborhood.append(input().split())

    if 'S' in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index('S')]
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    nice_kids += neighborhood[row].count('V')

while True:
    command = input()

    if command == 'Christmas morning':
        break

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        nice_kids_visited += 1
        num_of_presents -= 1
    elif house == 'C':
        for coordinates in directions.values():
            r = santa_pos[0] + coordinates[0]
            c = santa_pos[1] + coordinates[1]

            if neighborhood[r][c].isalpha():
                if neighborhood[r][c] == 'V':
                    nice_kids_visited += 1

                neighborhood[r][c] = '-'
                num_of_presents -= 1

            if not num_of_presents:
                break

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not num_of_presents or nice_kids_visited == nice_kids:
        break

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not num_of_presents and nice_kids_visited < nice_kids:
    print("Santa ran out of presents!")

[print(*row)for row in neighborhood]

if nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")









