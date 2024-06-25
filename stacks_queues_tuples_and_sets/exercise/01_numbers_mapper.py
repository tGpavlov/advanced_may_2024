first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())

mapper = {
    'Add First': lambda x: first_set.update(x),
    'Add Second': lambda x: second_set.update(x),
    'Remove First': lambda x: first_set.difference_update(x),
    'Remove Second': lambda x: second_set.difference_update(x),
    'Check Subset': lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set))
}

for _ in range(int(input())):
    data = input().split()
    command = data[0] + ' ' + data[1]
    num_list = [int(el) for el in data[2:]]

    mapper[command](num_list)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
