import sys

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        pass

    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Bruno","Agoston",50000)
emp_2 = Employee("test","user",60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) # Linha abaixo tem o mesmo objetivo de execução
print(Employee.fullname(emp_1))
