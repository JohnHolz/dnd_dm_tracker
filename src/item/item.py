from jh_utils.utils.utils import print_dict

class Item():
    """
    Item class
    equipment_category => ['Armor','Weapon','Mounts and Vehicles','Tools','Adventuring Gear','']
    """
    def __init__(self, 
                 name,
                 equipment_category,
                 appearence = None):
        self.name = name
        self.equipment_category = equipment_category
        self.description = {}
        if appearence!=None:
            self.add_description('appearence',appearence)

    def __repr__(self):
        return f"""{self.name}, {self.equipment_category}"""
            
    ##! type/tags
    def add_description(self, description_type, description_string):
        if description_type not in self.description.keys():
            self.description[description_type] = [description_string]
        else:
            self.description[description_type] = self.description[description_type] + [description_string]
 
    def print_description(self):
        print_dict(self.description)

    def get_item_json(self):
        ret = dict()
        ret['name'] = self.name
        ret['equipment_category'] = self.equipment_category
        ret['description'] = self.description
        return ret

def get_item(item_name):
    "read the db in world and return an item"
    return item_name