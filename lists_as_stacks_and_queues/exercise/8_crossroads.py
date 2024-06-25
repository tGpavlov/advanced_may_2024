from collections import deque

green_light_duration = int(input())
free_window = int(input())
cars = deque()

passed_cars = 0
crashed = False

while True:
    command = input()

    if command == "END":
        break
    if command == "green":
        if cars:
            current_car = cars.popleft()
            time_left = green_light_duration - len(current_car)
            while time_left > 0:
                passed_cars += 1
                if cars:
                    current_car = cars.popleft()
                    time_left -= len(current_car)
                else:
                    break
            if time_left == 0:
                passed_cars += 1
            if free_window >= abs(time_left):
                if time_left < 0:
                    passed_cars += 1
            else:
                idx = free_window + time_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)

if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
