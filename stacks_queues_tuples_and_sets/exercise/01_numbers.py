first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())

for _ in range(int(input())):
    data = input().split()
    command = data[0] + ' ' + data[1]
    num_list = [int(el) for el in data[2:]]

    if command == 'Add First':
        [first_set.add(el) for el in num_list]
    elif command == 'Add Second':
        [second_set.add(el) for el in num_list]
    elif command == 'Remove First':
        [first_set.discard(el) for el in num_list]
    elif command == 'Remove Second':
        [second_set.discard(el) for el in num_list]
    elif command == 'Check Subset':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
