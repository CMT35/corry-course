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


class Developer(Employee):  # inherits everything from Employee class
    raise_amount = 1.10  # Gives priority to the newly defined class variable in developer sub-class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employess = []
        else:
            self.employess = employees

    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def print_emp(self):
        for emp in self.employess:
            print('-->', emp.full_name())


dev_1 = Developer('Karen', 'Mane', 95000, 'Java')
dev_2 = Developer('lydiah', 'Njoki', 100000, 'Python')

mgr_1 = Manager('Chris', 'Mwangi', 750000, [dev_1, dev_2])

print(mgr_1.email)
# mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emp()

print(isinstance(mgr_1, Employee))  # tells us if an instance is an object of a class
print(issubclass(Developer, Manager))  # tells us if a class is a subclass of another
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_2.prog_lang)
