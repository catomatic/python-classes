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

import sys
import traceback
import itertools


class Flower:

    def __init__(self, fl_id, name):
        self.name = name
        # Set a Flower id in case it's needed in the future
        self.fl_id = fl_id

    def flower_info(self):
        return self.name


class Bouquet:
    bouquet_inventory = []
    bouquet_onhand = {}

    def create_bouquet(self, *fl):
        new_bouquet = []
        new_bouquet.extend(fl)
        Bouquet.bouquet_inventory.append(list(itertools.chain.from_iterable(new_bouquet)))
        Bouquet.bouquet_onhand.update({fl[0][0]: 1})

    def sell_bouquet(self, b_id, amt):
        for k, v in Bouquet.bouquet_onhand.iteritems():
            if v <= 0 or v - amt < 0:
                print "Can't sell any more {0}.".format(k)
            elif v - amt < 0:
                print "Not enough stock to sell {0} {1}.".format(amt, k)
            else:
                Bouquet.bouquet_onhand.update({b_id: v - amt})

    def add_bouquet(self, b_id, amt):
        for k, v in Bouquet.bouquet_onhand.iteritems():
            Bouquet.bouquet_onhand.update({b_id: v + amt})

    def show_bouquets(self):
        print 'Catalogue:'
        for each in Bouquet.bouquet_inventory:
            print '{0}'.format(each)
        print 'Quantity on hand:'
        for k, v in Bouquet.bouquet_onhand.iteritems():
            print '{0}: {1}'.format(k, v)
            if v <= 1:
                print 'Need to reorder {0}.'.format(k)


def main():
    try:
        manage_bouquets = Bouquet()

        f1 = Flower('f1', 'Red Rose')
        f2 = Flower('f2', 'White Lily')
        f3 = Flower('f3', 'Yellow Lily')
        f4 = Flower('f4', 'Pink Rose')
        f5 = Flower('f5', 'Dandelion')
        f6 = Flower('f6', 'Black Tulip')
        f7 = Flower('f7', 'Red Tulip')
        f8 = Flower('f8', 'White Daisy')

        # Create the initial bouquets w/ default qty
        manage_bouquets.create_bouquet(['b1'], [f1.flower_info(), f2.flower_info(), f5.flower_info()])
        manage_bouquets.create_bouquet(['b2'], [f6.flower_info(), f8.flower_info()])
        manage_bouquets.create_bouquet(['b3'], [f7.flower_info(), f3.flower_info(), f4.flower_info()])

        # Show the catalogue with default qtys
        manage_bouquets.show_bouquets()

        print '------------'

        # Adding and selling bouquets
        manage_bouquets.sell_bouquet('b1', 1)
        manage_bouquets.add_bouquet('b2', 3)
        manage_bouquets.sell_bouquet('b3', 3)

        print '------------'

        # Updated catalogue
        manage_bouquets.show_bouquets()

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
