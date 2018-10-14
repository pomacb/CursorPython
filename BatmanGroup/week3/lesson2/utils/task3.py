class Employees:

    employee_list = []

    def __add__(self, empl2add: object):
        if empl2add.years_experience >= 3:
            self.employee_list.append(empl2add)
            print(f"Employee {empl2add.name} successfully hired")
        else:
            print(f"Employee {empl2add.name} wasn't hired")
            print(f"Please, try again in {3 - empl2add.years_experience} year(s)")
        return self

    def print_employee(self):
        sorted_employee = sorted(self.employee_list, key=lambda x: x.years_experience)
        for empl in sorted_employee:
            print(f"{empl.name} - {empl.years_experience} years, {empl.language}")


    def fire_employee(self):
        pass
