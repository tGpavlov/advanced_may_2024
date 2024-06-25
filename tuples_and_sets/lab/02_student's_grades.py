students_count = int(input())

students_record = {}

for _ in range(students_count):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students_record:
        students_record[name] = []
    students_record[name].append(grade)

for student, grades in students_record.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([f'{x:.2f}' for x in grades])} (avg: {average_grade:.2f})")