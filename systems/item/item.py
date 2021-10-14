from jh_utils.utils.utils import to_print_dict, to_print_list
from jh_utils.utils.mensages import get_line, line
line = '\n+-------------------------------+\n'
class Item():
    def __init__(self, 
                 name, 
                 subtitle='', item_type = '',
                 magical=False, unique = False, owner=None):
        self.name = name
        self.subtitle = subtitle
        self.description = description

        ## core info
        self.unique = unique
        self.item_type = ''
        self.tags = []
        
        self.owner = owner
        self.status = {}
        self.other_info = {}
        self.magical = magical
        if magical:
            self.special = {
                'special_habilities':{},
                'hidden_habilities':{}
            }


    def __repr__(self):
        unique = 'Unique' if self.unique else 'Non-unique'
        magical = 'Magical' if self.magical else 'Non-Magical'
        special = f'\nSpecial:{to_print_list(list(self.special["special_habilities"].keys()))}'
        hidden = f'\nHidden:{self.to_print_hidden()}'
        ret = f"""{self.name}
            type: {self.item_type}
            {magical} {unique}
            status:{to_print_dict(self.status)}{special}{hidden}"""
        return ret
        
    ## description
    def add_description(self, string:str):
        self.description = self.description + line + f'\n {string}'
    
    ##! type/tags
    def add_tag(self, new_tag):
        self.tags = self.tags + [new_tag] 

    ##! owner
    def set_owner(self, owner):
        self.owner = owner
    
    ##! Status
    def add_status(self, status_name, value):
        self.status[status_name] = value

    ##! other info
    def add_info(self, key, value):
        self.other_info[key] = value

    ##! add tag
    def add_tag(self, new_tag):
        self.tags = self.tags + [new_tag]

    ##! get events
    def get_events():
        pass

    def to_print_hidden(self):
        ret = ''
        hidden_habilities = self.special['hidden_habilities']
        for i in hidden_habilities.keys():
            ret = ret + f'{i} → block: {hidden_habilities[i]["block"]} \n       '
        return ret
    
    ##! Special
    def add_special_hability(self, hability):
        self.special['special_habilities'][hability.name] = hability

    def add_hidden_hability(self, hability, block):
        self.special['hidden_habilities'][hability.name]={'hability':hability, 'block':block}