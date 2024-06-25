from collections import deque

cups = deque(int(el) for el in input().split())
bottles = [int(el) for el in input().split()]

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)


if not cups:
    print("Bottles:", *bottles)
else:
    print("Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")