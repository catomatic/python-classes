#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Bank Account Manager - Create a class called Account which will be an abstract 
# class for three other classes called CheckingAccount, SavingsAccount and 
# BusinessAccount. Manage credits and debits from these accounts through an ATM 
# style program.

import sys
import traceback
from abc import ABCMeta, abstractmethod


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = float(num) / 100
    return dec


class account:
    __metaclass__ = ABCMeta

    def __init__(self, balance):
        self.balance = balance

    def credit(self, amount):
        self.balance += amount

    @abstractmethod
    def debit(self):
        return self.balance

    def add_interest(self, int_rate):
        self.balance = self.balance * pct_to_dec(int_rate) + self.balance

    @abstractmethod
    def account_info(self):
        return '${0}'.format(self.balance)


class checking_account(account):

    def __init__(self):
        self.balance = 0

    def debit(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 35
            print 'You have been charged an overdraft fee.'

    def account_info(self):
        x = super(checking_account, self).account_info()
        return '{0}'.format(x)


class savings_account(account):

    def __init__(self):
        self.balance = 0

    def debit(self, amount):
        if self.balance <= 0:
            print 'Balance too low.'
        elif self.balance - amount < 0:
            print 'Debit amount too high.'
        else:
            self.balance -= amount

    def account_info(self):
        x = super(savings_account, self).account_info()
        return '{0}'.format(x)


class business_account(account):
    min_balance = 5000

    def __init__(self):
        self.balance = 5000

    def debit(self, amount):
        if self.balance - amount < business_account.min_balance:
            print 'Must maintain ${0} minimum balance'.format(business_account.min_balance)
        else:
            self.balance -= amount

    def account_info(self):
        x = super(business_account, self).account_info()
        return '{0}'.format(x)


def main():
    try:
        ca1 = checking_account()
        ca1.type = 'Checking Account'
        print ca1.type
        print ca1.account_info()
        ca1.credit(100)
        print ca1.account_info()
        ca1.credit(100)
        print ca1.account_info()
        ca1.credit(500)
        print ca1.account_info()
        ca1.debit(100)
        print ca1.account_info()
        ca1.debit(700)
        print ca1.account_info()
        ca1.credit(500)
        print ca1.account_info()

        print '-------------'

        sa1 = savings_account()
        sa1.type = 'Savings Account'
        print sa1.type
        print sa1.account_info()
        sa1.credit(5000)
        print sa1.account_info()
        sa1.add_interest(3)
        print sa1.account_info()
        sa1.add_interest(3)
        print sa1.account_info()
        sa1.credit(100)
        print sa1.account_info()
        sa1.debit(600)
        print sa1.account_info()
        sa1.debit(5000)
        print sa1.account_info()
        sa1.debit(4804.5)
        print sa1.account_info()
        sa1.debit(100)
        print sa1.account_info()
        sa1.credit(5000)
        print sa1.account_info()

        print '-------------'

        ba1 = business_account()
        ba1.type = 'Business Account'
        print ba1.type
        print ba1.account_info()
        ba1.credit(1000)
        print ba1.account_info()
        ba1.debit(2000)
        print ba1.account_info()
        ba1.add_interest(3)
        print ba1.account_info()

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
