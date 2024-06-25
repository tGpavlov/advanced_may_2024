from collections import deque

fuel = [int(f) for f in input().split()]
cons_index = deque(int(i) for i in input().split())
fuel_needed = deque(int(fn) for fn in input().split())

altitude_list = []
altitude_count = 0
is_reach_top = True
is_reach_altitude = False

while fuel and cons_index and fuel_needed:

    curr_fuel = fuel.pop()
    curr_idx = cons_index.popleft()
    curr_fuel_needed = fuel_needed.popleft()

    altitude_count += 1

    if (curr_fuel - curr_idx) >= curr_fuel_needed:
        is_reach_altitude = True
        altitude_list.append(f"Altitude {altitude_count}")
        print(f"John has reached: Altitude {altitude_count}")

    else:
        is_reach_top = False
        print(f"John did not reach: Altitude {altitude_count}")
        break


if not is_reach_top and not is_reach_altitude:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

elif is_reach_top:
    print("John has reached all the altitudes and managed to reach the top!")

else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(altitude_list)}")





