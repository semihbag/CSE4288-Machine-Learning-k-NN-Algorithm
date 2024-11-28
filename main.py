import traceback
import model as ml
import converter as cn
import distance_calculator as dc
import visualizer

if __name__ == '__main__':
    
   
    model = ml.Model(k=7)

    model.laod_model()

    test_instance_list = [
        {
            "Outlook": "Sunny",
            "Temperature": "Cool",
            "Humidity": "Normal",
            "Wind": "Strong",
        }
    ]

    test_instance = cn.convert_nominal_to_numeric(test_instance_list)
    
    
    model.train_with_knn(test_instance, dc.euclidean)

    data = model.return_model_as_array()
    
    visualizer.visualize(data=data)
