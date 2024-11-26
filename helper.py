import os
import json

# convet nominal data to numeric data
# model is json instance 
def convert_nominal_to_numeric(model):

    # this tree line will be deleted
    for item in model:
        print(item)
    print("___________________________________")


    # get mapping values from json file
    # current file path
    current_dir = os.path.dirname(__file__)
    mapping_path = os.path.join(current_dir, "resources", "mapping_nominal_tonumeric.json")

    # load mapping
    with open(mapping_path, 'r', encoding='utf-8') as file:
        mapping = json.load(file)    

    # initial model with numeric values -- empty list
    model_with_numeric_values = []

    # change nominal values to numeric values according to mapping
    for instance in model:
        processed_instance = {
            key: mapping[key][value] if key != "Day" else value for key, value in item.items()
        }
        model_with_numeric_values.append(processed_instance)


    for item in model_with_numeric_values:
        print(item)

