def move_boat(boat_poss, direction):
    curr_row = boat_poss[0] + direction[command][0]
    curr_col = boat_poss[1] + direction[command][1]

    if not 0 <= curr_row < size:
        curr_row = size - 1 if curr_row < 0 else 0

    elif not 0 <= curr_col < size:
        curr_col = size - 1 if curr_col < 0 else 0

    return curr_row, curr_col


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())
fishing_area = []

fisher_poss = []
fish_amount = 0
fish_quota = 20
is_whirlpool = False


for row in range(size):
    fishing_area.append(list(input()))

    if 'S' in fishing_area[row]:
        fisher_poss = [row, fishing_area[row].index('S')]

fishing_area[fisher_poss[0]][fisher_poss[1]] = '-'

while True:
    command = input()

    if command == 'collect the nets':
        break

    fisher_poss = move_boat(fisher_poss, directions)

    curr_poss = fishing_area[fisher_poss[0]][fisher_poss[1]]

    if curr_poss == 'W':
        is_whirlpool = True
        break

    elif curr_poss.isdigit():
        fish_amount += int(curr_poss)
        fishing_area[fisher_poss[0]][fisher_poss[1]] = '-'

fishing_area[fisher_poss[0]][fisher_poss[1]] = 'S'

if not is_whirlpool:

    print("Success! You managed to reach the quota!" if fish_amount >= fish_quota else
          f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {fish_quota - fish_amount} tons of fish more.")

    if fish_amount:
        print(f"Amount of fish caught: {fish_amount} tons.")

    [print(''.join(row)) for row in fishing_area]

else:

    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{fisher_poss[0]},{fisher_poss[1]}]")

