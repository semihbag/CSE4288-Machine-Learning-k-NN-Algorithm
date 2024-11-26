import os
import json
import helper as helper

"""
    This class is model class
    You can load previous models from json file
    You can store your current model into json file
""" 


# load the model
# if it was created before use it, if not create new one
def laod_model(k):

    # check whether model is exists and get model path
    model_path = check_model_exist_and_return_path(k)
    
    # load model
    with open(model_path, 'r', encoding='utf-8') as file:
        model = json.load(file)

    model = helper.convert_nominal_to_numeric(model)
    
    return model



# store model into memory
def store_model(model, k):
    
    # check whether model is exists and get model path
    model_path = check_model_exist_and_return_path(k)

    # store model into memory as json file
    with open(model_path, 'w', encoding='utf-8') as file:
        json.dump(model, file, ensure_ascii=False, indent=4)


    
# this fucntion checks whether model exist ot not
# retunr model path
def check_model_exist_and_return_path(k):
    # current file path
    current_dir = os.path.dirname(__file__)
    
    # set model path initial
    model_path_str = "model_k" + str(k) + ".json"
    model_path = os.path.join(current_dir, "resources", model_path_str)

    # set exact model path 
    if not os.path.exists(model_path):
        model_path = os.path.join(current_dir, "resources", "original_train_dataset.json")
    
    return model_path