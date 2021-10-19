import sys
sys.path.append('../')
from world.party import Party
from jh_utils.utils.utils import to_print_dict

party_char_list = []

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
        → {party_show}{npcs}{mobs}{to_print_dict(self.info)}"""
        return ret
