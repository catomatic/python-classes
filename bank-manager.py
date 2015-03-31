#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Bank Account Manager - Create a class called Account which will be an abstract
# class for three other classes called CheckingAccount, SavingsAccount and
# BusinessAccount. Manage credits and debits from these accounts through an ATM
# style program.
# https://github.com/karan/Projects

import sys
import traceback


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = float(num) / 100
    return dec


class Account:    

    def __init__(self, balance):
        self.balance = balance

    def credit(self, amount):
        self.balance += amount

    def debit(self):
        return self.balance

    def add_interest(self, int_rate):
        self.balance = self.balance * pct_to_dec(int_rate) + self.balance

    def __str__(self):
        return '${0}'.format(self.balance)


class CheckingAccount(Account):

    def __init__(self):
        self.balance = 0

    def debit(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 35
            print 'You have been charged an overdraft fee.'


class SavingsAccount(Account):

    def __init__(self):
        self.balance = 0

    def debit(self, amount):
        if self.balance <= 0:
            print 'Balance too low.'
        elif self.balance - amount < 0:
            print 'Debit amount too high.'
        else:
            self.balance -= amount


class BusinessAccount(Account):
    min_balance = 5000

    def __init__(self):
        self.balance = 5000

    def debit(self, amount):
        if self.balance - amount < BusinessAccount.min_balance:
            print 'Must maintain ${0} minimum balance'.format(BusinessAccount.min_balance)
        else:
            self.balance -= amount


def main():
    try:
        ca1 = CheckingAccount()
        ca1.type = 'Checking Account'
        print ca1.type
        print ca1
        ca1.credit(100)
        print ca1
        ca1.credit(100)
        print ca1
        ca1.credit(500)
        print ca1
        ca1.debit(100)
        print ca1
        ca1.debit(700)
        print ca1
        ca1.credit(500)
        print ca1

        print '-------------'

        sa1 = SavingsAccount()
        sa1.type = 'Savings Account'
        print sa1.type
        print sa1
        sa1.credit(5000)
        print sa1
        sa1.add_interest(3)
        print sa1
        sa1.add_interest(3)
        print sa1
        sa1.credit(100)
        print sa1
        sa1.debit(600)
        print sa1
        sa1.debit(5000)
        print sa1
        sa1.debit(4804.5)
        print sa1
        sa1.debit(100)
        print sa1
        sa1.credit(5000)
        print sa1

        print '-------------'

        ba1 = BusinessAccount()
        ba1.type = 'Business Account'
        print ba1.type
        print ba1
        ba1.credit(1000)
        print ba1
        ba1.debit(2000)
        print ba1
        ba1.add_interest(3)
        print ba1

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
