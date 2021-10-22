from small.coin import Money
from db_interact import read_db, write_db, load_from_db
import sys
sys.path.append('../')


class Npc():
    def __init__(self, name=None) -> None:
        self.name = name
        self.core = None
        self.combat = None
        self.drives = {
            'legacy': [],
            'value': [],
            'beliefs': [],
        }
        self.items = {
            'money': Money(0, 0, 0, 0, 0),
        }
        self.connections = {}

    def __repr__(self) -> str:
        ret = f'''{self.name}\n{self.core}\n{self.combat}\n{self.drives}\n{self.connections}'''
        return ret

    def add_core(self, core):
        self.core = core

    def add_combat(self, combat):
        self.combat = combat

    def add_item(self, item, value):
        self.items[item] = value

    def get_json(self):
        ret = dict()
        ret['name'] = self.name
        ret['core'] = self.core.get_dict()
        ret['combat'] = self.combat.get_dict()
        ret['drives'] = self.drives
        ret['connections'] = self.connections
        return ret

    def add_drives(self, drives_type, drives):
        if drives_type not in self.drives.keys():
            self.drives[drives_type] = [drives]
        else:
            self.drives[drives_type] = self.drives[drives_type] + [drives]

    def add_connection(self, connection_name, connection_desc):
        if connection_name not in self.connections.keys():
            self.connections[connection_name] = [connection_desc]
        else:
            self.connections[connection_name] = self.connections[connection_name] + \
                [connection_desc]

    def save_npc(self, path):
        db = read_db(path)
        db[self.name] = self.get_json()
        write_db(path)


def get_npc(npc_name, path):
    db = read_db(path)
    npc_dict = db[npc_name]
    npc = Npc()
    npc.name = npc_dict['name']
    npc.core = npc_dict['core']
    npc.combat = npc_dict['combat']
    npc.drives = npc_dict['drives']
    npc.connections = npc_dict['connections']
    return npc
