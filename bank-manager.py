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


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = float(num) / 100
    return dec


class Account(object):
    def __init__(self, balance, int_rate, act_type, min_balance, **kwargs):
        self.balance = balance
        self.int_rate = int_rate
        self.act_type = act_type
        self.min_balance = min_balance
        super(Account, self).__init__(**kwargs)

    def __str__(self):
        # Charge $25 fee if balance drops below minimum
        if self.balance < self.min_balance:
            self.balance -= 25
        # Add interest
        self.balance += round(self.balance * pct_to_dec(self.int_rate), 2)
        return '{0}: ${1}'.format(self.act_type, self.balance)


class CheckingAccount(Account):
    def __init__(self, **kwargs):
        super(CheckingAccount, self).__init__(**kwargs)


class SavingsAccount(Account):
    def __init__(self, **kwargs):
        super(SavingsAccount, self).__init__(**kwargs)


class BusinessAccount(Account):
    def __init__(self, **kwargs):
        super(BusinessAccount, self).__init__(**kwargs)


ca1 = CheckingAccount(balance=500, int_rate=0.25, act_type='Checking Account', 
    min_balance=0)
sa1 = SavingsAccount(balance=50, int_rate=0.50, act_type='Savings Account', 
    min_balance=0)
ba1 = BusinessAccount(balance=4000, int_rate=0.75, act_type='Business Account', 
    min_balance=5000)

# Month #1 statement, initial deposits plus interest
print(ca1)
print(sa1)
print(ba1)

print('-------------')

# Month #2 statement plus interest

# Make deposit into checking
setattr(ca1, 'balance', (ca1.balance + 1000))
# Withdraw from checking
setattr(ca1, 'balance', (ca1.balance - 500))

# Make a deposit into savings
setattr(sa1, 'balance', (sa1.balance + 100))

print(ca1)
print(sa1)
print(ba1)

print('-------------')

# Month #3 statement plus interest

# Make deposit into checking
setattr(ca1, 'balance', (ca1.balance + 2500))
# Withdraw from checking
setattr(ca1, 'balance', (ca1.balance - 700))

# Make a deposit into savings
setattr(sa1, 'balance', (sa1.balance + 100))

# Make a deposit into business
setattr(ba1, 'balance', (ba1.balance + 1000))

print(ca1)
print(sa1)
print(ba1)
