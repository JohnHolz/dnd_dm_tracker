from jh_utils.utils.utils import to_print_list

class Item():
    """
    Item class
    equipment_category => ['Armor','Weapon','Mounts and Vehicles','Tools','Adventuring Gear','']
    """
    def __init__(self, 
                 name,
                 equipment_category,
                 description = None):
        self.name = name
        self.equipment_category = equipment_category
        self.description = []
        if description!=None:
            self.add_description(description)

    def __repr__(self):
        ret = f"""{self.name}
        {self.equipment_category}
        {to_print_list(self.description)}
        """
        return ret
            
    ##! type/tags
    def add_description(self, new_description):
        self.description = self.description + [new_description] 

    def get_item_json(self):
        ret = {self.name}
