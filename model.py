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
        if k % 2 == 0 :
            k = k + 1
            print(f"k value can not be even number! New k value: {k} (k = k + 1) ")
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
        print(f"Model loaded: {self.k}nn\n")



    # store model into memory
    def store_model(self):
        # convert numeric data to nominal data
        model = cn.convert_numeric_to_nominal(self.model)

        # store model into memory as json file
        model_path = self.pp.model_path(self.k)
        with open(model_path, 'w', encoding='utf-8') as file:
            json.dump(model, file, ensure_ascii=False, indent=4)

        print(f"Model stored: {self.k}nn\n")


    # this function handle classification part
    def train_with_knn(self, test_instance_list, distance_function):
        
        # this loop is classification process
        # initial classified instance list is empty
        classified_test_instance_list = []
        for test_instance in test_instance_list:

           # initial distance and PlayTennis list is empty
            neighbour_list = []
            for current_instance in self.model:
                distance = distance_function(current_instance, test_instance)
                neighbour = {
                    "distance" : distance,
                    "PlayTennis" : current_instance['PlayTennis']
                }
                neighbour_list.append(neighbour)

            # sorting the list according to the distance value
            neighbour_list.sort(key=lambda x: x['distance'])
            
            # first k neighbour
            nearest_neighbour_list = neighbour_list[:self.k]

            # summation of all PlayTennis values
            sum_play_tennis = sum(n['PlayTennis'] for n in nearest_neighbour_list)

            # set test instance label
            label = 1 if (sum_play_tennis > self.k / 2) else 0 

            # classified test instance
            classified_test_instance = {
                'Day': len(neighbour_list) + 1, 
                'Outlook': test_instance['Outlook'], 
                'Temperature': test_instance['Temperature'], 
                'Humidity': test_instance['Humidity'], 
                'Wind': test_instance['Wind'], 
                'PlayTennis': label
            }

            classified_test_instance_list.append(classified_test_instance)
            self.model.append(classified_test_instance)

            print(f"Test Instance: {test_instance}")
            print(f"Classified Test Instance: {classified_test_instance}")
            print(f"Classification: {label}\n")
            
        return classified_test_instance_list



    # this function returns instances data as integer array
    def return_instances_as_int_array(self,instances):

        data_array = []
        for instance in instances:
            data = []
            for key, value in instance.items():
                if key != 'Day':
                    data.append(value)
            data_array.append(data)

        return data_array