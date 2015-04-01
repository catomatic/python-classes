#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Company Manager - Create an hierarchy of classes - abstract class Employee
# and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every
# one's pay is calculated differently, research a bit about it. After you've
# established an employee hierarchy, create a Company class that allows you to
# manage the employees. You should be able to hire, fire and raise employees.
# https://github.com/karan/Projects


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = float(num) / 100
    return dec


class Employee(object):
    def __init__(self, emp_name, emp_type, bonus, pay_raise, **kwargs):
        self.emp_name = emp_name
        self.emp_type = emp_type
        self.bonus = bonus
        self.pay_raise = pay_raise
        super(Employee, self).__init__(**kwargs)

    def employee_name(self):
        return 'Employee Name: {0}'.format(self.emp_name)

    def employee_type(self):
        return 'Employee Type: {0}'.format(self.emp_type)

    def year_to_date(self):
        give_raise = (self.pay_year * pct_to_dec(self.pay_raise)) + self.pay_year
        self.total_pay = give_raise + self.bonus
        return 'Total Pay: {0}'.format(self.total_pay)


class HourlyEmployee(Employee):
    def __init__(self, pay_hour, wk_hours, **kwargs):
        self.pay_hour = pay_hour
        self.wk_hours = wk_hours
        super(HourlyEmployee, self).__init__(**kwargs)

    def year_to_date(self):
        base_year = (self.pay_hour * self.wk_hours) * 52
        give_raise = (base_year * pct_to_dec(self.pay_raise)) + base_year
        self.total_pay = give_raise + self.bonus
        return 'Total Pay: {0}'.format(self.total_pay)


class SalariedEmployee(Employee):
    def __init__(self, pay_year, **kwargs):
        self.pay_year = pay_year
        super(SalariedEmployee, self).__init__(**kwargs)


class Manager(Employee):
    def __init__(self, pay_year, **kwargs):
        self.pay_year = pay_year
        super(Manager, self).__init__(**kwargs)


class Executive(Employee):
    def __init__(self, pay_year, **kwargs):
        self.pay_year = pay_year
        super(Executive, self).__init__(**kwargs)


class Company:
    status_hired = []
    status_fired = []

    def hired(self, emp_name):
        Company.status_hired.append(emp_name)

    def fired(self, emp_name):
        Company.status_fired.append(emp_name)
        Company.status_hired.remove(emp_name)

    def show_status_hired(self):
        print('Hired:')
        for each in Company.status_hired:
            print('{0}'.format(each))

    def show_status_fired(self):
        print('Fired:')
        for each in Company.status_fired:
            print('{0}'.format(each))


company_stuff = Company()

he1 = HourlyEmployee(pay_hour=10.00, bonus=2000, wk_hours=20, 
    pay_raise=2.00, emp_name='Fluffy', emp_type='Hourly Employee')
company_stuff.hired(he1.employee_name())
print(he1.employee_name())
print(he1.employee_type())
print(he1.year_to_date())

print('-------------')

se1 = SalariedEmployee(emp_name='Mittens', emp_type='Salaried Employee', 
    bonus=5000, pay_raise=2.0, pay_year=35000)
company_stuff.hired(se1.employee_name())
print(se1.employee_name())
print(se1.employee_type())
print(se1.year_to_date())

print('-------------')

m1 = Manager(emp_name='Chirpy', emp_type='Manager', 
    bonus=7000, pay_raise=3.5, pay_year=50000)
company_stuff.hired(m1.employee_name())
print(m1.employee_name())
print(m1.employee_type())
print(m1.year_to_date())
company_stuff.fired(m1.employee_name())

print('-------------')

e1 = Manager(emp_name='Snowball', emp_type='Executive', 
    bonus=10000, pay_raise=5.0, pay_year=100000)
company_stuff.hired(e1.employee_name())
print(e1.employee_name())
print(e1.employee_type())
print(e1.year_to_date())

print('-------------')

company_stuff.show_status_hired()

print('-------------')

company_stuff.show_status_fired()
