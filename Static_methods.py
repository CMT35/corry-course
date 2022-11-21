import datetime


class Employee:
    raise_amount = 1.04  # This is a class variable
    num_of_emps = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Jamleck', 'Thuo', 650000)
emp_2 = Employee('Milka', 'Wanjiku', 550000)

emp_3_str = 'John-Doe-20000'
emp_4_str = 'Jane-Doe-25000'

emp_3 = Employee.from_string(emp_3_str)
print(emp_3.pay)


my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
