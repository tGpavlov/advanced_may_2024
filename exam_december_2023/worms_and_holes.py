from collections import deque

worms = [int(w) for w in input().split()]
holes = deque(int(h) for h in input().split())

matches_count = 0
worms_count = len(worms)

while worms and holes:
    curr_worm = worms.pop()
    curr_hole = holes.popleft()

    if curr_worm <= 0:
        holes.appendleft(curr_hole)
        continue

    if curr_worm == curr_hole:
        matches_count += 1
    else:
        worms.append(curr_worm - 3)

print(f"Matches: {matches_count}" if matches_count else f"There are no matches.")

if not worms:
    print(f"Every worm found a suitable hole!" if matches_count == worms_count else "Worms left: none")
else:
    print(f"Worms left: {', '.join(str(w) for w in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(h) for h in holes)}")