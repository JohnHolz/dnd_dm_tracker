import json

def read_db(file_path):
    file = open(file_path, "r")
    output = file.read()
    db = eval(output)
    return db

def write_db(dict,file_path):
    file_write = open(file_path, "w")
    json.dump(dict, file_write)
    file_write.close()

def load_from_db(key,db_file_path):
    db = read_db(db_file_path)
    dict_to_load = db[key]
    return dict_to_load