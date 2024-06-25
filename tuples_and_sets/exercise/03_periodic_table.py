num = int(input())

elements = set()

for _ in range(num):
    for el in input().split():
        elements.add(el)

print(*elements, sep='\n')

