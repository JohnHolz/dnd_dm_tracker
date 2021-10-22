import sys
sys.path.append('../')
from jh_utils.utils.utils import to_print_dict

class Core():
    def __init__(self,
                 ocupation=None,
                 race='human',
                 languages={'common': 'fluent'},
                 aligment='N',
                 background='soldier') -> None:
        self.ocupation = ocupation
        self.race = race
        self.languages = languages
        self.aligment = aligment
        self.background = background

    def __repr__(self) -> str:
        ret = f'''{self.race} - {self.ocupation} - {self.aligment}
{to_print_dict(self.languages)}
{self.background}'''
        return ret

    def get_dict(self):
        ret = dict()
        ret['ocupation'] = self.ocupation
        ret['race'] = self.race
        ret['languages'] = self.languages
        ret['aligment'] = self.aligment
        ret['background'] = self.background
        return ret


def dict_to_core(core_dict):
    ret = Core(ocupation=core_dict['ocupation'],
               race=core_dict['race'],
               languages=core_dict['languages'],
               aligment=core_dict['aligment'],
               background=core_dict['background'])
    return ret