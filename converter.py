import os
import json

# convet nominal data to numeric data
# model is json instance 
def convert_nominal_to_numeric(model):

    # get mapping values from json file
    # current file path
    current_dir = os.path.dirname(__file__)
    mapping_path = os.path.join(current_dir, "resources", "mapping_nominal_to_numeric.json")

    # load mapping
    with open(mapping_path, 'r', encoding='utf-8') as file:
        mapping = json.load(file)    

    # initial model with numeric values -- empty list
    model_with_numeric_values = []

    # change nominal values to numeric values according to mapping
    for instance in model:
        processed_instance = {
            key: mapping[key][value] if key != "Day" else value for key, value in instance.items()
        }
        model_with_numeric_values.append(processed_instance)

    return model_with_numeric_values


# convert numeric data to nominal data
# model is json instance
def convert_numeric_to_nominal(model):
    
    # get mapping values from json file
    # current file path
    current_dir = os.path.dirname(__file__)
    mapping_path = os.path.join(current_dir, "resources", "mapping_numeric_to_nominal.json")

    # load mapping
    with open(mapping_path, 'r', encoding='utf-8') as file:
        mapping = json.load(file)   
    pass

    # initial model with numeric values -- empty list
    model_with_nominal_values = []

    # change numeric values to nominal values according to mapping
    for instance in model:
        processed_instance = {
            key: mapping[key][str(value)] if key != "Day" else value for key, value in instance.items()
        }
        model_with_nominal_values.append(processed_instance)

    return model_with_nominal_values
