from monetary_system import Money
{
    # ! basic
    'core': {
        'name': 'choosen fire',
        'class': 'novice',
        'lvl': 1,
        'race': 'human',
        'subraces': 'none',
        'languages': {'common'},
        'alignment': 'neutral',
        'background': 'soldier',
        'flaws': 'dump',
    },

    # ! appearance
    'appearance': {
        'age': 20,
        'size': 'medium',
        'height': 0,
        'weight': 0,
        'skin': 'bege',
        'eyes': 'brown',
        'hair': 'black',
    },

    'connections': {},

    # ! keep track
    'daily': {
        'gold': Money(),
        'hp': 0,
        'xp': 0,
    },

    # ! combat
    'combat': {
        'passive-perception': 11,
        'CA': 10,
        'initiative': 0,
    },

    # ! equipament
    'equipament': {
        'armor': {},
        'weapon': {},
        'itens': {},
    },
}
