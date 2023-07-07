import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have the 'unicorn' DataFrame with the 'Country' column
unicorn = pd.read_csv('clean_unicorn.csv')

# Count the number of companies in each country
country_counts = unicorn['Country'].value_counts()

# Sort the data in descending order based on the number of companies
country_counts = country_counts.sort_values(ascending=True)

# Create the horizontal bar graph
plt.figure(figsize=(10, 6))  # Set the figure size
plt.barh(country_counts.index, country_counts.values, color='blue')

# Add labels and title
plt.xlabel('Number of Companies')
plt.ylabel('Country')
plt.title('Number of Companies in Each Country')

# Show the plot
plt.show()
