# data = [el.split() for el in input().split('|')]
# print(*[' '.join(sub_list) for sub_list in data[::-1] if sub_list])

data = input().split('|')

data_list = []

for sub_list in data[::-1]:
    data_list.extend(sub_list.split())

print(*data_list)

