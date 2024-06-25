from collections import deque

rows, cols = [int(el) for el in input().split()]
snake = list(input())

snake_copy = deque()

for row in range(rows):
    while len(snake_copy) < cols:
        snake_copy.extend(snake)

    if row % 2 == 0:
        print(*[snake_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[snake_copy.popleft() for _ in range(cols)][::-1], sep='')

