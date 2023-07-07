import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

unicorn = pd.read_csv('clean_unicorn.csv')  # Assuming the dataset is in a CSV file

# Extract the last 10 years of data
current_year = pd.to_datetime('today').year
last_10_years_unicorn = unicorn[unicorn['Year Joined'] >= current_year - 10].copy()

# Convert "Year Joined" to integer type using .loc indexer
last_10_years_unicorn.loc[:, 'Year Joined'] = last_10_years_unicorn['Year Joined'].astype(int)

# Group by "Year Joined" and "Country" and calculate the total raised
grouped_data = last_10_years_unicorn.groupby(['Year Joined', 'Country'])['Total Raised ($B)'].sum().reset_index()

# Calculate rankings within each year based on total raised
grouped_data['Ranking'] = grouped_data.groupby('Year Joined')['Total Raised ($B)'].rank(ascending=False, method='min')

# Filter the data to include rankings 1 to 10 only
filtered_data = grouped_data[grouped_data['Ranking'].between(1, 10)]

# Create a pivot table to reshape the data for heatmap
pivot_data = filtered_data.pivot(index='Ranking', columns='Year Joined', values='Country')

# Sort the columns by year
pivot_data = pivot_data.reindex(sorted(pivot_data.columns), axis=1)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Get unique countries and assign colors using multiple palettes
unique_countries = filtered_data['Country'].unique()
num_countries = len(unique_countries)

palettes = ['Paired', 'Set3', 'gist_ncar']
colors_per_palette = num_countries // len(palettes)
colors_remainder = num_countries % len(palettes)

colors = []

# Assign colors from each palette
for i, palette in enumerate(palettes):
    if i < colors_remainder:
        colors += sns.color_palette(palette, colors_per_palette + 1)
    else:
        colors += sns.color_palette(palette, colors_per_palette)

country_color_map = {country: color for country, color in zip(unique_countries, colors)}

# Convert country names to numeric values
country_numeric_map = {country: i for i, country in enumerate(unique_countries)}

# Convert pivot_data to numeric values and replace missing values with placeholder
pivot_data_numeric = pivot_data.applymap(lambda x: country_numeric_map.get(x, -1))

# Create a custom colormap with unique colors for each country
cmap = mcolors.ListedColormap(colors)

# Create the heatmap using seaborn
sns.heatmap(pivot_data_numeric, cmap=cmap, annot=pivot_data, fmt='', ax=ax, cbar_kws={'orientation': 'horizontal'})

# Add borders to each cell
for _, spine in ax.spines.items():
    spine.set_visible(True)

# Add gridlines
ax.set_xticks(range(len(pivot_data.columns)))
ax.set_yticks(range(len(pivot_data) + 1))
ax.set_xticklabels(pivot_data.columns, rotation=0, ha='left')

# Set the title
ax.set_title('Top 10 Countries by Total Raised From 2013 - 2022')

# Set the y-axis limits and labels
ax.set_ylim(len(pivot_data), 0)  # Adjust y-axis limits to place labels between boxes
ax.set_yticks(range(1, len(pivot_data) + 1))
ax.set_yticklabels(list(pivot_data.index), va='top', rotation = 'horizontal')  # Display ranking numbers as y-axis labels
ax.yaxis.set_tick_params(pad=30)  # Adjust padding for y-axis labels
ax.set_ylabel('Ranking')

# Format y-axis labels as integers without decimal places
ax.yaxis.set_major_formatter('{x:.0f}')

# Show the plot
plt.tight_layout()
plt.show()
