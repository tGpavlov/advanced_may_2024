matrix = [[int(j) for j in input().split(', ')] for i in range(int(input()))]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

print(
      f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}."
      f" Sum: {sum(primary_diagonal)}"
)
print(
      f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}."
      f" Sum: {sum(secondary_diagonal)}"
)

