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


