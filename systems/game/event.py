class Event():
    def __init__(self, time, place, info = '', npcs = [], chars = []):
        self.time = time
        self.place = place
        self.npcs = npcs
        self.chars = chars
        self.info = info

    def __repr__(self):
        ret = f"""
        date: {self.time}
        where: {self.place}
        npcs: {self.npcs}
        chars: {self.chars}
        {self.info}
        """
        return ret

    