#!/usr/bin/python
"""Products and Inventories"""

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Product Inventory Project - Create an application which manages an
# Inventory of products. Create a Product class which has a price, id,
# and quantity on hand. Then create an Inventory class which keeps
# track of various products and can sum up the Inventory value.
# https://github.com/karan/Projects

from __future__ import print_function


class Product(object):
    """Creates a Product"""
    def __init__(self, price, prod_id, qty, name, **kwargs):
        self.price = price
        self.prod_id = prod_id
        self.qty = qty
        self.name = name
        super(Product, self).__init__(**kwargs)

    def product_info(self):
        """Returns a list of product attributes"""
        return [self.price, self.prod_id, self.qty, self.name]


class Inventory(object):
    """Creates an Inventory"""
    def __init__(self, inv_id, name, products, **kwargs):
        self.inv_id = inv_id
        self.name = name
        self.products = products
        super(Inventory, self).__init__(**kwargs)


# pylint: disable=C0103
pf1 = Product(price=5.00, prod_id='fr01', qty=12, name='Apples')
pf2 = Product(price=3.00, prod_id='fr02', qty=13, name='Oranges')
pv1 = Product(price=2.00, prod_id='veg01', qty=8, name='Eggplant')

print(pf1.product_info())
print(pf2.product_info())
print(pv1.product_info())

print('-------------')

inv1 = Inventory(inv_id='inv01', name='Fruit', products=[])
print(inv1.name)

inv1.products.append(pf1.product_info())
inv1.products.append(pf2.product_info())

for each in inv1.products:
    print(each)

print('Total Value: {0}'.format(sum(i[0] for i in inv1.products)))

print('-------------')

inv2 = Inventory(inv_id='inv02', name='Vegetables', products=[])
print(inv2.name)

inv2.products.append(pv1.product_info())

for each in inv2.products:
    print(each)

print('Total Value: {0}'.format(sum(i[0] for i in inv2.products)))
