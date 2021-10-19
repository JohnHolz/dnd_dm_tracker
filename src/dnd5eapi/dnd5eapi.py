import requests as rq

base_url = 'https://www.dnd5eapi.co/api/'

# ! spells
def get_spells(spell=''):
    return rq.get(base_url + 'spells/' + spell)
def get_magic_schools(magic_school=''):
    return rq.get(base_url + 'magic-schools/' + magic_school)

# ! monsters
def get_monsters(monster=''):
    return rq.get(base_url + 'monsters/' + monster)
def get_traits(trait=''):
    return rq.get(base_url + 'traits/' + trait)

# ! battle
def get_conditions(condition=''):
    return rq.get(base_url + 'conditions/' + condition)
def get_damage_types(damage_type=''):
    return rq.get(base_url + 'damage-types/' + damage_type)

# ! items

def get_equipment_categories(equipment_categorie=''):
    return rq.get(base_url + 'equipment-categories/'+equipment_categorie)
def get_equipments(equipment=''):
    return rq.get(base_url + 'equipment/'+equipment)
def get_weapon_properties(weapon_properties=''):
    return rq.get(base_url + 'weapon-properties/'+weapon_properties)

# ! magic items

def get_magic_items(magic_item=''):
    return rq.get(base_url+'magic-items/'+magic_item)

# ! char

def get_ability_scores(ability=''):
    return rq.get(base_url+'ability-scores/' + ability)
def get_races(race=''):
    return rq.get(base_url + 'races/' + race)
def get_subraces(subrace=''):
    return rq.get(base_url + 'subraces/'+subrace)
def get_classes(classe=''):
    return rq.get(base_url + 'classes/' + classe)
def get_subclasses(subclasse=''):
    return rq.get(base_url + 'subclasses/' + subclasse)
def get_alignments(alignment=''):
    return rq.get(base_url + 'alignments/' + alignment)
def get_backgrounds(background=''):
    return rq.get(base_url + 'backgrounds/'+background)
def get_languages(language=''):
    return rq.get(base_url + 'languages/' + language)
def get_skills(skill=''):
    return rq.get(base_url + 'skills/' + skill)
def get_features(features=''):
    return rq.get(base_url + 'features/' + features)
def get_proficiencies(proficiencie=''):
    return rq.get(base_url + 'proficiencies/' + proficiencie)
def get_feats(feat=''):
    return rq.get(base_url + 'feats/' + feat)

# ! dm
def get_rule_sections(rule):
    return rq.get(base_url + 'rule-sections/' + rule)
def get_rules(rule):
    return rq.get(base_url + 'rules/' + rule)
