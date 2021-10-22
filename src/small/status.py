class Status():
    def __init__(self, strength=10,
                 dexterity=10,
                 constitution=10,
                 inteligence=10,
                 wisdom=10,
                 charisma=10) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.inteligence = inteligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.str_mod = round((self.strength - 10)/2)
        self.dex_mod = round((self.dexterity - 10)/2)
        self.con_mod = round((self.constitution - 10)/2)
        self.int_mod = round((self.inteligence - 10)/2)
        self.wis_mod = round((self.wisdom - 10)/2)
        self.cha_mod = round((self.charisma - 10)/2)

    def __repr__(self) -> str:
        ret = f"""str: +{self.str_mod}({self.strength})\ndex: +{self.dex_mod}({self.dexterity})\ncon: +{self.con_mod}({self.constitution})\nint: +{self.int_mod}({self.inteligence})\nwis: +{self.wis_mod}({self.wisdom})\ncha: +{self.cha_mod}({self.charisma})"""
        return ret

    def get_dict(self):
        ret = dict()
        ret['strength'] = self.strength
        ret['dexterity'] = self.dexterity
        ret['constitution'] = self.constitution
        ret['inteligence'] = self.inteligence
        ret['wisdom'] = self.wisdom
        ret['charisma'] = self.charisma
        return ret


def dict_to_Status(dict_status):
    ret = Status(
        strength=dict_status['strength'],
        dexterity=dict_status['dexterity'],
        constitution=dict_status['constitution'],
        inteligence=dict_status['inteligence'],
        wisdom=dict_status['wisdom'],
        charisma=dict_status['charisma'])
    return ret
