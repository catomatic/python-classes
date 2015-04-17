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
        super(Animalia, self).__init__(**kwargs)

    def kingdom_info(self):
        """Returns information on this kingdom"""
        return '''
        Animals (kingdom Animalia) are eukaryotic and multicellular inhabitants 
        of planet Earth. {0} {1} is a member of this kingdom.
        '''.format(self.__class__.__name__, self.species)


class Chordata(Animalia):
    """Creates a Chordata"""
    def __init__(self, **kwargs):
        super(Chordata, self).__init__(**kwargs)

    def phylum_info(self):
        """Returns information on this phylum"""
        pass


class Vertebrata(Chordata):
    """Creates a Vertebrata"""
    def __init__(self, **kwargs):
        super(Vertebrata, self).__init__(**kwargs)

    def subphylum_info(self):
        """Returns information on this subphylum"""
        pass


class Reptilia(Vertebrata):
    """Creates a Reptilia"""
    def __init__(self, **kwargs):
        super(Reptilia, self).__init__(**kwargs)

    def class_info(self):
        """Returns information on this class"""
        pass


class Squamata(Reptilia):
    """Creates a Squamata"""
    def __init__(self, **kwargs):
        super(Squamata, self).__init__(**kwargs)

    def order_info(self):
        """Returns information on this order"""
        pass


class Serpentes(Squamata):
    """Creates a Serpentes"""
    def __init__(self, **kwargs):
        super(Serpentes, self).__init__(**kwargs)

    def suborder_info(self):
        """Returns information on this suborder"""
        pass


class Colubridae(Serpentes):
    """Creates a Colubridae"""
    def __init__(self, **kwargs):
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
        super(Lampropeltis, self).__init__(**kwargs)

    def genus_info(self):
        """Returns information on this genus"""
        pass

    def hierarchy(self):
        """Returns an arrow-separated hierarchy list"""
        names = reversed([i.__name__ for i in inspect.getmro(self.__class__)])
        return ' > '.join(names)

    def species_info(self):
        """Returns species"""
        return 'Species: {0}'.format(self.species)

    def common_name_info(self):
        """Returns common name"""
        return 'Common Name: {0}'.format(self.common_name)

    def colors_info(self):
        """Returns colors"""
        return 'Colors: {0}'.format(', '.join(self.colors))

    def geo_info(self):
        """Returns colors"""
        return 'Geographic Location: {0}'.format(self.geo_loc)


# pylint: disable=C0103
ks1 = Lampropeltis(species='getula getula',
    common_name='Eastern Chain Kingsnake',
    colors=['black', 'yellow', 'white'],
    geo_loc='United States East Coast')

print(ks1.hierarchy())
print(ks1.species_info())
print(ks1.common_name_info())
print(ks1.geo_info())
print(ks1.colors_info())
print(ks1.kingdom_info())
