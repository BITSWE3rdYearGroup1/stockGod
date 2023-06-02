import pandas as pd
from sklearn.linear_model import LinearRegression

import pickle
model = LinearRegression()
# Load the trained model
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

prediction_data = pd.read_csv('./prediction.csv')
X_pred = prediction_data[[  'High', 'Low', 'Volume']]  

prediction = model.predict(prediction_data);
print(prediction)
