# Itens

Characteristcs of itens:
1. How many they are:
   1. Unique itens
   2. Non-Unique itens
2. Important in the world:
   1. Lore
   1. Why
3. Special Effects Itens:
   1. Special Habilities
   2. Special Effects
   3. Lore

Itens information:
1. Name
2. Status

2. Unique: boolean
3. Where they are in your world
4.  Lore
6.  Special effects
7.  Special habilities
8.  If they are unique? How many they are?


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
