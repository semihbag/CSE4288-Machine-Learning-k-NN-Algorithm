import json
import converter as cn
from path_provider import PathProvider

"""
    This class is model class
    You can load previous models from json file
    You can store your current model into json file
""" 
class Model:
    
    def __init__(self):
    
        # set a path provider object
        self.pp = PathProvider()

        # initiate model
        self.training_data_set = ""

        # initiate prediction list
        self.model_data = []

        # initiate evaluated model data
        # this data will be stored as json
        self.evaluated_model_data_list = []


    # load the model
    # if it was created before use it, if not create new one
    def laod_model(self):
        # load model from json, if there no model create
        model_path = self.pp.path_original_train_dataset
        with open(model_path, 'r', encoding='utf-8') as file:
            dataset = json.load(file)

        # convert nominal data to numeric data
        dataset = cn.convert_nominal_to_numeric(dataset)
    
        self.training_data_set = dataset
        print(f"Model loaded: Dataset: {self.pp.path_original_train_dataset}\n")



    # store model into memory
    def store_model(self):

        for model in self.evaluated_model_data_list:
            # convert numeric data to nominal data
            model['ClassifiedInstances']['TestData'] = cn.convert_numeric_to_nominal(model['ClassifiedInstances']['TestData'])

            # store model into memory as json file
            model_path = self.pp.model_path(model['k'], model['DistanceFunc'])
            with open(model_path, 'w', encoding='utf-8') as file:
                json.dump(model, file, ensure_ascii=False, indent=4)

            print(f"Model stored: {self.k}nn\n")


    # this function handle classification part
    def classify_with_knn(self, k, distance_function):

        # check k value
        if k % 2 == 0 :
            k = k + 1
            print(f"k value can not be even number! New k value: {k} (k = k + 1) ")
        
        # this loop is classification process
        # initial classified instance list is empty
        classified_test_instance_data = []
        for test_instance in self.training_data_set:

           # initial distance and PlayTennis list is empty
            neighbour_list = []
            for current_instance in self.training_data_set:
                # do not test with same instance
                if test_instance['Day'] == current_instance['Day']:
                    continue
                distance = distance_function(current_instance, test_instance)
                neighbour = {
                    "distance" : distance,
                    "PlayTennis" : current_instance['PlayTennis']
                }
                neighbour_list.append(neighbour)

            # sorting the list according to the distance value
            neighbour_list.sort(key=lambda x: x['distance'])
            
            # first k neighbour
            nearest_neighbour_list = neighbour_list[:k]

            # summation of all PlayTennis values
            sum_play_tennis = sum(n['PlayTennis'] for n in nearest_neighbour_list)

            # set test instance label
            label = 1 if (sum_play_tennis > k / 2) else 0 

            # classified test instance
            classified_test_instance = {
                'Prediction' : label,
                'ActualClass': test_instance['PlayTennis'],
                'TestData' : test_instance,
                'KNearestNeighbourList' : nearest_neighbour_list
            }

            classified_test_instance_data.append(classified_test_instance)

           # print(f"Test Instance: {test_instance}")
           # print(f"Classified Test Instance: {classified_test_instance}")
           # print(f"Classification: {label}\n")
        

        self.model_data.append((classified_test_instance_data, k, distance_function.__name__))  



    def evaluate_models_and_log(self):
        for classified_instances, k, distance_function in self.model_data:
            tp = fp = tn = fn = 0
            
            for instance in classified_instances:
                prediction = instance['Prediction']
                actual = instance['ActualClass'] 

                if prediction == 1 and actual == 1:
                    tp += 1
                elif prediction == 1 and actual == 0:
                    fp += 1
                elif prediction == 0 and actual == 0:
                    tn += 1
                elif prediction == 0 and actual == 1:
                    fn += 1

            accuracy = (tp + tn) / (tp + tn + fp + fn)

            evaluated_model_data = {
                "k" : k,
                "DistanceFunc" : distance_function,
                "ConfusionMatrix" : {
                    "TruePositive" : tp,
                    "FalsePositive" : fp,
                    "TrueNegative" : tn,
                    "FalseNegative" : fn 
                },
                "Accuracy" :accuracy,
                "ClassifiedInstances" : classified_instances
            }

            self.evaluated_model_data_list.append(evaluated_model_data)

            print("---LOGS---")
            print(f"KNN Model with k: {k}")
            print(f"Confusion Matrix:")
            print(f"  TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")
            print(f"Accuracy: {accuracy:.2f}\n")


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