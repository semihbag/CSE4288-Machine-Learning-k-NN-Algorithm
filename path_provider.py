import os

class PathProvider:
    
    # current dir
    current_dir = os.path.dirname(__file__)
    
    # original train datase path
    path_original_train_dataset = os.path.join(current_dir, "resources", "original_train_dataset.json")
   
    # nominal to numeric mapping path
    path_mapping_nominal_to_numeric = os.path.join(current_dir, "resources", "mapping", "mapping_nominal_to_numeric.json")

    # numeric to nominal mapping path
    path_mapping_numeric_to_nominal = os.path.join(current_dir, "resources", "mapping", "mapping_numeric_to_nominal.json")


    # create path for given model
    def model_path(self,k):
        return os.path.join(self.current_dir, "resources", "models", "model_k" + str(k) + ".json")
    
    # this fucntion checks whether model exist ot not
    # retunr model path
    def check_model_exist_and_return_path(self, k):

        # set model path initial
        model_path = self.model_path(k)

        # set exact model path 
        if not os.path.exists(model_path):
            model_path = os.path.join(self.current_dir, "resources", "original_train_dataset.json")
        
        return model_path
