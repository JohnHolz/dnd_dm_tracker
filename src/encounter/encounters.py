from db_interact import read_db, write_db
from jh_utils.utils.utils import to_print_dict, to_print_list
from small.coin import Money, list_to_money
import sys
sys.path.append('../')


class Encounter():
    def __init__(self, name=None):
        self.name = name
        self.location = []
        self.plot = ''
        self.description = {}
        self.rewards = {'money': Money(0, 0, 0, 0, 0),
                        'common_itens': [],
                        'magical_items': []}

    def __repr__(self):
        ret = f'''{self.name} - {self.location}\n{to_print_dict(self.rewards)} \n{self.plot}'''
        return ret

    # ! location
    def add_location(self, location):
        self.location = self.location + [location]

    # ! rewards
    def add_money(self, money):
        self.rewards['money'] = self.rewards['money'] + money

    def add_item(self, item):
        self.rewards['common_itens'] = self.rewards['common_itens'] + [item]

    def add_magical_item(self, magical_item):
        self.rewards['magical_items'] = self.rewards['magical_items'] + [magical_item]

    # ! add information
    def add_info(self, key, value):
        self.description[key] = value

    # ! set plot
    def set_plot(self, new_plot):
        self.plot = self.name + f'\n{new_plot}'

    def reward_json(self):
        ret = dict()
        for i in self.rewards:
            ret[i] = self.rewards[i]
        ret['money']=self.rewards['money'].get_list()
        return ret

    # ! save
    def get_json(self):
        ret = dict()
        ret['name'] = self.name
        ret['location'] = self.location
        ret['plot'] = self.plot
        ret['description'] = self.description
        ret['rewards'] = self.reward_json()
        return ret

    def save_encounter(self, path):
        db = read_db(path)
        db[self.name] = self.get_json()
        write_db(db, path)


def get_encounter(encounter_name, path):
    db = read_db(path)
    encounter_dict = db[encounter_name]
    encounter = Encounter()
    encounter.name = encounter_dict['name']
    encounter.location = encounter_dict['location']
    encounter.plot = encounter_dict['plot']
    encounter.description = encounter_dict['description']
    encounter.rewards = encounter_dict['rewards']
    encounter.rewards['money'] = list_to_money(encounter.rewards['money'])
    return encounter