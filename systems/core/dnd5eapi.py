import requests as rq

base_url = 'https://www.dnd5eapi.co/api/'

## ! spells
def get_spells():
    return rq.get(base_url+ 'spells/')
def get_magic_schools():
    return rq.get(base_url+ 'magic-schools/')

## ! monsters
def get_monsters():
    return rq.get(base_url+ 'monsters/')
def get_monster(monster):
    return rq.get(base_url+ 'monsters/'+monster)
def get_traits():
    return rq.get(base_url+ 'traits/')
def get_trait(trait):
    return rq.get(base_url+ 'traits/'+trait)

## ! battle
def get_conditions():
    return rq.get(base_url+ 'conditions/')
def get_damage_types():
    return rq.get(base_url+ 'damage_types/')

## ! items
def get_equipment_categories():
    return rq.get(base_url+ 'equipment_categories/')
def get_equipment():
    return rq.get(base_url+ 'equipment/')
def get_weapon_properties():
    return rq.get(base_url+ 'weapon-properties/')

## ! magic items
def get_magic_items():
    return rq.get(base_url+ 'magic-items/')
def get_magic_item(magical_item_name):
    return rq.get(base_url+'magic-items/'+magical_item_name)

## ! char
def get_ability_scores():
    return rq.get(base_url+'ability-scores/')
def get_alignments():
    return rq.get(base_url+ 'alignments/')
def get_backgrounds():
    return rq.get(base_url+ 'backgrounds/')
def get_languages():
    return rq.get(base_url+ 'languages/')
def get_classes():
    return rq.get(base_url+ 'classes/')
def get_subclasses():
    return rq.get(base_url+ 'subclasses/')
def get_races():
    return rq.get(base_url+ 'races/')
def get_subraces():
    return rq.get(base_url+ 'subraces/')
def get_skills():
    return rq.get(base_url+ 'skills/')
def get_features():
    return rq.get(base_url+ 'features/')
def get_proficiencies():
    return rq.get(base_url+ 'proficiencies/')
def get_feats():
    return rq.get(base_url+ 'feats/')

## ! dm
def get_rule_sections():
    return rq.get(base_url+ 'rule-sections/')
def get_rules():
    return rq.get(base_url+ 'rules/')
