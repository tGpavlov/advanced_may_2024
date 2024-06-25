from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque(int(lock) for lock in input().split())
value_of_intelligence = int(input())

shot_counter = 0

while bullets and locks:
    shot_counter += 1
    value_of_intelligence -= bullet_price
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_lock >= current_bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    if bullets and size_of_barrel == shot_counter:
        print("Reloading!")
        shot_counter = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")