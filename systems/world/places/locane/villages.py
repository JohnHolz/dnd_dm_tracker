class Urban():
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return self.name
class Place():
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return self.name
class Room():
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return self.name


# ! Village
## @ Place
### * Rooms

# ! Ormskirk
Ormskirk = Urban('Ormskirk')
## @ Place
Ormskirk_Tavern = Place('Ormskirk_Tavern')
### * Rooms

# ! Marmouth
Marmouth = Urban('Marmouth')
## @ Place
Marmouth_Tavern = Place('Marmouth_Tavern')

# ! Bredon
Bredon = Urban('Bredon')
## @ Place
Bredon_Tavern = Place('Bredon_Tavern')

# ! Bellmare
Bellmare = Urban('Bellmare')
## @ Place
Bellmare_Tavern = Place('Bellmare_Tavern')