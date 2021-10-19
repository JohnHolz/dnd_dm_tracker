import sys
sys.path.append('../')
from jh_utils.utils.utils import to_print_dict
import json
party = 'FULL PARTY'
Party = 'FULL PARTY'
party_char_list = [Party]

line = '+----------------------------------------------------+'

## ! ###################
## ! Event class
class Event():
    def __init__(self, time, place, description='', party=True, npcs=[], chars=[]):
        self.time = time
        self.place = place
        self.npcs = npcs
        self.mobs = {}
        self.info = {
            'description':description
        }
        self.full_party = party
        if party:
            self.chars = party_char_list
            self.full_party = party
        else:
            self.chars = chars
    
    ## TODO add npc
    ## TODO add mobs
    ## TODO more description types
    ## TODO add description
    
    def __repr__(self):
        ## npcs
        npcs = '' if self.npcs==[] else f'\n        npcs:{self.npcs}\n'
        ## mobs
        mobs = '' if self.mobs=={} else f'\n        {self.mobs}\n'
        ## full party
        party_show = f'Full Party' if self.full_party else f'{self.chars}'

        ret = f"""{self.time}
        → {self.place}
        → {party_show}{npcs}{mobs}
        {to_print_dict(self.info)}"""
        return ret

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
    ## ! ###################
    ## ! Event class
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