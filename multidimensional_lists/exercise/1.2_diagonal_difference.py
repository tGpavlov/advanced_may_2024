n = int(input())

matrix = [[int(el) for el in input().split()]for line in range(n)]

primary_sum, secondary_sum = 0, 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - i - 1]

print(abs(primary_sum - secondary_sum))