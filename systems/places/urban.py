line = '\n+-------------------+\n'


class Urban():
    def __init__(self, name, subtitle, urban_type='village', description=''):
        self.name = name
        self.subtitle = subtitle
        self.urban_type = urban_type
        # intern places
        self.places = {}  # TODO function to list all places that have this as major place
        self.events = {}  # TODO function to list all events envolving this major place
        self.other = {}
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
        ret = f"""
        {self.name}
            {self.subtitle}
            {self.urban_type}
        """
        return ret

    # update description and spermm
    def add_info(self, where: str = 'description', string: str = ''):
        self.urban_info[where] = self.urban_info[where]+line+string

    def add_past(self, where: str = 'lore', string: str = ''):
        self.past[where] = self.past[where]+line+string

    def add_place(self, place):
        self.places[place.name] = place
    # def add_event(self, event):
    #     self.events[event.name] = event

    def add_info(self, key: str, string: str):
        self.other[key] = string
