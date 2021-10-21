import sys
sys.path.append('../')
from jh_utils.utils.utils import print_dict, to_print_dict
from db_interact import read_db, write_db
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
        ret['index'] = self.time.__repr__().replace(' ','-')+self.place.__repr__().replace(' ','-')
        ret['time'] = self.time
        ret['place'] = self.place
        ret['description'] = self.description
        return ret

class Game():
    def __init__(self):
        self.events = {}
    
    def __repr__(self):
        ret = f'{line}'
        for i in self.events:
            ret = ret + f'\n{self.events[i]}\n{line}'
        return ret

    def add(self,event):
        self.events[event.name] = event

    def save_game(self, file_name=None):
        events_list = {}
        for i in self.events:
            events_list[i.name] = i.get_json()
        write_db(events_list, file_name)

def load_game(file_path):
    ret = Game()
    ret.events = read_db(file_path)
    return ret