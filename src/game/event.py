import sys
sys.path.append('../')
from jh_utils.utils.utils import to_print_dict
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
        {self.description}"""
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
        ret['npcs'] = self.npcs
        ret['info'] = self.info
        ret['chars'] = self.chars
        return ret

class Game():
    def __init__(self):
        self.events = []
    
    def __repr__(self):
        ret = f'{line}'
        for i in self.events:
            ret = ret + f'\n{i}{line}'
        return ret

    def add(self,event):
        self.events.append(event)

    def save_game(self, cicle_name, relative_path=None):
        import pandas as pd
        events_list = list(map(lambda x: x.get_json(), self.events))
        pd.DataFrame(events_list).to_json(f'{relative_path}events_{cicle_name}.json',orient='records',lines=True)

def load_game(file_path):
    ret = Game()
    event_list = file_path ## TODO read event list function
    ret.events = event_list
    return ret