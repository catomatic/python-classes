#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Flower Shop Ordering To Go - Create a Flower shop application which deals in
# Flower objects and use those Flower objects in a Bouquet object which can
# then be sold. Keep track of the number of objects and when you may need to
# order more.
# https://github.com/karan/Projects


class Flower(object):
    def __init__(self, name, color, fl_id, **kwargs):
        self.name = name
        self.color = color
        self.fl_id = fl_id
        super(Flower, self).__init__(**kwargs)

    def flower_info(self):
        return [self.name, self.color, self.fl_id]


class Bouquet(object):
    def __init__(self, name, qty, flowers, b_id, **kwargs):
        self.name = name
        self.b_id = b_id
        self.flowers = flowers
        self.qty = qty
        super(Bouquet, self).__init__(**kwargs)


fl1 = Flower(name='Rose', color='red', fl_id='r01')
fl2 = Flower(name='Rose', color='white', fl_id='r02')
fl3 = Flower(name='Rose', color='black', fl_id='r03')
fl4 = Flower(name='Dandelion', color='yellow', fl_id='d01')
fl5 = Flower(name='Tulip', color='pink', fl_id='t01')
fl6 = Flower(name='Tulip', color='red', fl_id='t02')
fl7 = Flower(name='Daisy', color='white', fl_id='da01')
fl8 = Flower(name='Gardenia', color='white', fl_id='g01')

print(fl1.flower_info())
print(fl2.flower_info())
print(fl3.flower_info())
print(fl4.flower_info())
print(fl5.flower_info())
print(fl6.flower_info())
print(fl7.flower_info())
print(fl8.flower_info())

print('-------------')

b1 = Bouquet(name='Birthday', qty=10, flowers=[fl1.flower_info(), 
    fl4.flower_info(), fl8.flower_info()], b_id='bb01')

print('Bouquet Name: {0}'.format(getattr(b1, 'name')))
print('Bouquet ID#: {0}'.format(getattr(b1, 'b_id')))
print('Bouquet Quantity: {0}'.format(getattr(b1, 'qty')))
print('Bouquet Contents: {0}'.format(getattr(b1, 'flowers')))

print('-------------')

# Find out if you need to reorder
print('Reorder?')
if getattr(b1, 'qty') < 20:
    print('reorder')
else:
    print('sufficient stock')

print('-------------')

# Sell bouquets
print('Sell a bouquet (1)')
setattr(b1, 'qty', (b1.qty-1))
print('Bouquet Quantity: {0}'.format(getattr(b1, 'qty')))

print('-------------')

# Add bouquets
print('Add more bouquets (11)')
setattr(b1, 'qty', (b1.qty+11))
print('Bouquet Quantity: {0}'.format(getattr(b1, 'qty')))

print('-------------')

print('Reorder?')
if getattr(b1, 'qty') < 20:
    print('reorder')
else:
    print('sufficient stock')
