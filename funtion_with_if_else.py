def evaluate_student(cgpa, internships, projects):
    if cgpa >= 7.5 and internships >= 1 and projects >= 2:
        return "Placement Ready"

    return "Needs Improvement"


status = evaluate_student(
    cgpa=8.2,
    internships=2,
    projects=4
)

print(status)