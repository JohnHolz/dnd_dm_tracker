from jh_utils.utils.utils import print_dict
import sys
sys.path.append('../')
from db_interact import read_db, write_db, load_from_db

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

    def get_json(self):
        ret = dict()
        ret['name'] = self.name
        ret['equipment_category'] = self.equipment_category
        ret['description'] = self.description
        return ret

    def save_item(self,db_path):
        db = read_db(db_path)
        db[self.name] = self.get_json()
        write_db(db,db_path)


def dict_to_Item(item_dict):
    item = Item(item_dict['name'],item_dict['equipment_category'])
    item.description = item_dict['description']
    return item

def load_item(item_name, db_path):
    item_dict  = load_from_db(item_name, db_path)
    return dict_to_Item(item_dict)

def items_table(items_db_path):
    import pandas as pd
    db = read_db(items_db_path)
    item_names = list(db.keys())
    df = pd.DataFrame(pd.Series(item_names),columns=['Items'])
    df['equipment_category'] = df['Items'].apply(lambda x: db[x]['equipment_category'])
    return df