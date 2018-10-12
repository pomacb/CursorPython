class Employees():

    def __index__(self):
        self.employee_list = []

    def add_employee(self, new_emp):
        self.employee_list.append(new_emp)

    def __str__(self):
        return f"{self.employee_list}"

    def fire_employee(self):
        pass
