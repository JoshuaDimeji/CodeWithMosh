"""
This program collects user's data such as name, matric number, number of courses offering
and scores in exams.
It then prints out the user details, grade of each course and calculate the Grade point average of that semester
"""

student_fullname = input("Enter your full name here: ")
matric_number = input("Enter your matriculation number here: ")
course_count = int(input("How many courses offering this semester? : "))
course_index = 1

gp = 0
totalUnit = 0
while course_count >= 1:
    grade = 0
    course_title = input(f"Enter the title for course {course_index}: ")
    score = int(input(f"Enter score got in course {course_index}: "))
    unit = int(input(f"Enter the unit of course {course_index}: "))
    if 70 <= score <= 100:
        grade += 5.0
    elif 60 <= score < 70:
        grade += 4.0
    elif 50 <= score < 60:
        grade += 3.0
    elif 45 <= score < 50:
        grade += 2.0
    elif 40 <= score < 45:
        grade += 1.0
    else:
        grade += 0.0
        print(f"You have a carry over on {course_title}")

    course_count -= 1
    course_index += 1
    score += score
    totalUnit += unit
    gradePoint = grade * unit
    gp  += gradePoint


cgp = gp / totalUnit
print(f"Your total score is: {score}")
print(f"Your cummulative grade point is: {cgp}")