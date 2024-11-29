import traceback
import model as ml
import converter as cn
import distance_calculator as dc
import visualizer

if __name__ == '__main__':
    
    # initiate model witk k value
    model = ml.Model(k=1)

    # load model
    model.laod_model()

    # give test instance as list (one or more)
    test_instance_list = [
        {
            "Outlook": "Sunny",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Wind": "Strong",
        },
        {
            "Outlook": "Rain",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Wind": "Strong",
        }
    ]

    # conver nominal values to numeric, because of calculation
    test_instance_list = cn.convert_nominal_to_numeric(test_instance_list)
    
    # training
    # two types of distance calculation method:
    #   -eclidean
    #   -manhattan
    # select one, and give as parameter
    model.train_with_knn(test_instance_list=test_instance_list, distance_function=dc.euclidean)

    # store model
    model.store_model()

    # int data of model, required for visualize
    data = model.return_instances_as_int_array(model.model)
    
    # visualize
    no_test_instances = len(test_instance_list)
    visualizer.visualize(data=data, no_test_instances=no_test_instances)
