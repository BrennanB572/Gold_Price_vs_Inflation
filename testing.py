import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV files and convert them into DataFrames
Annual_Gold_Value_In_Rubles_df = pd.read_csv('Resources/output_Annual_Gold_Value_In_Rubles.csv')
Inflation_rates_2013_2021_df = pd.read_csv('Resources/inflation_rates_2013-2021.csv')

# Filter inflation rates for currency "RUB"
inflation_rates_rub_df = Inflation_rates_2013_2021_df[Inflation_rates_2013_2021_df['currency'] == 'RUB']

# Merge data based on the "year" column
merged_df = pd.merge(Annual_Gold_Value_In_Rubles_df, inflation_rates_rub_df, how='inner', left_on='Year', right_on='year')

# Define a function to calculate percent change
def calculate_percent_change(data, value_column):
    percent_change = {}
    for i in range(1, len(data)):
        old_value = data[value_column].iloc[i - 1]
        new_value = data[value_column].iloc[i]
        change = ((new_value - old_value) / old_value) * 100
        percent_change[data['Year'].iloc[i]] = change
    return percent_change

# Calculate percent change in gold value year over year
percent_change_gold = calculate_percent_change(merged_df, 'Gold_Value_In_Rubles')

# Calculate percent change in inflation rates year over year
percent_change_inflation = calculate_percent_change(inflation_rates_rub_df, 'year', 'inflation rate')

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot percent change in gold value
plt.plot(percent_change_gold.keys(), percent_change_gold.values(), marker='o', linestyle='-', label='Gold Value')

# Plot percent change in inflation rates
plt.plot(percent_change_inflation.keys(), percent_change_inflation.values(), marker='o', linestyle='-', label='Inflation Rate')

# Adding labels and title
plt.title('Percent Change in Gold Value and Inflation Rate Over Years')
plt.xlabel('Year')
plt.ylabel('Percent Change (%)')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.xticks(list(percent_change_gold.keys()))
plt.tight_layout()
plt.show()
