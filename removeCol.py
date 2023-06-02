import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('./google.csv')  # Replace 'input.csv' with the path to your input CSV file

# Remove the columns you want to drop
columns_to_drop = ['Adj Close', 'Close', 'Date', 'Open']  # Replace 'Column1' and 'Column2' with the names of the columns you want to remove
data = data.drop(columns=columns_to_drop)

# Save the modified DataFrame back to a CSV file
data.to_csv('prediction.csv', index=False)