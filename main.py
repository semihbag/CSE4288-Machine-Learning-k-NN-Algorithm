
import traceback
import model as ML

if __name__ == '__main__':
    
    # loan model from json file
    model = ML.laod_model(2)
    
    ML.store_model(model, 2)