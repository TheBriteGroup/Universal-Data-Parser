#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from IPython.display import display, HTML

# Load the CSV file from a specified path
file_path = r"C:\Users\robel\Desktop\final_product_data.csv"
data_df = pd.read_csv(file_path)

# Define a function to determine if a serial number's format is improper
def is_improper_format(serial):
    if pd.isnull(serial):
        return False
    return not (len(serial) == 4 and serial[:2].isdigit() and serial[2:].isalpha())

# Define a function to check if the serial number is missing
def is_missing_data(serial):
    return pd.isnull(serial)

# Apply the 'is_improper_format' function to each serial number in the dataframe to identify improper formats
data_df['Improper Data Structure'] = data_df['Serial Number'].apply(is_improper_format)

# Apply the 'is_missing_data' function to identify missing serial numbers
data_df['Missing Serial Number'] = data_df['Serial Number'].apply(is_missing_data)

# Create a dataframe for rows where the serial number is missing
missing_serial_numbers_df = data_df[data_df['Missing Serial Number']]

# Create a separate dataframe for rows with an improper data structure, excluding those with missing serial numbers
improper_data_structure_df = data_df[data_df['Improper Data Structure'] & ~data_df['Missing Serial Number']]

# Function to display DataFrame as HTML
def display_html(df, title):
    display(HTML(f"<h2>{title}</h2>"))
    display(HTML(df.to_html(index=False)))

# Display the dataframe containing rows with missing serial numbers
display_html(missing_serial_numbers_df, "Rows with Missing Serial Numbers")

# Display the dataframe containing rows with improper data structure
display_html(improper_data_structure_df, "Rows with Improper Data Structure")


# In[ ]:




