class Item():
    def __init__(self, name, unique=True, info='', owner=None, unique = False):
        self.name = name
        self.owner = owner
        self.info = info
        self.status = dict()
        self.unique = unique


    def __repr__(self):
        ret = f"""
        {self.name}
        {self.status}
        """
        return ret


class SpecialItem(Item):
    def add_special_hability(self, name, effect):
        self.special_habilities = self.special_habilities+{name:effect}

    def add_hidden_hability(self, name, effect):
        self.hidden_habilities = self.hidden_habilities+{name:effect}

magical_item = {
    
}