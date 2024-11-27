
import traceback
import model as ml

if __name__ == '__main__':
    
   
    model = ml.Model(2)

    model.laod_model()

    model.train_with_knn()
