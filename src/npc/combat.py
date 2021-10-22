from jh_utils.utils.utils import to_print_dict
from small.status import Status, dict_to_Status
import sys
sys.path.append('../')


class Combat():
    def __init__(self,
                 hp=0,
                 ca=10,
                 cr=None,
                 speed=30,
                 passive_perception=10,
                 initiative=0,
                 status=Status(),
                 resistences={},
                 senses=None,
                 arcana={},
                 actions={},
                 equipment={'armor': [], 'weapons': [], 'items': []}) -> None:

        # mob tings
        self.hp = hp
        self.ca = ca
        self.cr = cr
        self.speed = speed
        # status
        self.status = status
        self.passive_perception = passive_perception + self.status.wis_mod
        self.initiative = initiative + self.status.dex_mod
        ## resistences and immunities
        self.resistences = resistences
        self.senses = senses
        ##
        self.equipment = equipment
        self.arcana = arcana
        self.actions = actions

    def __repr__(self) -> str:
        ret = f'''hp:{self.hp}, ca:{self.ca}, cr:{self.cr}, speed:{self.speed}
pass-per:{self.passive_perception}, initiative:{self.initiative}
#-------------------------------------#
{self.status}
#-------------------------------------#
resistences: 
{to_print_dict(self.resistences)}, 
senses: {self.senses}
#-------------------------------------#
weapons: 
{to_print_dict(self.equipment)}#-------------------------------------#
arcana: 
{to_print_dict(self.arcana)}#-------------------------------------#
actions: 
{to_print_dict(self.actions)}'''
        return ret

    def get_dict(self):
        ret = dict()
        ret['hp'] = self.hp
        ret['ca'] = self.ca
        ret['cr'] = self.cr
        ret['speed'] = self.speed
        ret['passive_perception'] = self.passive_perception
        ret['initiative'] = self.initiative
        ret['status'] = self.status.get_dict()
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


def dict_to_combat(combat_dict):
    ret = Combat(hp=combat_dict['hp'],
                 ca=combat_dict['ca'],
                 cr=combat_dict['cr'],
                 speed=combat_dict['speed'],
                 passive_perception=0,
                 initiative=0,
                 status=dict_to_Status(combat_dict['status']),
                 resistences=combat_dict['resistences'],
                 armor=combat_dict['armor'],
                 weapons=combat_dict['weapons'],
                 items=combat_dict['items'],
                 senses=combat_dict['senses'])
    ret.passive_perception = combat_dict['passive_perception']
    ret.initiative = combat_dict['initiative']
    return ret
