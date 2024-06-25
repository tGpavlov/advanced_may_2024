even_set = set()
odd_set = set()

for line in range(1, int(input()) + 1):
    name_char_sum = sum([ord(char) for char in input()]) // line
    even_set.add(name_char_sum) if name_char_sum % 2 == 0 else odd_set.add(name_char_sum)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=', ')

