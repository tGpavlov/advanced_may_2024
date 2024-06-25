def calc_numbers(*args):
    sum_of_positive = 0
    sum_of_negative = 0

    for digit in args:
        if digit > 0:
            sum_of_positive += digit
        else:
            sum_of_negative += digit

    return sum_of_positive, sum_of_negative


sequence = [int(x) for x in input().split()]
result = calc_numbers(*sequence)

print(f"{result[1]}\n{result[0]}")

if abs(result[1]) > result[0]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")