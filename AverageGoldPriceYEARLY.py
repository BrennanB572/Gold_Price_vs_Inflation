
import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('archive/Gold Price (2013-2023).csv')  
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

columns_to_average = ["Price", "Open", "High", "Low", "Vol.", "Change %"]  ##STILL GETTING ERROR ON  "Vol." and "Change %"

for column in columns_to_average:
    df[column] = df[column].str.replace(',', '', regex=True)  # Remove commas in order to make cells numerical
    df[column] = pd.to_numeric(df[column], errors='coerce')  # Convert to numeric, replace non-numeric values with NaN ### this is showing the issues is still on "Vol." and "Change %"

average_annual_data = pd.DataFrame()

for column in columns_to_average:
    average_annual_data[column + '_Avg'] = df.groupby('Year')[column].mean()

print(average_annual_data)

# Creates a CSV file
average_annual_data.to_csv('average_annual_gold_prices.csv', header=True)