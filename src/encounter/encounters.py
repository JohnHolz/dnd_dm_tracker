from os import write
from db_interact import read_db, write_db
from small.coin import Money
import sys
sys.path.append('../')


class Encounter():
    def __init__(self, name):
        self.name = name
        self.location = []
        self.plot = ''
        self.description = {}
        self.rewards = {'money': Money(0, 0, 0, 0, 0),
                        'common_itens': [],
                        'magical_items': []}

    def __repr__(self):
        ret = f'''{self.name} - {self.location} \n{self.rewards} \n{self.plot}'''
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
        self.rewards['magical_items'] = self.rewards['magical_items'] + \
            [magical_item]

    # ! add information
    def add_info(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + \
                [description_string]

    # ! set plot
    def set_plot(self, new_plot):
        self.plot = self.name + f'\n{new_plot}'

    # ! save
    def get_json(self):
        ret = dict()
        ret['name'] = self.name
        ret['location'] = self.location
        ret['plot'] = self.plot
        ret['description'] = self.description
        ret['rewards'] = self.rewards
        return ret

    def save_encounter(self, path):
        db = read_db(path)
        db[self.name] = self.get_json()
        write_db(db, path)


def get_encounter(encounter_name, path):
    db = read_db(path)
    encounter_dict = db[encounter_name]
    encounter = Npc()
    encounter.name = encounter_dict['name']
    encounter.core = encounter_dict['core']
    encounter.combat = encounter_dict['combat']
    encounter.drives = encounter_dict['drives']
    encounter.connections = encounter_dict['connections']
    return encounter