def gather_credits(credits_needed, *course_info):
    courses = []
    total_credits = 0

    result = ''

    for name, course_credits in course_info:
        if total_credits >= credits_needed:
            break

        if name not in courses:

            courses.append(name)
            total_credits += course_credits

    if total_credits >= credits_needed:
        result = (f"Enrollment finished! Maximum credits: {total_credits}.\n"
                  f"Courses: {', '.join(sorted(courses))}")
    else:
        result = (f"You need to enroll in more courses!"
                   f" You have to gather {credits_needed - total_credits} credits more.")


    return result

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))


# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
