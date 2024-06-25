from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cups = deque(int(x) for x in input().split(', '))

milkshakes = 0

while cups and chocolate and milkshakes < 5:
    curr_chocolate = chocolate.pop()
    curr_cup = cups.popleft()

    if curr_chocolate <= 0 and curr_cup <= 0:
        continue
    elif curr_chocolate <= 0:
        cups.appendleft(curr_cup)
        continue
    elif curr_cup <= 0:
        chocolate.append(curr_chocolate)
        continue

    if curr_chocolate == curr_cup:
        milkshakes += 1
    else:
        cups.append(curr_cup)
        chocolate.append(curr_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate) or 'empty'}")  # --->  new method
print(f"Milk: {', '.join(str(x) for x in cups) or 'empty'}")

