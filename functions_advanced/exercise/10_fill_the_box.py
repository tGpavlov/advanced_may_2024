from collections import deque


def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes = deque(args)

    while cubes[0] != "Finish":
        volume -= cubes.popleft()

        if volume < 0:
            cubes_left = sum(x for x in cubes if x != "Finish")
            return f"No more free space! You have {cubes_left + abs(volume)} more cubes."

    return f"There is free space in the box. You could put {volume} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
