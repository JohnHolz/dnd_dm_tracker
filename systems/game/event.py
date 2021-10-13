from ..char.npc import Vutar, Benio, Bushi, Aussyrk

party_char_list = [Vutar, Benio, Bushi, Aussyrk]

class Event():
    def __init__(self, time, place, info='', party=True, npcs=[], chars=[]):

        self.time = time
        self.place = place
        self.npcs = npcs
        self.info = info
        self.full_party = party
        if party:
            self.chars = party_char_list
            self.full_party = party
        else:
            self.chars = chars

    def __repr__(self):
        if self.full_party:
            party_show = f'Full Party'
        else:
            party_show = f'{self.chars}'
        ret = f"""
        {self.time}
        where:  {self.place}
        npcs: {self.npcs}
        chars: {party_show}
        {self.info}
        """
        return ret
