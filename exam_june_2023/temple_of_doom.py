from collections import deque

tools = deque(int(t) for t in input().split())
substances = [int(s) for s in input().split()]
challenges = [int(c) for c in input().split()]

is_lost = True

while tools and substances:
    curr_tool = tools.popleft()
    curr_sub = substances.pop()

    result = curr_tool * curr_sub

    if result in challenges:
        challenges.pop(challenges.index(result))

        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            is_lost = False
            break

    else:
        tools.append(curr_tool + 1)

        curr_sub -= 1
        if not curr_sub == 0:
            substances.append(curr_sub)


if is_lost:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}" )

if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}" )

if challenges:
    print(f"Challenges: {', '.join(str(c) for c in challenges)}" )