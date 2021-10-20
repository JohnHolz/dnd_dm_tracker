import sys
sys.path.append('../')

class Core():
    def __init__(self,
                ocupation=None, 
                race='human', 
                languages={'common':'fluent'}, 
                aligment='N',
                background='soldier') -> None:
        self.ocupation = ocupation
        self.race = race
        self.languages = languages
        self.aligment = aligment
        self.background = background

    def __repr__(self) -> str:
        ret = f'''{self.race} - {self.ocupation}
        {self.languages}
        {self.background}
        {self.drives}'''
        return ret

    def get_json(self):
        ret = dict()
        ret['ocupation'] = self.ocupation
        ret['race'] = self.race
        ret['languages'] = self.languages
        ret['aligment'] = self.aligment
        ret['background'] = self.background
        return ret

