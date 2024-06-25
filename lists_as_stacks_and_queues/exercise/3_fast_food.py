from collections import deque

quantity_of_food = int(input())

food_queue = deque([int(x) for x in input().split()])
print(max(food_queue))

while food_queue and food_queue[0] <= quantity_of_food:
    quantity_of_food -= food_queue.popleft()


if food_queue:
    print("Orders left:", *food_queue)
else:
    print(f"Orders complete")