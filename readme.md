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
       4. notebooks ... 
    3. src
       1. dnd5eapi -------------------------> bunch of api get requests built
       2. encounter ------------------------> encounter class
       3. game -----------------------------> game class and event class
       4. item -----------------------------> item class
       5. npcs -----------------------------> npc class
       6. small ----------------------------> small systems
       7. tests ----------------------------> test of all src folder
    4. world
       1. db -------------------------------> folder to save all you create
       2. dm -------------------------------> dm plots, encounters and things like that
       3. players --------------------------> open information for the players
