def is_out_hood(r, c):
    return not (0 <= r < n and 0 <= c < m)


def move_in_hood(*pos):
    r = pos[0] + directions[command][0]
    c = pos[1] + directions[command][1]

    if not is_out_hood(r, c):
        pos = neighborhood[r][c]

    return pos, r, c


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n, m = [int(num) for num in input().split()]
neighborhood = []

start_pos = tuple()

for row in range(n):
    neighborhood.append(list(input()))

    if 'B' in neighborhood[row]:
        start_pos = row, neighborhood[row].index('B')

curr_pos = start_pos

while True:
    command = input()

    curr_row, curr_col = curr_pos[0], curr_pos[1]

    next_pos, next_row, next_col = move_in_hood(curr_row, curr_col)

    if is_out_hood(next_row, next_col):
        print("The delivery is late. Order is canceled.")
        neighborhood[start_pos[0]][start_pos[1]] = ' '
        break

    if next_pos == '*':
        continue

    elif next_pos == '-':
        neighborhood[next_row][next_col] = '.'

    elif next_pos == 'P':
        neighborhood[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    elif next_pos == 'A':
        neighborhood[next_row][next_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    curr_pos = next_row, next_col

[print(''.join(row)) for row in neighborhood]
