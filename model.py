import os
import json
import converter as cn
from path_provider import PathProvider

"""
    This class is model class
    You can load previous models from json file
    You can store your current model into json file
""" 

# set a path provider object
pp = PathProvider()

# load the model
# if it was created before use it, if not create new one
def laod_model(k):

    # load model from json, if there no model create
    model_path = pp.check_model_exist_and_return_path(k)
    with open(model_path, 'r', encoding='utf-8') as file:
        model = json.load(file)

    # convert nominal data to numeric data
    model = cn.convert_nominal_to_numeric(model)
   
    return model



# store model into memory
def store_model(model, k):
    
    # convert numeric data to nominal data
    model = cn.convert_numeric_to_nominal(model)

    # store model into memory as json file
    model_path = pp.model_path(k)
    with open(model_path, 'w', encoding='utf-8') as file:
        json.dump(model, file, ensure_ascii=False, indent=4)
