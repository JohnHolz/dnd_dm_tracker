from jh_utils.utils.utils import to_print_dict, to_print_list
import sys
sys.path.append('../')
from db_interact import read_db, write_db, load_from_db


class Mob_group():
    def __init__(self, mobs={}, boss=None, cr=0):
        self.mobs = mobs
        self.boss = []
        self.cr = cr
        if boss != None:
            if type(boss) == str:
                boss = [boss]
            self.boss = self.boss + boss

    def __repr__(self) -> str:
        ret = f'''boss: {to_print_list(self.boss)} \nmobs:\n{to_print_dict(self.mobs)}'''
        return ret

    def add_mobs(self, mob, number):
        self.mobs[mob] = number

    def add_boss(self, boss):
        self.boss = self.boss + [boss]

    def number_of_monsters(self):
        n = 0
        if self.boss != []:
            n = n+len(self.boss)
        if self.mobs != {}:
            for i in self.mobs:
                n = n + self.mobs[i]
        return n

    def create_id(self):
        return f'{self.cr}-{self.boss[0]}'

    def get_json(self):
        ret = dict()
        ret['id'] = self.create_id()
        ret['mobs'] = self.mobs
        ret['boss'] = self.boss
        ret['cr'] = self.cr
        ret['n'] = self.number_of_monsters()
        return ret

    def save_group(self,db_path):
        db = read_db(db_path)
        group_dict = self.get_json()
        db[group_dict['id']] = group_dict
        write_db(db, db_path)

def dict_to_mob_gr(mob_dict):
    mob_gr = Mob_group(mob_dict['mobs'], mob_dict['boss'], mob_dict['cr'])
    return mob_gr

def load_mob_group(mob_group_id, db_path):
    item_dict  = load_from_db(mob_group_id, db_path)
    return dict_to_mob_gr(item_dict)

def mobs_table(mob_db_path):
    import pandas as pd
    db = read_db(mob_db_path)
    db_keys = list(db.keys())
    df = pd.DataFrame(pd.Series(db_keys),columns=['group-id'])
    df['cr'] = df['group-id'].apply(lambda x: db[x]['cr'])
    df['n'] = df['group-id'].apply(lambda x: db[x]['n'])
    df['mobs'] = df['group-id'].apply(lambda x: db[x]['mobs'])
    df['boss'] = df['group-id'].apply(lambda x: db[x]['boss'])
    return df