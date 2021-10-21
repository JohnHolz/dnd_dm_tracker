import sys
sys.path.append('../../')
from jh_utils.utils.utils import print_dict, to_print_dict
from src.db_interact import read_db, write_db
party = 'FULL PARTY'
Party = 'FULL PARTY'
party_char_list = [Party]

line = '+----------------------------------------------------+'

class Event():
    def __init__(self, name, time, place, description=''):
        self.name = name
        self.time = time
        self.place = place
        self.description = {}
        if description != None:
            self.add_description('description',description)
    
    def __repr__(self):
        ret = f"""{self.name}
        → {self.place}
        → {self.time}
        {to_print_dict(self.description)}"""
        return ret

    def add_description(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + \
                [description_string]

    def get_json(self):
        ret = {}
        ret['name'] = self.name
        ret['time'] = self.time.__repr__()
        ret['place'] = self.place
        ret['description'] = self.description
        return ret

class Game():
    def __init__(self):
        self.events = {}
    
    def __repr__(self):
        ret = f'{line}'
        for i in self.events:
            ret = ret + f'\n{self.events[i]}{line}'
        return ret

    def add(self,event):
        self.events[event.name] = event

    def save_game(self, file_name=None):
        db = dict()
        for i in self.events:
            db[i] = self.events[i].get_json()
        write_db(db, file_name)

def load_game(file_path):
    ret = Game()
    db = read_db(file_path)
    for i in db:
        ret.add(Event(db[i]['name'],
                        db[i]['time'],
                        db[i]['place'],
                        db[i]['description']))
    return ret