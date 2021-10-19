import sys
sys.path.append('../')
from core.coin import Money

class Encounter():
    def __init__(self, name,first_idea):
        self.first_idea = first_idea
        self.name = name
        self.location = []
        self.monsters = {}
        self.npcs = {}
        self.plot = ''
        self.rewards = {'money':Money(0,0,0,0,0),
                        'common_itens':[],
                        'magical_items':[]}
    
    def __repr__(self):
        ret = f'''{self.name} - {self.location}
{self.monsters}
{self.rewards}
{self.plot}'''
        return ret

    ## ! location
    def add_location(self, location):
        self.location = self.location + [location]

    ## ! npcs
    def add_npc(self, npc, text):
        ret = f'self.npcs["{npc}"] = "{text}"'
        exec(ret)

    def rm_npc(self, npc):
        ret = f'del r["{npc}"]'
        exec(ret)

    def add_mob_group(self, mob_group):
        self.monsters = mob_group

    ## ! rewards
    def add_item(self, item):
        self.rewards['common_itens'] = self.rewards['common_itens'] + [item]

    def add_magical_item(self, magical_item):
        self.rewards['magical_items'] = self.rewards['magical_items'] + [magical_item]

    ## ! plot
    def add_info(self, new_info):
        self.plot = self.plot + f'\n{new_info}'
    
    def set_plot(self, new_plot):
        self.plot = self.name + f'\n{new_plot}'

def create_encounter(encounter_name,
                     location,
                     monsters,
                     npcs,
                     plot,
                     rewards,
                     first_idea = ''):
    encounter = Encounter(encounter_name,
                          first_idea)
    encounter.add_location(location)
    encounter.add_mob_group(monsters)
    encounter.npcs = npcs
    encounter.rewards = rewards
    encounter.plot = plot
    return Encounter