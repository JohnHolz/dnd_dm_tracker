import sys
sys.path.append('../')
# from game.event import list_evets

line = '\n+-------------------+\n'

class Room():
    def __init__(self, name, where, description='', mob_group = None):
        self.name = name
        self.where = where
        self.description = []

        self.mobs = mob_group
        self.hidden = {}  # hidden info
        self.itens = []
        self.tags = []

    def __repr__(self):
        ret = f"""{self.name}
        where:       {self.where}
        description: {self.description}"""
        return ret

    # first updatable
    def add_description(self, string: str):
        self.description = f"""{self.description}
        {string}"""

    def add_tag(self, new_tag):
        self.tags = self.tags + [new_tag]

    # add to dictionaries
    def add_mob(self, mob_name, mob_count=1):
        self.mobs[mob_name] = mob_count

    def add_hidden(self, what_is_hidden, description):
        self.hidden[what_is_hidden] = description

    def add_itens(self, new_itens):
        if type(new_itens) == str:
            new_itens = [new_itens]
        self.itens = self.itens + new_itens

class Place():
    def __init__(self, name, where, what, lore=''):
        self.name = name
        self.where = where
        self.what = what
        self.npcs = {
            'core_npcs': [],
            'npcs': [],
            'other_npcs': []
        }
        self.rooms = {}
        self.other = {}
        self.description = {
            'lore': lore,
            'description': ''}
        self.tags = []

    def add_tag(self, new_tag):
        self.tags = self.tags + [new_tag]

    def __repr__(self):
        ret = f"""{self.name}\nwhere: {self.where}"""
        return ret

    # add npcs
    def add_npc(self, new_npc, npc_type='npcs'):
        if type(new_npc) == str:
            new_npc = [new_npc]
        self.npcs[npc_type] = self.npcs[npc_type]+new_npc

    # add room
    def add_room(self, room):
        self.rooms[room.name] = room

    def add_info(self, key, value):
        self.other[key] = value

    # add description
    def add_lore(self, string: str):
        self.description['lore'] = self.description['lore'] + \
            line+f"""\n {string}"""

    def add_description(self, string: str):
        self.description['description'] = self.description['description'] + \
            line+f"""\n {string}"""

class Urban():
    def __init__(self, name, subtitle, urban_type='village', description=''):
        self.name = name
        self.subtitle = subtitle
        self.urban_type = urban_type
        # intern places
        self.places = {}  # TODO function to list all places that have this as major place
        self.other = {}
        self.tags = []
        # npcs
        self.npcs = {
            'npcs_from_places': [],  # TODO function to list places
            'npcs': [],
            'other_npcs': []
        }
        # past events
        self.past = {
            'foundation': '',
            'lore': ''
        }
        # basic urban info
        self.urban_info = {
            'description': description,
            'social': '',
            'political': '',
            'economy': '',
            'religious': '',
            'military': '',
            'magical': '',
        }

    def __repr__(self):
        ret = f"""{self.name}, {self.subtitle}"""
        return ret

    def add_tag(self, new_tag):
        self.tags = self.tags + [new_tag]

    # update description and spermm
    def add_info(self, where: str = 'description', string: str = ''):
        self.urban_info[where] = self.urban_info[where]+line+string

    def add_past(self, where: str = 'lore', string: str = ''):
        self.past[where] = self.past[where]+line+string

    def add_place(self, place):
        self.places[place.name] = place

    def add_info(self, key: str, string: str):
        self.other[key] = string
