from collections import deque

bees = deque(int(el) for el in input().split())
nectar = deque(int(el) for el in input().split())
operators = deque(input().split())

total_honey_made = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b if b != 0 else 0,  # IMPORTANT
    '*': lambda a, b: a * b,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    else:
        total_honey_made += abs(operations[operators.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(char) for char in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(char) for char in nectar)}")
