import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the file that we will clean later
df = pd.read_csv(r'C:\Users\User\Desktop\VV\merged_file.csv') 
print("Исходные данные:")
print(df.head())

# Remove rows that will not affect the statistics
columns_to_drop = ['author', 'author_type', 'url', 'phone']
df_cleaned = df.drop(columns=columns_to_drop, errors='ignore')

# Function to replace "Москква" with "Москва" in a specified column
def replace_moscow_name(dataframe, column_name):
    if column_name in dataframe.columns:
        dataframe[column_name] = dataframe[column_name].replace("Москква", "Москва")

# Function to remove the "object_type" column
def remove_object_type_column(dataframe):
    return dataframe.drop(columns=['object_type'], errors='ignore')

# Function to remove the "house_material_type" column
def remove_house_material_type_column(dataframe):
    return dataframe.drop(columns=['house_material_type'], errors='ignore')

# Function to remove the "heating_type" column
def remove_heating_type_column(dataframe):
    return dataframe.drop(columns=['heating_type'], errors='ignore')

# Function to remove the "finish_type" column
def remove_finish_type_column(dataframe):
    return dataframe.drop(columns=['finish_type'], errors='ignore')

# Replace "Москква" with "Москва" in the 'location' column
replace_moscow_name(df_cleaned, 'location')

# Remove the "object_type" column
df_cleaned = remove_object_type_column(df_cleaned)

# Remove the "house_material_type" column
df_cleaned = remove_house_material_type_column(df_cleaned)

# Remove the "heating_type" column
df_cleaned = remove_heating_type_column(df_cleaned)

# Remove the "finish_type" column
df_cleaned = remove_finish_type_column(df_cleaned)

# Create a new file and add the cleaned data to it
df_cleaned.to_csv(r'cleaned_data.csv', index=False)

# Function to remove rows with missing values in "year_of_construction"
def remove_rows_with_missing_year(dataframe):
    return dataframe.dropna(subset=['year_of_construction'])

# Remove rows with missing values in "year_of_construction"
df_cleaned = remove_rows_with_missing_year(df_cleaned)

# Replace non-numeric values with NaN (or handle them as needed)
df_cleaned['year_of_construction'] = pd.to_numeric(df_cleaned['year_of_construction'], errors='coerce')

# Remove rows with missing values in "year_of_construction" again after conversion
df_cleaned = remove_rows_with_missing_year(df_cleaned)

# Convert 'year_of_construction' to integer type
df_cleaned['year_of_construction'] = df_cleaned['year_of_construction'].astype(int)

# Check for missing values
missing_percentages = df_cleaned.isna().mean() * 100 
print("Проценты пропущенных значений по столбцам:") 
print(missing_percentages)

# Check for duplicates
duplicate_count = df_cleaned.duplicated().sum()
print(f"Количество дубликатов после удаления: {duplicate_count}")

# Save the cleaned data
df_cleaned.to_csv(r'cleaned_data.csv', index=False)

# Load the cleaned data
total_data = pd.read_csv('cleaned_data.csv')
print("Очищенные данные:")
print(total_data.head())