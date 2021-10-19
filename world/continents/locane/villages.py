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

# ! Village
## @ Place
### * Rooms

# ! Ormskirk
Ormskirk = Urban('Ormskirk')
## @ Place
Ormskirk_Tavern = Place('Ormskirk_Tavern')
### * Rooms
### $ npcs
leshanna_ormskirk = npc(name = 'leshanna_ormskirk', age = 110, race = 'halfling', sex = 'female', alignment = 'N', ocupation = 'waitress', city = 'ormskirk', place = 'taberna', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
lekishr_ormskirk = npc(name = 'lekishr_ormskirk', age = 200, race = 'dwarf', sex = 'male', alignment = 'N', ocupation = 'barman', city = 'ormskirk', place = 'taberna', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
shaw_ormskirk = npc(name = 'shaw_ormskirk', age = 55, race = 'aarakroka', sex = 'male', alignment = 'N', ocupation = 'inn owner', city = 'ormskirk', place = 'inn', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 200 sp 120', descricao = 'gentil')
kaugea_ormskirk = npc(name = 'kaugea_ormskirk', age = 80, race = 'satyr', sex = 'female', alignment = 'N', ocupation = 'herbalista', city = 'ormskirk', place = 'casa dele aberta pra praça', alive = True, classe = 'druid', lvl = 8, ac = 8, itens = 'dagger', gold = 'gp 200 sp 120', descricao = 'gentil')
laroth_ormskirk = npc(name = 'laroth_ormskirk', age = 70, race = 'golliah', sex = 'male', alignment = 'N', ocupation = 'blacksmith', city = 'ormskirk', place = 'casa dele aberta pra praça', alive = True, classe = 'barbaro', lvl = 9, ac = 15, itens = 'greataxe+1', gold = 'gp 300 sp 600', descricao = 'gentil')


# ! Marmouth
Marmouth = Urban('Marmouth')
## @ Place
Marmouth_Tavern = Place('Marmouth_Tavern')
### $ npcs
kreldik_marnmouth = npc(name = 'kreldik_marnmouth', age = 40, race = 'dragonborn', sex = 'male', alignment = 'N', ocupation = 'owner inn', city = 'marnmouth', place = 'inn de marnmouth', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil') 
enna_marnmouth = npc(name = 'enna_marnmouth', age = 25, race = 'human', sex = 'female', alignment = 'N', ocupation = 'waitress', city = 'marnmouth', place = 'taberna de marnmouth', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
gofu_marnmouth = npc(name = 'gofu_marnmouth', age = 35, race = 'halfling', sex = 'male', alignment = 'N', ocupation = 'barman', city = 'marnmouth', place = 'taberna de marnmouth', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')


# ! Bredon
Bredon = Urban('Bredon')
## @ Place
Bredon_Tavern = Place('Bredon_Tavern')
### $ npcs
shava_bredon = npc(name = 'shava_bredon', age = 50, race = 'human', sex = 'female', alignment = 'N', ocupation = 'waitress e funcionario', city = 'bredon', place = 'taberna bredon', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
alcam_bredon = npc(name = 'alcam_bredon', age = 25, race = 'human', sex = 'male', alignment = 'N', ocupation = 'barman e funcionario', city = 'bredon', place = 'taberna bredon', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
luenuem_bredon = npc(name = 'luenuem_bredon', age = 55, race = 'human', sex = 'male', alignment = 'N', ocupation = 'blacksmith', city = 'bredon', place = 'casa dele aberta', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 200 sp 120', descricao = 'gentil')


# ! Bellmare
Bellmare = Urban('Bellmare')
## @ Place
Bellmare_Tavern = Place('Bellmare_Tavern')
### npcs
bumeg_bellmare = npc(name = 'bumeg_bellmare', age = 100, race = 'dwarf', sex = 'male', alignment = 'N', ocupation = 'male waitress', city = 'bellmare', place = 'taberna bredon', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
orinulir_bellmare = npc(name = 'orinulir_bellmare', age = 140, race = 'dwarf', sex = 'male', alignment = 'N', ocupation = 'barman', city = 'bellmare', place = 'taberna bredon', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 40 sp 60', descricao = 'gentil')
yakeala_bellmare = npc(name = 'yakeala_bellmare', age = 55, race = 'dwarf', sex = 'female', alignment = 'N', ocupation = 'inn owner', city = 'bellmare', place = 'inn de bellmare', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 200 sp 120', descricao = 'gentil')
grakgregit_bellmare = npc(name = 'grakgregit_bellmare', age = 200, race = 'dwarf', sex = 'female', alignment = 'N', ocupation = 'herbalista', city = 'bellmare', place = 'herbalista de bellmare', alive = True, classe = ' ', lvl = 0, ac = 8, itens = ' ', gold = 'gp 200 sp 120', descricao = 'gentil')