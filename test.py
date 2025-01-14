import pickle
import numpy as np

model_path = 'final_random_forest_model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file)


test_input = np.array([[37.9,40.9,9.0,2.11,5.9],[18.4,16.6,7.3,1.04,10.2]])
predictions = model.predict(test_input)
print(predictions)