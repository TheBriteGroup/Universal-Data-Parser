#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd  # Import the pandas library for data manipulation
import numpy as np  # Import the numpy library for numerical operations
from IPython.display import display, HTML  # Import display and HTML for better Jupyter notebook output

def load_and_analyze_data(file_path):
    """Loads data and analyzes missing values."""
    df = pd.read_csv(file_path)  # Load the CSV file into a DataFrame
    print(f"Analyzing {file_path}...")  # Print a message indicating which file is being analyzed
    missing_values = df.isnull().sum()  # Calculate the sum of missing values for each column
    for column, count in missing_values.items():  # Loop through each column and its missing values count
        print(f"{column}: {count} missing value{'s' if count != 1 else ''}")  # Print the count of missing values per column
    return df  # Return the DataFrame

def fill_missing_values(df, strategy='mean'):
    """Fills missing values based on the specified strategy."""
    if strategy == 'mean':  # Check if the strategy is 'mean'
        return df.fillna(df.mean())  # Fill missing values with the mean of each column
    elif strategy == 'median':  # Check if the strategy is 'median'
        return df.fillna(df.median())  # Fill missing values with the median of each column
    elif strategy == 'mode':  # Check if the strategy is 'mode'
        # Note: mode() returns a DataFrame, so we use iloc to select the first mode if there are multiple
        return df.fillna(df.mode().iloc[0])  # Fill missing values with the mode of each column
    else:
        raise ValueError(f"Unknown filling strategy: {strategy}")  # Raise an error if an unknown strategy is provided

def validate_filled_data(df):
    """Validates filled data to ensure it's within expected ranges."""
    if df.isnull().values.any():  # Check if there are still any missing values
        raise ValueError("Data still contains missing values after filling.")  # Raise an error if missing values are found
    print("Validation passed: No missing values found.")  # Print a message if validation passes

def main():
    base_path = "C:/Users/robel/OneDrive/Documents/Data Quality"  # Set the base path for the files
    files = ['data_quality_python1.csv', 'data_quality_python2.csv', 'data_quality_python3.csv']  # List of files to process
    for file in files:  # Loop through each file
        full_path = f"{base_path}/{file}"  # Construct the full file path
        df = load_and_analyze_data(full_path)  # Load and analyze the data
        print("Sample data before processing:")  # Print a message before showing a sample of the data
        display(HTML(df.head(20).to_html()))  # Display the first 20 rows of the DataFrame as HTML
        # Decide on filling strategy (mean, median, mode, etc.)
        filling_strategy = 'mean'  # Set the filling strategy
        filled_df = fill_missing_values(df, strategy=filling_strategy)  # Fill missing values according to the chosen strategy
        validate_filled_data(filled_df)  # Validate the filled DataFrame
        # Optionally, save the filled DataFrame back to a CSV
        filled_df.to_csv(f'{base_path}/filled_{file}', index=False)  # Save the filled DataFrame to a new CSV file
        print(f"Filled missing values using {filling_strategy} strategy and saved to filled_{file}")  # Print a success message

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly


# In[ ]:





# In[ ]:




