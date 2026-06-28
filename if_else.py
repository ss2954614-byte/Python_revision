candidate = {
    "cgpa": 8.1,
    "python_skill": True,
    "projects": 4
}

if (
    candidate["cgpa"] >= 7.5
    and candidate["python_skill"]
    and candidate["projects"] >= 2
):
    status = "Eligible for Interview"
else:
    status = "Needs Improvement"

print(status)