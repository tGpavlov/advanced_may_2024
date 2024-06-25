from collections import deque

string = deque(input().split())

colours = ["red", "yellow", "blue", "orange", "purple", "green"]
req_colours = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

founded_colours = []

while string:
    first_string = string.popleft()
    second_string = string.pop() if string else ''

    for colour in (first_string + second_string, second_string + first_string):
        if colour in colours:
            founded_colours.append(colour)
            break
    else:
        for el in (first_string[:-1], second_string[:-1]):
            if el:
                string.insert(len(string) // 2, el)


for colour in set(req_colours.keys()).intersection(founded_colours):
    if not req_colours[colour].issubset(founded_colours):
        founded_colours.remove(colour)

print(founded_colours)