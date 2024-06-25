longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(',') for el in input().split('-')]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(char) for char in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)