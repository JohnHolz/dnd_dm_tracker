class Item():
    def __init__(self, name, unique = False):
        self.name = name
        self.place = place
        self.npcs = npcs
        self.chars = chars
        self.info = info

    def __repr__(self):
        ret = f"""
        date: {self.name}
        where: {self.place}
        npcs: {self.npcs}
        chars: {self.chars}
        {self.info}
        """
        return ret

    