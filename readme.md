# Dnd game tracker

As a GM i need to keep track of a lot of ideas, encounters, events, rounds, party stats, itens, npcs...

## Objective

Handcode the fewest as possible to track my dnd tables. So I will create a dozen of classes and use [Dnd5eapi](https://www.dnd5eapi.co/) to get the rest.

# Folder Structure

    1. campaigns:
       1. campaign_name --------------------> campaign been or finished run
       2. campaign_name_2 ------------------> campaign been or finished run
       3. default_folder -------------------> folder to copy and paste and start campaign
           1. db ---------------------------> save the events of the campaign
           2. current-place.ipynb ----------> fast information of the party and npcs
           3. events.ipynb -----------------> declaring events
           4. major-plots.ipynb ------------> major plot notes
           5. random-encounters.ipynb ------> random encounters / happenings
    2. creation:
       1. encounter-creation.ipynb ---------> encounter creation and save in world db
       2. npc-creation.ipynb ---------------> npc creation and save in word db
       3. mob-group-creation.ipynb ---------> balance encounters
    3. src
       1. characters -----------------------> char class
       2. dnd5eapi -------------------------> bunch of api get requests built
       3. encounter ------------------------> encounter class
       4. game -----------------------------> game class and event class
       5. item -----------------------------> item class
       6. npcs -----------------------------> npc class
       7. small ----------------------------> small systems
       8. tests ----------------------------> test of all src folder
    4. world
       1. db -------------------------------> folder to save all you create
       2. locane ---------------------------> a continent folder to pre-build objects to fast access
       3. lossenue -------------------------> a continent folder to pre-build objects to fast access
       4. rules ----------------------------> my roleplay rules accessile
       5. utils.py -------------------------> util objects

# 1.0.0

Creating my classes and functions with the 1.0 Tracker I want to use just jupyter notebooks for running the code to help me out during the sessions and a database for homebrew itens and npcs.

| To finish   | needed | ok     |
| ----------- | ------ | ------ |
| encounter   | class  | almost |
| encounter   | save   | --     |
| encounter   | read   | --     |
| npc         | --     | ok     |
| game/events | --     | ok     |
| item        | --     | ok     |
| mob_group   | --     | ok     |

## Game Example

### Game Notebook

### Possible Encounters Notebook

### Creation notebook

# 2.0.0

Maybe someday i will do a website but the focus is to create some notebooks and a database to keep track of my dnd tables.
