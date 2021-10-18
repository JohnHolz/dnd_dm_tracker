from jh_utils.utils.utils import to_print_dict


class mob_group():
    def __init__(self, mobs={}, boss=None):
        self.mobs = mobs
        self.boss = boss

    def __repr__(self) -> str:
        ret = f'''boss: {self.boss}
        mobs: 
        {to_print_dict(self.mobs)}'''
        return ret

    def add_mobs(self, mob, number):
        self.mobs[mob] = number

    def add_boss(self, boss):
        self.boss = self.boss + [boss]
