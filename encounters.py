from monetary_system import Money

class Encounter():
    def __init__(self, first_idea):
        self.first_idea = first_idea
        self.name = ''
        self.locaton = []
        self.monsters = {'order1':[],'boss':[]}
        self.npcs = {}
        self.plot = ''
        self.rewards = {'money':Money(0,0,0,0,0)}
    
    """
    @ name - String
    @ location - vector
    @ monsters - dict in orders + boss
        * order - list
        * sub-boss - list
        * boss - string
    @ npcs - dict 
        * key:npc name
        * value:part in the encounter
    @ rewards - dict
        * gp: value
        * common_itens: list
        * magical_itens: list
    """

    def __repr__(self):
        return self.name

    #!##################
    ## ! location
    #!##################
    def add_location(self, location):
        self.locaton = self.locaton + [location]

    #!##################
    ## ! npcs
    #!##################
    def add_npc(self, npc, text):
        ret = f'self.npcs["{npc}"] = "{text}"'
        exec(ret)

    def rm_npc(self, npc):
        ret = f'del r["{npc}"]'
        exec(ret)

    #!##################
    ## ! rewards
    #!##################
    def set_gp(self, value):
        self.rewards['gp'] = value

    def add_item(self, item):
        self.rewards['common_itens'] = self.rewards['common_itens'] + [item]

    def add_magical_item(self, magical_item):
        self.rewards['magical_items'] = self.rewards['magical_items'] + [magical_item]

    #!##################
    ## ! plot
    #!##################
    def add_info(self, new_info):
        self.plot = self.plot + f'\n{new_info}'
    
    def set_plot(self, new_plot):
        self.plot = self.name + f'\n{new_plot}'