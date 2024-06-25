from collections import deque

water = int(input())
name = input()

queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        liters = int(command)
        if liters <= water:
            water -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    else:
        _, liters = command.split()
        water += int(liters)
    command = input()

print(f"{water} liters left")