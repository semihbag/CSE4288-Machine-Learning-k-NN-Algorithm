import json
from path_provider import PathProvider as pp

# convet nominal data to numeric data
# model is json instance 
def convert_nominal_to_numeric(model):

    # load mapping
    mapping_path = pp.path_mapping_nominal_to_numeric
    with open(mapping_path, 'r', encoding='utf-8') as file:
        mapping = json.load(file)    

    # change nominal values to numeric values according to mapping
    # initial model with numeric values -- empty list
    model_with_numeric_values = []
    for instance in model:
        processed_instance = {
            key: mapping[key][value] if key != "Day" else value for key, value in instance.items()
        }
        model_with_numeric_values.append(processed_instance)

    return model_with_numeric_values


# convert numeric data to nominal data
# model is json instance
def convert_numeric_to_nominal(model):
    
    # load mapping
    mapping_path = pp.path_mapping_numeric_to_nominal

    with open(mapping_path, 'r', encoding='utf-8') as file:
        mapping = json.load(file)   

    # change numeric values to nominal values according to mapping
    # initial model with numeric values -- empty list
    model_with_nominal_values = []
    for instance in model:
        processed_instance = {
            key: mapping[key][str(value)] if key != "Day" else value for key, value in instance.items()
        }
        model_with_nominal_values.append(processed_instance)

    return model_with_nominal_values
