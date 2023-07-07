import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have the 'unicorn' DataFrame with columns: 'Country' and 'Total Raised ($B)'
unicorn = pd.read_csv('clean_unicorn.csv')

# Group the data by country and calculate the sum of total raised
country_totals = unicorn.groupby('Country')['Total Raised ($B)'].sum().reset_index()

# Sort the data in descending order based on the total raised
country_totals = country_totals.sort_values(by='Total Raised ($B)', ascending=True)

# Create the horizontal bar graph
plt.figure(figsize=(10, 6))  # Set the figure size
plt.barh(country_totals['Country'], country_totals['Total Raised ($B)'], color='blue')

# Add labels and title
plt.xlabel('Total Raised ($B)')
plt.ylabel('Country')
plt.title('Countries with the Highest Total Raised')

# Invert the y-axis to display the countries with the highest total raised at the top
# plt.gca().invert_yaxis()

# Show the plot
plt.show()

