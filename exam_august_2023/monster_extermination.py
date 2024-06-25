from collections import deque

monsters_armor = deque(int(a) for a in input().split(','))
strike_strength = [int(s) for s in input().split(',')]

killed_monsters = 0

while monsters_armor and strike_strength:

    curr_armor = monsters_armor.popleft()
    curr_strike = strike_strength.pop()

    if curr_strike >= curr_armor:
        curr_strike -= curr_armor
        killed_monsters += 1

        if strike_strength:
            strike_strength.append(curr_strike + strike_strength.pop())
        else:
            if curr_strike > 0:
                strike_strength.append(curr_strike)

    else:
        curr_armor -= curr_strike
        if curr_armor > 0:
            monsters_armor.append(curr_armor)


# print("All monsters have been killed!" if not monsters_armor else "The soldier has been defeated.")
# print(f"Total monsters killed: {killed_monsters}")

if not monsters_armor:
    print("All monsters have been killed!")
if not strike_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
