from utils.task1 import Developer, Python, Ruby, Java
from utils.task2 import E
from utils.task3 import Employees

if __name__ == "__main__":
    # print("Task1")
    # dev1 = Developer(4, 'Homer')
    # print(dev1.about())
    # print(dev1.write_code())
    # print(dev1)
    # print(dev1())
    #
    # dev2 = Python(3, 'Batman')
    # print(dev2.about())
    # print(dev2.write_code())
    # print(dev2)
    # print(dev2())
    #
    # dev3 = Ruby(5, 'Hulk')
    # print(dev3.about())
    # print(dev3.write_code())
    # print(dev3)
    # print(dev3())

    dev4 = Java(7, 'Superman')
    # print(dev4.about())
    # print(dev4.write_code())
    # print(dev4)
    # print(dev4())
    #
    # print("Task2")
    # print(E.mro())

    print("Task3")
    Emp = Employees()
    print(Employees)
    Emp = Employees.add_employee()
    print(Employees)
