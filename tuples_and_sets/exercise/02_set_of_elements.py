numbers = input().split()
num1, num2 = int(numbers[0]), int(numbers[1])

first_set = set()   # ----> first_set = {int(input() for _ in range(num1))}
second_set = set()  # ----> second_set = {int(input() for _ in range(num2))}

for _ in range(num1):             #
    first_set.add(int(input()))   #
for _ in range(num2):             #
    second_set.add(int(input()))  #

print(*first_set.intersection(second_set), sep='\n')
