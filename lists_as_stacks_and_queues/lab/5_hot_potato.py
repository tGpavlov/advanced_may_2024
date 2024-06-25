from collections import deque

kids_queue = deque(input().split())
toss_count = int(input())

while len(kids_queue) > 1:
    for i in range(toss_count - 1):
        first_kid = kids_queue.popleft()
        kids_queue.append(first_kid)
    print(f"Removed {kids_queue.popleft()}")

print(f"Last is {kids_queue.popleft()}")