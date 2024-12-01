import traceback
import model as ml
import converter as cn
import distance_calculator as dc
import visualizer

if __name__ == '__main__':
    
    # initiate model witk k value
    model = ml.Model()

    # load model
    model.laod_model()

    # classifing
    # two types of distance calculation method:
    #   -eclidean
    #   -manhattan
    # select one, and give as parameter
    model.classify_with_knn(k=3, distance_function=dc.euclidean)

    # evaluet and log
    model.evaluate_models_and_log()

    # store model
    model.store_model()

    # int data of model, required for visualize
    data = model.return_instances_as_int_array(model.training_data_set)
    
    # visualize
    visualizer.visualize(data=data)
