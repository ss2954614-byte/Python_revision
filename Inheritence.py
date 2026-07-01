class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def details(self):
        print(f"{self.employee_id} | {self.name}")


class DataScientist(Employee):
    def __init__(self, employee_id, name, primary_skill):
        super().__init__(employee_id, name)
        self.primary_skill = primary_skill

    def details(self):
        super().details()
        print(f"Primary Skill : {self.primary_skill}")


employee = DataScientist(
    employee_id="DS-101",
    name="Suhail",
    primary_skill="Machine Learning"
)

employee.details()