#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Product Inventory Project - Create an application which manages an 
# inventory of products. Create a product class which has a price, id, 
# and quantity on hand. Then create an inventory class which keeps 
# track of various products and can sum up the inventory value.

import traceback
import sys


class product:

    def __init__(self, price, prod_id, qty, name):
        self.price = price
        self.prod_id = prod_id
        self.qty = qty
        self.name = name

    def product_info(self):
        return self.price, self.prod_id, self.qty, self.name


class inventory:
    __products_list = []

    def add_prod(self, prod):
        inventory.__products_list.append(prod.product_info())

    def del_prod(self, prod):
        inventory.__products_list.remove(prod.product_info())

    def show_inventory(self):
        for each in inventory.__products_list:
            print each

    def total_inventory(self):
        __total = []
        for each in inventory.__products_list:
            __total.append(each[2])
        print 'Total inventory: {0}'.format(sum(__total))

    def total_inventory_value(self):
        __total_value = []
        for each in inventory.__products_list:
            __total_value.append(each[0])
        print 'Total inventory value: ${0}'.format(sum(__total_value))


def main():
    try:
        track_inventory = inventory()

        p1 = product(5.00, 1234, 12, 'Apples')
        track_inventory.add_prod(p1)

        p2 = product(3.00, 4321, 13, 'Oranges')
        track_inventory.add_prod(p2)

        track_inventory.show_inventory()
        track_inventory.total_inventory()
        track_inventory.total_inventory_value()

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
