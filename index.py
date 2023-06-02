import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import pickle
# Load the dataset
data = pd.read_csv('./google.csv')

# Convert the 'Date' column to datetime
# data['Date'] = pd.to_datetime(data['Date'])

# Extract the features (e.g., date, volume, etc.) and target variable (closing price)
X = data[[ 'High', 'Low', 'Volume']]  # Include relevant features
# X['Date'] = X['Date'].astype(int) 
y = data['Close']  # Target variable

# Preprocess the data (if needed)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('R-squared Score:', r2)

with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)
