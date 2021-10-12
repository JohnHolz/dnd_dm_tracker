class Urban():
    def __init__(self, name, type, lore=''):
        self.name = name
        self.type = type
        self.lore = lore
        self.type_info = place_types[type]

    def __repr__(self):
        ret = f"""
        date: {self.time}
        where: {self.location}
        npcs: {self.npcs}
        chars: {self.chars}
        {self.info}
        """
        return ret

class Place():
    def __init__(self, name, type, lore=''):
        self.name = name
        self.type = type
        self.lore = lore
        self.type_info = place_types[type]

    def __repr__(self):
        ret = f"""
        date: {self.time}
        where: {self.location}
        npcs: {self.npcs}
        chars: {self.chars}
        {self.info}
        """
        return ret

religius_place = {
    'deiti': '',
    'itens': '',
}

military_place = {
    'itens': '',
}

urban_place = {'Social': '',
               'Political': '',
               'Economical': '',
               'Religious': '',
               'Military': '',
               'Magical': '', }

campaing_place = {
    'npcs':[],
}

place_types = {
        ## @ urban/human places
         'city': urban_place.copy(),
         'village': urban_place.copy(),
        ## @ random campaing place
         'farm-village':'',
         'temple': religius_place.copy(),
         'fort': military_place.copy(),
         'monument': military_place.copy(),
        ## @ random places        
         'dungeon':'',
         'cave':'',
}
