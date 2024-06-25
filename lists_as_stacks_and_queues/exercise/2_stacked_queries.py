num_of_iterations = int(input())

stack_of_numbers = []

for _ in range(num_of_iterations):
    query = input().split()
    if query[0] == "1":
        stack_of_numbers.append(int(query[1]))
    elif stack_of_numbers:
        if query[0] == "2":
            stack_of_numbers.pop()
        elif query[0] == "3":
            print(max(stack_of_numbers))
        elif query[0] == "4":
            print(min(stack_of_numbers))

print(*reversed(stack_of_numbers), sep=', ')