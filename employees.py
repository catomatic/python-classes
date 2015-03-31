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

import sys
import traceback


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = float(num) / 100
    return dec


class Employee:    
    def __init__(self, total_pay):
        self.total_pay

    def __str__(self):
        return 'Total pay: {0}'.format(self.total_pay)


class HourlyEmployee(Employee):
    def __init__(self, pay_hour, bonus, wk_hours, pay_raise):
        base_year = (pay_hour * wk_hours) * 52
        give_raise = (base_year * pct_to_dec(pay_raise)) + base_year
        self.total_pay = give_raise + bonus


class SalariedEmployee(Employee):
    def __init__(self, pay_year, bonus, pay_raise):
        give_raise = (pay_year * pct_to_dec(pay_raise)) + pay_year
        self.total_pay = give_raise + bonus


class Manager(Employee):
    def __init__(self, pay_year, bonus, pay_raise):
        give_raise = (pay_year * pct_to_dec(pay_raise)) + pay_year
        self.total_pay = give_raise + bonus


class Executive(Employee):
    def __init__(self, pay_year, bonus, pay_raise):
        give_raise = (pay_year * pct_to_dec(pay_raise)) + pay_year
        self.total_pay = give_raise + bonus


class company:
    __status_hired = []
    __status_fired = []

    def hired(self, emp_name):
        company.__status_hired.append(emp_name)

    def fired(self, emp_name):
        company.__status_fired.append(emp_name)
        company.__status_hired.remove(emp_name)

    def show_status_hired(self):
        print 'Hired:'
        for each in company.__status_hired:
            print '{0}'.format(each)

    def show_status_fired(self):
        print 'Fired:'
        for each in company.__status_fired:
            print '{0}'.format(each)


def main():
    try:
        company_stuff = company()

        he1 = HourlyEmployee(12, 1000, 30, 5)
        he1.emp_name = 'Mittens'
        he1.emp_type = 'Hourly Employee'
        print he1.emp_name
        print he1.emp_type
        print he1
        company_stuff.hired(he1.emp_name)
        print '-------------'

        he2 = HourlyEmployee(12, 0, 30, 0)
        he2.emp_name = 'Chirpy'
        he2.emp_type = 'Hourly Employee'
        print he2.emp_name
        print he2.emp_type
        print he2
        he2.bonus = 200
        he2.pay_raise = 5
        print he2
        company_stuff.hired(he2.emp_name)
        print '-------------'

        se1 = SalariedEmployee(45000, 500, 2)
        se1.emp_name = 'Fluffy'
        se1.emp_type = 'Salaried Employee'
        print se1.emp_name
        print se1.emp_type
        print se1
        company_stuff.hired(se1.emp_name)
        print '-------------'

        m1 = Manager(80000, 2000, 1)
        m1.emp_name = 'Flipper'
        m1.emp_type = 'Manager'
        print m1.emp_name
        print m1.emp_type
        print m1
        company_stuff.hired(m1.emp_name)
        print '-------------'

        ex1 = Executive(120000, 10000, 5)
        ex1.emp_name = 'Rufus'
        ex1.emp_type = 'Executive'
        print ex1.emp_name
        print ex1.emp_type
        print ex1
        company_stuff.hired(ex1.emp_name)
        print '-------------'

        company_stuff.show_status_hired()
        company_stuff.show_status_fired()
        company_stuff.fired(he1.emp_name)

        print '-------------'
        company_stuff.show_status_hired()
        company_stuff.show_status_fired()
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
