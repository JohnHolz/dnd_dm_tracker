import sys
sys.path.append('../')
from world.time import DateTime
from world.places.places import Selgaunt
from characters.party import Vutar, Benio, Bushi, Aussyrk, Party

line = '\n+----------------------------------+\n'
party_char_list = [Vutar, Benio, Bushi, Aussyrk]

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
        if self.npcs==[]: 
            npcs = ''
        else:
            npcs=f'\n        npcs:{self.npcs}\n'
        ## mobs
        if self.mobs=={}: 
            mobs = ''
        else:
            mobs=f'\n        {self.mobs}\n'
        ## full party
        if self.full_party:
            party_show = f'Full Party'
        else:
            party_show = f'{self.chars}'

        ret = f"""{line}{self.time}
        → {self.place}
        → {party_show}{npcs}{mobs}{to_print_dict(self.info)}{line}
        """
        return ret

def evets(order):
    pass

def list_evets():
    pass