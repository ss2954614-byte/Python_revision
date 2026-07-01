class StudentProfile:
    def __init__(self, name, cgpa, specialization):
        self.name = name
        self.cgpa = cgpa
        self.specialization = specialization

    def display_profile(self):
        print(f"Name           : {self.name}")
        print(f"CGPA           : {self.cgpa}")
        print(f"Specialization : {self.specialization}")


student = StudentProfile(
    name="Suhail",
    cgpa=7.28,
    specialization="AI & Data Science"
)

student.display_profile()