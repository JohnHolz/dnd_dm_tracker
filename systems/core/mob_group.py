from jh_utils.utils.utils import to_print_dict, to_print_list

class Mob_group():
    def __init__(self, mobs={}, boss=None):
        self.mobs = mobs
        self.boss = []
        if boss!=None:
            if type(boss)==str:
                boss = [boss]
            self.boss = self.boss + boss

    def __repr__(self) -> str:
        ret = f'''boss: {to_print_list(self.boss)} \nmobs:\n{to_print_dict(self.mobs)}'''
        return ret

    def add_mobs(self, mob, number):
        self.mobs[mob] = number

    def add_boss(self, boss):
        self.boss = self.boss + [boss]
