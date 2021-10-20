import sys
sys.path.append('../')
from small.status import Status

class Combat():
    def __init__(self,
                hp,
                ca=10,
                cr=None,
                speed=30,
                passive_perception=10,
                initiative=0,
                status = Status(10,10,10,10,10),
                resistences = {},
                armor=[],
                weapons=[],
                items=[],
                senses=None) -> None:

        ## mob tings
        self.hp = hp
        self.ca = ca
        self.cr = cr
        self.speed = speed
        ## status
        self.status = status
        self.passive_perception = passive_perception + self.status.wis_mod
        self.initiative = initiative + self.status.dex_mod
        ## resistences and immunities
        self.resistences = resistences
        self.senses = senses
        ## 
        self.equipment = {
                    'armor': armor,
                    'weapons': weapons,
                    'items':items}
        self.arcana = {}
        self.actions = {}

    def __repr__(self) -> str:
        ret = f'''hp:{self.hp}, ca:{self.ca}, cr:{self.cr}, speed:{self.speed}
        pass-per:{self.passive_perception}, initiative:{self.initiative}
        {self.status}
        resistences: {self.resistences}, {self.senses}
        weapons: {self.equipment}
        arcana: {self.arcana}
        actions: {self.actions}'''
        return ret  

    def get_json(self):
        ret = dict()
        ret['hp'] = self.hp
        ret['ca'] = self.ca
        ret['cr'] = self.cr
        ret['speed'] = self.speed
        ret['passive_perception'] = self.passive_perception
        ret['initiative'] = self.initiative
        ret['status'] = self.status
        ret['resistences'] = self.resistences
        ret['senses'] = self.senses
        ret['equipment'] = self.equipment        
        ret['arcana'] = self.arcana
        ret['actions'] = self.actions
        return ret
    
    def add_arcana(self, info_key, info_desc):
        if info_key not in self.arcana.keys():
            self.arcana[info_key] = [info_desc]
        else:
            self.arcana[info_key] = self.arcana[info_key] + [info_desc]

    def add_action(self, info_key, info_desc):
        if info_key not in self.actions.keys():
            self.actions[info_key] = [info_desc]
        else:
            self.actions[info_key] = self.actions[info_key] + [info_desc]
