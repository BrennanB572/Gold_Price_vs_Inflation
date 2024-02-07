import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('Resources/RUBLE2US.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

columns_to_average = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]  ##STILL GETTING ERROR ON  "Vol." and "Change %"

average_annual_data = pd.DataFrame()

for column in columns_to_average:
    average_annual_data[column + '_Avg'] = df.groupby('Year')[column].mean()

print(average_annual_data)

# Creates a CSV file
average_annual_data.to_csv('RUSSIAN_averages.csv', header=True)