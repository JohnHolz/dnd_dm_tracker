import sys
sys.path.append('../')
from core.coin import Money
from numpy.random import randint

races = ['High Elf',
         'Wood Elf',
         'Half High Elf', 
         'Half Wood Elf',
         'Montain Dwarf', 
         'Hill Dwarf', 
         'Human', 
         'Leonin', 
         'Halfings']#,
#         'Drow']

classes = ['novice','novice','guard','veteran']

def sample(vec):
    return vec[randint(len(vec))]

class Char():
    def __init__(self,
                 name,
                 money=Money(0, 0, 0, 31, 0),
                 dnd_class=sample(classes),
                 race=sample(races), lvl=randint(1,6)):
        self.name = name
        self.money = money
        self.dnd_class = dnd_class
        self.race = race
        self.lvl = lvl

    def __repr__(self) -> str:
        ret = f"""{self.name} -  {self.race}:{self.dnd_class}"""
        return ret



class Char():
    def __init__(self, nome):
        self.nome = nome
        self.connection = {}
    
    def def_core(self, 
             rpg_class, 
             lvl, 
             race, 
             subrace, 
             alignment, 
             background, 
             flaws={}, 
             languages={'common':'fluent'}, 
             subclass=None, 
             xp=0):
        self.rpg_class = rpg_class
        self.lvl = lvl
        self.race = race
        self.subrace = subrace
        self.alignment = alignment
        self.background = background
        self.flaws = flaws
        self.languages = languages
        self.subclass = subclass
        self.xp = xp

    def def_appearance(self,
                   age,
                   height,
                   weight,
                   skin,
                   eyes,
                   hair = None,
                   size = 'Medium'):
        self.appearance = {
            'age': age,
            'height': height,
            'weight': weight,
            'skin': skin,
            'eyes': eyes,
            'hair': hair,
            'size': size,
        }

    def add_connection(self, new_connection, connection_description = ''):
        self.connection[new_connection] = connection_description
