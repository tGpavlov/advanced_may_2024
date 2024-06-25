def is_m_in_cupboard(r, c):
    return 0 <= r < n and 0 <= c < m


def move_m_in_cupboard(*pos):
    r = pos[0] + directions[command][0]
    c = pos[1] + directions[command][1]

    if is_m_in_cupboard(r, c):
        pos = cupboard[r][c]

    return pos, r, c


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n, m = [int(el) for el in input().split(',')]

cupboard = []

mouse_pos = tuple()
cheese_count = 0
is_danger = False

for row in range(n):
    cupboard.append(list(input()))

    if 'M' in cupboard[row]:
        mouse_pos = row, cupboard[row].index('M')

    if 'C' in cupboard[row]:
        cheese_count += cupboard[row].count('C')

cupboard[mouse_pos[0]][mouse_pos[1]] = '*'

while True:
    command = input()

    if command == 'danger':
        print("Mouse will come back later!")
        break

    # curr_row, curr_col = mouse_pos[0], mouse_pos[1]

    next_pos, next_row, next_col = move_m_in_cupboard(mouse_pos[0], mouse_pos[1])

    if not is_m_in_cupboard(next_row, next_col):
        print("No more cheese for tonight!")
        break

    if next_pos == '@':
        continue

    elif next_pos == 'T':
        print("Mouse is trapped!")
        mouse_pos = next_row, next_col
        break

    elif next_pos == 'C':
        cheese_count -= 1
        cupboard[next_row][next_col] = '*'

        if cheese_count <= 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            mouse_pos = next_row, next_col
            break

    mouse_pos = next_row, next_col

cupboard[mouse_pos[0]][mouse_pos[1]] = 'M'
[print(''.join(row)) for row in cupboard]