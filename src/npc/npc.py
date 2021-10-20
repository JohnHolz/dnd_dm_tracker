from small.coin import Money

class Npc():
    def __init__(self, name) -> None:
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


def save_npc(npc):
    pass


def get_npc(npc_name):
    pass
