import sys
sys.path.append('../')
line = '\n+-------------------+\n'

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
