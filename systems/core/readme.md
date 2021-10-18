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
