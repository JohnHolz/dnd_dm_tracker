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

#! City
Selgaunt = Urban('Selgaunt')

##@ Yondalla_Temple
YondallaTemple = Place('Yondalla Temple')
###* Rooms from place
ChapelDome = Room('Chapel Dome')
InsideDungeon = Room('Inside Dungeon')

##@ Selgaunt_High_Castle
SelgauntHighCastle = Place('Selgaunt High Castle')
###* Rooms from place
BigTower = Room('Big Tower')
CenterRoom = Room('Center Room')
CastleRoomsCorridors = Room('Castle Rooms Corridors')
BigFightRoom = Room('Big Fight Room')