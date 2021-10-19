# Core

Core systems composes othe big systems. To create an NPC or a char we need, money, past events, habilities, dice, status...

| System     | Description                                            |
| ---------- | ------------------------------------------------------ |
| Coin       | Money System                                           |
| Dice       | Rolls                                                  |
| Dnd 5e api | Use Dnd 5e api to get access to all the things we need |
| Event      | Past events to keep                                    |
| Item       | Item creation                                          |
| Mob group  | Enemy group to be used in encounters                   |
| Status     | Status + Modifiers                                     |
| Time       | World time and calendar to be used                     |

# Events

Events will be kinda the log of the game. Every time you want to save an information as an event that happens in game you just call a method of the game/events class ans save the info you need.

- NPCs names, itens, gold rewarded, apearence. Some frase used by someone.
- If you want all the information, but you will need to type all the info.

# Core System

Small systems to compose the parts we wanna track

1. Coin
2. Dice
3. Hability
4. Status

---

<br>

# Coin System

| Coin     | sim  | cp   | sp   | ep   | gp    | pp     |
| -------- | ---- | ---- | ---- | ---- | ----- | ------ |
| Copper   | (cp) | 1    | 1/10 | 1/50 | 1/100 | 1/1000 |
| Silver   | (sp) | 10   | 1    | 1/5  | 1/10  | 1/100  |
| Electrum | (ep) | 50   | 5    | 1    | 1/2   | 1/20   |
| Gold     | (gp) | 100  | 10   | 2    | 1     | 1/10   |
| Platinum | (pp) | 1000 | 100  | 20   | 10    | 1      |

---

<br>

# Dice System

From the dice system we will need a Roll dice function working. Like

    roll('1d6+2') # -> random int between 1-6 plus 2

We need too:

1.  default random mean rolls:

        10*d10+10 -> 60
        10*d6 +10 -> 45
        10*d4 +10 -> 35

2.  random default value rolls:

        start_gold: 20*d8 + 20 -> 110
        human+hp: lvl*d6 + 10 -> lvl*3.5+10

---

<br>

# Hability

Hability class to save habilities

---

<br>

# Status

Hability scores as a class to be fast associated with npcs and chars

| Score | Modifier | Score | Modifier |
| ----- | -------- | ----- | -------- |
| 2-3   | -4       | 18-19 | +4       |
| 4-5   | -3       | 20-21 | +5       |
| 6-7   | -2       | 22-23 | +6       |
| 8-9   | -1       | 24-25 | +7       |
| 10-11 | +O       | 26-27 | +8       |
| 12-13 | +l       | 28-29 | +9       |
| 14-15 | +2       | 30    | +10      |

# Items

### Unique Shield example:

      {
         "index": "animated-shield",
         "name": "Animated Shield",
         "equipment_category": {
            "index": "armor",
            "name": "Armor",
            "url": "/api/equipment-categories/armor"
        },
         "desc": [
            "Armor (shield), very rare (requires attunement)",
            "While holding this shield, you can speak its command word as a bonus action to cause it to animate. The shield leaps into the air and hovers in your space to protect you as if you were wielding it, leaving your hands free. The shield remains animated for 1 minute, until you use a bonus action to end this effect, or until you are incapacitated or die, at which point the shield falls to the ground or into your hand if you have one free."
            ]
        }

### Unique Sword example:

      {
      	"index": "flame-tongue",
      	"name": "Flame Tongue",
      	"equipment_category": {
            "index": "weapon",
            "name": "Weapon",
            "url": "/api/equipment-categories/weapon"
         },
         "desc": [
            "Weapon (any sword), rare (requires attunement)",
            "You can use a bonus action to speak this magic sword's command word, causing flames to erupt from the blade. These flames shed bright light in a 40-foot radius and dim light for an additional 40 feet. While the sword is ablaze, it deals an extra 2d6 fire damage to any target it hits. The flames last until you use a bonus action to speak the command word again or until you drop or sheathe the sword."
         ]
      }


### Encounter:

Encounters I want to let as a database of ideas of encounters.
A class that:

1.  Init the class with simple ideas to been completed as you want.
2.  Keep the important information of a possible already planned encounter.
3.  Ease to find the encounter that the DM needs at the moment (finding by location, rewards, enemies).

# Places

| Type   | Contains    | ---             |
| ------ | ----------- | --------------- |
| Room   | mobs, items | Small           |
| Places | npcs        | Contains rooms  |
| Urban  | ---         | Contains places |

## Types of Places

1. Cities, Town and villages
   1. general info
      1. description
      2. lore
      3. important npcs
   2. (↧) SPERMM info
      1. social
      2. politic
      3. economy
      4. religius
      5. military
      6. magical
   3. intern places
2. Intern places
   1. types
      1. open places
         1. dungeons
         2. forts
         3. cave
         4. open fields
         5. planicies
         6. florest
         7. swamp
         8. monuments
      2. urban intern places
         1. stores
         2. taverns
         3. temples
         4. squares
         5. farm
   2. rooms
   3. description
   4. itens inside
   5. lore

## Characteristics of places:

      ---
      Selgaunt
         The sea white fortress
         city
         places:
            port
            central square
            castle
      ---

      hideen info
         1. basic city info:
            1. social
            2. political
            3. economy
            4. religious
            5. military
            6. magical
         2. lore
         3. important npcs


      ---
      Minas Mirabar
         The suspended minas on the grey Hill
         city
         places:
            port
            central square
            castle
      ---

# Characters/Players:

The char class need just to keep the most important info of our party. So I will just keep what I use in my day by day. But with time maybe I will implement a whole character sheet.

- Passive Perception
- Magical Itens
- AC
- HP
- Some spells slots

### NPCs

NPC class are to keep important npcs, npcs itens, gold, lore and to create random npcs to us.

---

# Xp System

| Experience Points | Level | Proficiency Bonus |
| ----------------- | ----- | ----------------- |
| 0                 | 1     | +2                |
| 300               | 2     | +2                |
| 900               | 3     | +2                |
| 2.700             | 4     | +2                |
| 6.500             | 5     | +3                |
| 14.000            | 6     | +3                |
| 23.000            | 7     | +3                |
| 34.000            | 8     | +3                |
| 48.000            | 9     | +4                |
| 64.000            | 10    | +4                |
| 85.000            | 11    | +4                |
| 100.000           | 12    | +4                |
| 120.000           | 13    | +5                |
| 140.000           | 14    | +5                |
| 165.000           | 15    | +5                |
| 195.000           | 16    | +5                |
| 225.000           | 17    | +6                |
| 265.000           | 18    | +6                |
| 305.000           | 19    | +6                |
| 355.000           | 20    | +6                |
