from collections import deque

contestants = deque(int(el) for el in input().split())
pies = [int(el) for el in input().split()]

while contestants and pies:
    curr_contest = contestants.popleft()
    curr_pie = pies.pop()

    if curr_contest >= curr_pie:
        curr_contest -= curr_pie

        if curr_contest > 0:
            contestants.append(curr_contest)

    else:
        curr_pie -= curr_contest

        if curr_pie == 1 and pies:
            curr_pie += pies.pop()
        pies.append(curr_pie)

if not pies and not contestants:
    print("We have a champion!")
elif not pies:
    print(f"We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(el) for el in contestants])}")
elif not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(el) for el in pies])}")