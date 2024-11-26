
import traceback
import model as ml

if __name__ == '__main__':
    
    # loan model from json file
    model = ml.laod_model(2)
    
    ml.store_model(model, 2)