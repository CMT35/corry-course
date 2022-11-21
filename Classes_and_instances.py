# Python OOP programming

class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Chris', 'Thuo', 250000)
emp_2 = Employee('Test', 'User', 100000)

print(emp_1.full_name())
print(Employee.full_name(emp_2))
emp_1.raise_amount = 1.05  # you can update the class variable raise amount to a particular instance
emp_1.apply_raise()
emp_2.apply_raise()  # Will use the class variable raise_amount = 1.04
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

