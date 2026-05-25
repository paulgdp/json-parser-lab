import json

# Open JSON file
with open('data/students.json', 'r') as file:
    data = json.load(file)

# Display school information
print("School:", data['school'])
print("Semester:", data['semester'])
print("Academic Year:", data['academic_year'])
print()

# Loop through students
for student in data['students']:
    print("Student ID:", student['student_id'])
    print("Name:", student['first_name'], student['last_name'])
    print("Program:", student['program'])
    print("Year Level:", student['year_level'])
    print("Email:", student['email'])
    print("Courses:")

    total_units = 0

    for course in student['courses']:
        print(" -", course['course_code'], "-", course['course_title'])
        print("   Units:", course['units'])
        print("   Instructor:", course['instructor'])

        total_units += course['units']

    print("Total Units:", total_units)
    print("---------------------------")