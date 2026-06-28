import csv

with open("student_report.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"{row['Student_Name']} | "
            f"CGPA: {row['CGPA']}"
        )