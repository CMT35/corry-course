def hello_func():
    return 'Hello Function!'


print(hello_func().upper())


# Pass arguments
def hello(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello('Hi', name='Chris'))


# Positional Keywords argument
def student_info(*args, **kwargs):  # Allows us to include arbitrary number of keywords arguments
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

# Example (check if its a leap year)
# Number of days per month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month"""

    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return month_days(month)


print(is_leap(2020))
print(days_in_month(2020, 2))
