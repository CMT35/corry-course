class Employee:
    raise_amount = 1.04
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
        self.pay = self.pay * self.raise_amount

    def __repr__(self):  # Representation of an object used for debugging and logging
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # Readable representation of an object, used as a display by end user
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Kaylin', 'Thuo', 350000)
emp_2 = Employee('Tracey', 'Wahito', 400000)

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)
print(len(emp_1))


