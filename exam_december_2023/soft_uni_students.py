def softuni_students(*students_info, **course_info):
    softuni_info = {}
    invalid_students = set()

    result = ''

    for student_id, student_name in students_info:

        if student_id not in course_info:
            invalid_students.add(student_name)
        else:
            course_name = course_info[student_id]
            softuni_info[student_name] = course_name

    for username, course in sorted(softuni_info.items()):
        result += (f"*** A student with the username {username}"
                   f" has successfully finished the course {course}!\n")

    sorted_invalid_students = sorted(invalid_students)

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted_invalid_students)}"

    return result.strip()


# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))

# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
