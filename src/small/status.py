class Status():
    def __init__(self, strength, dexterity, constitution, inteligence, wisdom, charisma) -> None:
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
