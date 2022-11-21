class Employee:
    raise_amount = 1.04  # Class variables
    num_of_emps = 0

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

    @classmethod  # takes class as the first argument
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Chris', 'Thuo', 550000)
emp_2 = Employee('Victor', 'Thuo', 450000)
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-75000'
emp_str_3 = 'Lydia-Karemeri-300000'

emp_3 = Employee.from_string(emp_str_3)

Employee.set_raise_amount(1.05)  # same as Employee.raise_amount = 1.05 only that we have used a class method

print(Employee.full_name(emp_1))
print(Employee.num_of_emps)
print(emp_2.pay)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)
print(Employee.full_name(emp_3))
