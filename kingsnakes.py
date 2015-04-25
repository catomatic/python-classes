#!/usr/bin/python
"""A long class inheritance chain from Animalia to Lampropeltis"""

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# An example of a long chain of inheritance, just messing around
# I've left out some things like clade, subfamily, tribe for simplification

from __future__ import print_function
import inspect


class Animalia(object):
    """Creates an Animalia"""
    def __init__(self, **kwargs):
        self.kingdom_name = self.__class__.__name__
        super(Animalia, self).__init__(**kwargs)

    @staticmethod
    def kingdom_info(*args):
        """Returns information on this kingdom"""
        return '''
        Animals (kingdom Animalia) are eukaryotic and multicellular inhabitants 
        of planet Earth. {0} is a member of this kingdom.
        '''.format(' '.join(args))


class Chordata(Animalia):
    """Creates a Chordata"""
    def __init__(self, **kwargs):
        self.phylum_name = self.__class__.__name__
        super(Chordata, self).__init__(**kwargs)

    def phylum_info(self):
        """Returns information on this phylum"""
        pass


class Vertebrata(Chordata):
    """Creates a Vertebrata"""
    def __init__(self, **kwargs):
        self.subphylum_name = self.__class__.__name__
        super(Vertebrata, self).__init__(**kwargs)

    def subphylum_info(self):
        """Returns information on this subphylum"""
        pass


class Reptilia(Vertebrata):
    """Creates a Reptilia"""
    def __init__(self, **kwargs):
        self.class_name = self.__class__.__name__
        super(Reptilia, self).__init__(**kwargs)

    def class_info(self):
        """Returns information on this class"""
        pass


class Squamata(Reptilia):
    """Creates a Squamata"""
    def __init__(self, **kwargs):
        self.order_name = self.__class__.__name__
        super(Squamata, self).__init__(**kwargs)

    def order_info(self):
        """Returns information on this order"""
        pass


class Serpentes(Squamata):
    """Creates a Serpentes"""
    def __init__(self, **kwargs):
        self.suborder_name = self.__class__.__name__
        super(Serpentes, self).__init__(**kwargs)

    def suborder_info(self):
        """Returns information on this suborder"""
        pass


class Colubridae(Serpentes):
    """Creates a Colubridae"""
    def __init__(self, **kwargs):
        self.family_name = self.__class__.__name__
        super(Colubridae, self).__init__(**kwargs)

    def family_info(self):
        """Returns information on this family"""
        pass


class Lampropeltis(Colubridae):
    """Creates a Lampropeltis"""
    def __init__(self, species, common_name, colors, geo_loc, **kwargs):
        self.species = species
        self.common_name = common_name
        self.colors = colors
        self.geo_loc = geo_loc
        self.genus_name = self.__class__.__name__
        super(Lampropeltis, self).__init__(**kwargs)

    def genus_info(self):
        """Returns information on this genus"""
        pass

    def hierarchy(self):
        """Returns an arrow-separated hierarchy list"""
        names = reversed([i.__name__ for i in inspect.getmro(self.__class__)])
        return ' > '.join(names)


# pylint: disable=C0103
generic_animal = Animalia()
generic_reptile = Reptilia()

ks1 = Lampropeltis(species='getula getula',
    common_name='Eastern Chain Kingsnake',
    colors=['black', 'yellow', 'white'],
    geo_loc='United States East Coast')

print(ks1.hierarchy())
print('Species: {0}'.format(ks1.species))
print('Common Name: {0}'.format(ks1.common_name))
print('Geographic Location: {0}'.format(ks1.geo_loc))
print('Colors: {0}'.format(', '.join(ks1.colors)))
print(ks1.kingdom_info(ks1.genus_name, ks1.species))

print(generic_animal.kingdom_info('Generic animal'))
print(generic_reptile.kingdom_info('Generic reptile'))
