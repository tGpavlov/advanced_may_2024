from collections import deque

expression = input().split()

operators = '+-*/'
nums = deque()

functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b,
}

for char in expression:
    if char not in operators:
        nums.append(int(char))
    else:
        while len(nums) > 1:
            first_num = nums.popleft()
            second_num = nums.popleft()

            nums.appendleft(functions[char](first_num, second_num))

print(*nums)