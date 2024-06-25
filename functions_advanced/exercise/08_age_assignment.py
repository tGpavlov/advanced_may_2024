def age_assignment(*names, **kv_pairs):
    result = []

    for name in names:
        for key, value in kv_pairs.items():

            if name.startswith(key):
                result.append(f"{name} is {value} years old.")
                break

    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))