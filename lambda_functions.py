students = [
    {"name": "Aman", "cgpa": 8.5},
    {"name": "Priya", "cgpa": 7.4},
    {"name": "Rahul", "cgpa": 9.1},
    {"name": "Neha", "cgpa": 8.0}
]

students = sorted(
    students,
    key=lambda student: student["cgpa"],
    reverse=True
)

for student in students:
    print(student)