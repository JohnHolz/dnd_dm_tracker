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
class npc():
    def __init__(self,name,*args) -> None:
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


### !! NPCS !! ###
## *templos - priests
Shao = npc('Shao')
Nokora = npc('Nokora')
##* inn
Beatrice = npc('beatrice')
Leo = npc('leo')
Remus = npc('remus')
##* tabernas
Grik = npc('grik')
Lia = npc('lia')
Astalon = npc('astalon')
Xaalha = npc('xaalha')
Jaq = npc('jaq')
Tiana = npc('tiana')
##* market
Cxorr = npc('cxorr')
Azathot = npc('azathot')
Riuan = npc('riuan')
Balanar = npc('balanar')
Felosial = npc('felosial')
Edino = npc('edino')
Val = npc('val')
Kled = npc('kled')
Drungar = npc('Drungar') ## Meu nome parece bebado pra vocês mas na minha terra significa o grande quebrador de pedras e Dugnars.
