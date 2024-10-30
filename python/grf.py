import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
total_data = pd.read_csv('cleaned_data.csv')

# Check the first few rows to understand the structure
print("Очищенные данные:")
print(total_data.head())

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a box plot to show the distribution of prices by location
plt.figure(figsize=(12, 6))  # Set the figure size
sns.boxplot(x='location', y='price', data=total_data)
plt.title('Зависимость цены от местоположения')
plt.xlabel('Местоположение')
plt.ylabel('Цена')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()  # Display the plot




# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the cleaned data
# total_data = pd.read_csv(r'cleaned_data.csv')
# print("Очищенные данные:")
# print(total_data.head())

# # Ensure that the relevant columns exist
# # Replace 'price' and 'floor' with the actual column names in your DataFrame
# price_column = 'price'  # Change this to your actual price column name
# floor_column = 'floor'   # Change this to your actual floor column name

# # Check if the necessary columns are present
# if price_column in total_data.columns and floor_column in total_data.columns:
#     # Create a new DataFrame with average price per floor
#     price_floor_relationship = total_data.groupby(floor_column)[price_column].mean().reset_index()
#     price_floor_relationship.columns = [floor_column, 'average_price']  # Rename columns for clarity

#     # Print the new DataFrame
#     print("Зависимость цены от этажа:")
#     print(price_floor_relationship)

#     # Optionally, visualize the relationship
#     plt.figure(figsize=(10, 6))
#     sns.barplot(data=price_floor_relationship, x=floor_column, y='average_price', palette='viridis')
#     plt.title('Средняя цена по этажам')
#     plt.xlabel('Этаж')
#     plt.ylabel('Средняя цена')
#     plt.xticks(rotation=45)
#     plt.show()
# else:
#     print(f"Не найдены необходимые столбцы: '{price_column}' или '{floor_column}'.")

# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the cleaned data
# total_data = pd.read_csv(r'cleaned_data.csv')
# print("Очищенные данные:")
# print(total_data.head())

# # Check the data types of each column
# print("Типы данных в DataFrame:")
# print(total_data.dtypes)

# # Encode the "location" column if it exists
# if 'location' in total_data.columns:
#     location_dummies = pd.get_dummies(total_data['location'], prefix='location', drop_first=True)
#     total_data = pd.concat([total_data, location_dummies], axis=1)
#     total_data.drop('location', axis=1, inplace=True)  # Optionally drop the original 'location' column

# # Convert all columns to numeric where possible
# # This will help identify non-numeric columns
# total_data_numeric = total_data.select_dtypes(include=[np.number])

# # Create a correlation matrix only for numeric columns
# correlation_matrix = total_data_numeric.corr()

# # Print the correlation matrix
# print("Корреляционная таблица:")
# print(correlation_matrix)

# # Visualize the correlation matrix using a heatmap
# plt.figure(figsize=(12, 8))  # Set the figure size
# sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
# plt.title('Корреляционная таблица')
# plt.show()  # Display the heatmap

# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the cleaned data
# total_data = pd.read_csv(r'cleaned_data.csv')
# print("Очищенные данные:")
# print(total_data.head())

# # Create a histogram for a specific numerical column
# # Replace 'year_of_construction' with the column you want to visualize
# plt.figure(figsize=(10, 6))  # Set the figure size
# sns.histplot(total_data['year_of_construction'], bins=30, kde=True)  # kde=True adds a kernel density estimate
# plt.title('Гистограмма года постройки')
# plt.xlabel('Год постройки')
# plt.ylabel('Частота')
# plt.grid(True)
# plt.show()  # Display the histogram