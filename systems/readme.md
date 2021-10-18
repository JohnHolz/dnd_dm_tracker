# Systems Tree

## Core

| System Name | System needed | Description                                          |
| ----------- | ------------- | ---------------------------------------------------- |
| coin        |               | Money class + coin changes                           |
| dice        |               | Dice rolls function                                  |
| dnd5eapi    |               | Dnd things from book (Monsters, magic-itens, spells) |
| event       |               | Declare campaing events to remember later            |
| item        |               | To create a item                                     |
| mob_group   | dnd5eapi      | Create a mob party (mobs + boss, kobolds + basilisk) |
| status      |               | Declare a status class to get modifiers faster       |
| time        |               | Time class, when something happens                   |

## Biger systems

| System Name | Needed Systems | Core Systens needed         | Description                                    |
| ----------- | -------------- | --------------------------- | ---------------------------------------------- |
| Characters  | NPCs           | coin, spells, item          | NPCs class and random creation                 |
| Place       | Party char     | npc, item                   | Place Class to add                             |
| Encounter   | Party char     | monsters, place, item, npcs | Future Encounter ideas and possible encounters |
