import os
import json
import converter as cn
from path_provider import PathProvider

"""
    This class is model class
    You can load previous models from json file
    You can store your current model into json file
""" 
class Model:
    
    def __init__(self, k):
        
        # set k value
        self.k = k

        # set a path provider object
        self.pp = PathProvider()

        # initiate model
        self.model = ""



    # load the model
    # if it was created before use it, if not create new one
    def laod_model(self):
        # load model from json, if there no model create
        model_path = self.pp.check_model_exist_and_return_path(self.k)
        with open(model_path, 'r', encoding='utf-8') as file:
            model = json.load(file)

        # convert nominal data to numeric data
        model = cn.convert_nominal_to_numeric(model)
    
        self.model = model
        print(f"Model loaded: {self.k}nn")



    # store model into memory
    def store_model(self):
        # convert numeric data to nominal data
        model = cn.convert_numeric_to_nominal(self.model)

        # store model into memory as json file
        model_path = self.pp.model_path(self.k)
        with open(model_path, 'w', encoding='utf-8') as file:
            json.dump(model, file, ensure_ascii=False, indent=4)

        print(f"Model stored: {self.k}nn")



    def train(self):
        pass