import sys
sys.path.append('../')
# from game.event import list_evets


class Room():
    def __init__(self, name, where, add_appearence_description=None, itens: list = []):
        self.name = name
        self.where = where
        self.description = {}
        self.hidden = {}  # hidden info
        self.itens = itens
        if add_appearence_description != None:
            self.description['appearence'] = add_appearence_description

    def __repr__(self):
        return f'{self.name} from {self.where}'

    def add_description(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + \
                [description_string]

    def add_hidden(self, what_is_hidden, description):
        self.hidden[what_is_hidden] = description

    def add_mob(self, mob_group):
        self.mobs = mob_group

    def add_itens(self, new_itens):
        if type(new_itens) == str:
            new_itens = [new_itens]
        self.itens = self.itens + new_itens


class Place():
    def __init__(self, name, where, place_type, appearence_description=None):
        self.name = name
        self.where = where
        self.place_type = place_type
        self.npcs = {
            'core_npcs': [],
            'npcs': [],
            'other_npcs': []
        }
        self.rooms = []
        self.description = {}
        if appearence_description != None:
            self.add_description('appearence', appearence_description)

    def __repr__(self):
        return f"""{self.name}, {self.place_type} - {self.where}"""

    # add npcs
    def add_npc(self, new_npc, npc_type='npcs'):
        if type(new_npc) == str:
            new_npc = [new_npc]
        self.npcs[npc_type] = self.npcs[npc_type]+new_npc

    def add_room(self, room):
        self.rooms = self.rooms + [room]

    def add_description(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + \
                [description_string]


class Urban():
    def __init__(self, name, subtitle, urban_type='village', description=''):
        self.name = name
        self.subtitle = subtitle
        self.urban_type = urban_type
        # intern places
        self.places = []  # TODO function to list all places that have this as major place
        self.other = {}
        # npcs
        self.npcs = {
            'npcs_from_places': [],  # TODO function to list places
            'npcs': [],
            'other_npcs': []
        }
        # basic urban info
        self.description = {
            'appearence': [],
            'social': [],
            'political': [],
            'economy': [],
            'religious': [],
            'military': [],
            'magical': [],
            'lore': [],
            'foundation': [],
        }

    def __repr__(self):
        ret = f"""{self.name}, {self.subtitle}"""
        return ret

    def add_description(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + \
                [description_string]
    
    def add_place(self, place):
        self.places = self.places + [place]

    def add_info(self, key: str, string: str):
        self.other[key] = string
