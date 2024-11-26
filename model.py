import os
import json

# this class is model class

# load the model
# if it was created before use it, if not create new one
def laod_model(k):
    # current file path
    current_dir = os.path.dirname(__file__)
    
    # model path
    model_path_str = "model_k" + str(k) + ".json"
    model_path = os.path.join(current_dir, "resources", model_path_str)

    # check whether model is exists
    if not os.path.exists(model_path):  
        model_path = os.path.join(current_dir, "resources", "original_train_dataset.json")

    # load model or create new model
    with open(model_path, 'r', encoding='utf-8') as file:
        model = json.loads(file)



    
if __name__ == '__main__':
    
    laod_model(3)

