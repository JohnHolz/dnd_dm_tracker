# Itens

    def __init__(self, name, description='', item_type = '',
                 magical=False, unique = False, owner=None):
        self.name = name
        self.description = description

        ## core info
        self.unique = unique
        self.item_type = ''
        self.tags = []
        self.roll = ''

        self.owner = owner
        self.status = {}
        self.other_info = {}
        self.magical = magical
        if magical:
            self.special = {
                'special_habilities':{},
                'hidden_habilities':{}
            }

---

# Item class

info keeped

1. name
2. description
3. type
4. tags
5. owner
6. unique
7. magical
8. habilities

methods
1. get events associateds with the item
---

Characteristcs of itens:

1. How many they are:
   1. Unique itens
   2. Non-Unique itens
2. Important in the world:
   1. Lore
   2. Why
3. Special Effects Itens:
   1. Special Habilities
   2. Special Effects
   3. Lore

Itens information:

1. Name
2. Status

3. Unique: boolean
4. Where they are in your world
5. Lore
6. Special effects
7. Special habilities
8. If they are unique? How many they are?

# Class Item

## Unique Itens

### Unique Shield example:

      {
         'name': 'Heironeous Shield',
         'description':
            'beaultiful white shield with a big Heironeous simpble'
         status: {
            'ac':+3
         }
         special_effects: {
            special_habilities:{
               'blocking against evil': '+2AC'
               'blocking': 'heal proficiency*d6+4'
            }
            hidden_habilities:{
               'Heironeous Power': 'once a week can be cast a strong light from the shield that heals all allies inside the room or 10 meters radius with 15%hp + 2d10'
            }
         }
      }

### Unique Sword example:

      {
         'name': 'Heironeous Shield',
         'description':
            'beaultiful white shield with a big Heironeous simpble'
         status: {
            'ac':+3
         }
         special_effects: {
            special_habilities:{
               'blocking against evil': '+2AC'
               'blocking': 'heal proficiency*d6+4'
            }
            hidden_habilities:{
               'Heironeous Power': 'once a week can be cast a strong light from the shield that heals all allies inside the room or 10 meters radius with 15%hp + 2d10'
            }
         }
      }
