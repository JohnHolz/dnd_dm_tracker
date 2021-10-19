import sys
sys.path.append('../')
class Char():
    def __init__(self,name,*args) -> None:
        self.name = name
    def __repr__(self) -> str:
        return self.name

Vutar = Char('Vutar')
Benio = Char('Benio')
Bushi = Char('Bushi')
Aussyrk = Char('Aussyrk')

Party = [Vutar, Benio, Bushi, Aussyrk]