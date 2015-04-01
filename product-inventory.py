#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Product Inventory Project - Create an application which manages an
# Inventory of products. Create a Product class which has a price, id,
# and quantity on hand. Then create an Inventory class which keeps
# track of various products and can sum up the Inventory value.
# https://github.com/karan/Projects


class Product:

    def __init__(self, price, prod_id, qty, name):
        self.price = price
        self.prod_id = prod_id
        self.qty = qty
        self.name = name

    def product_info(self):
        return self.price, self.prod_id, self.qty, self.name


class Inventory:
    products_list = []

    def add_prod(self, prod):
        Inventory.products_list.append(prod.product_info())

    def del_prod(self, prod):
        Inventory.products_list.remove(prod.product_info())

    def show_inventory(self):
        for each in Inventory.products_list:
            print(each)

    def total_inventory(self):
        total = []
        for each in Inventory.products_list:
            total.append(each[2])
        print('Total Inventory: {0}'.format(sum(total)))

    def total_inventory_value(self):
        total_value = []
        for each in Inventory.products_list:
            total_value.append(each[0])
        print('Total Inventory value: ${0}'.format(sum(total_value)))


track_inventory = Inventory()

p1 = Product(5.00, 1234, 12, 'Apples')
track_inventory.add_prod(p1)

p2 = Product(3.00, 4321, 13, 'Oranges')
track_inventory.add_prod(p2)

track_inventory.show_inventory()
track_inventory.total_inventory()
track_inventory.total_inventory_value()
