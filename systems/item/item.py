from jh_utils.utils.utils import to_print_dict
line = '\n+-------------------------------+\n'

class Item():
    def __init__(self, 
                 name, 
                 description='', item_type = '',
                 magical=False, unique = False, owner=None):
        self.name = name
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
            self.magical = {
                'special_habilities':{},
                'hidden_habilities':{}
            }


    def __repr__(self):
        if self.magical:
            magical_repr = f"""\nmagical:{to_print_dict(self.magical)}\n"""
        ret = f"""{self.name}
            unique:  {self.unique}
            type:    {self.item_type}
            
            status: {to_print_dict(self.status)} {magical_repr}
            
            description
            {self.description}
            """
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
        
    ##! Special
    def add_special_hability(self, hability):
        self.magical['special_habilities'][hability.name] = hability

    def add_hidden_hability(self, hability, block):
        self.magical['hidden_habilities'][hability.name]={'hability':hability, 'block':block}