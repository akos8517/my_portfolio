import pandas as pd
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the clean_unicorn.csv dataset
unicorn = pd.read_csv('clean_unicorn.csv')

# Filter the data for only United States
unicorn_us = unicorn[unicorn['Country'] == 'United States']

# Modify the columns 'Total Raised' and 'Valuation' to actual values
unicorn_us['Total Raised ($B)'] *= 1e9
unicorn_us['Valuation ($B)'] *= 1e9

# Separate the features from the labels
X = unicorn_us[['Valuation ($B)', 'Total Raised ($B)', 'Investors Count', 'Deal Terms', 'Portfolio Exits']]
y = unicorn_us['Industry']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply t-SNE to reduce the dimensionality to 2D
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_scaled)

# Get unique industry categories and assign colors
unique_industries = y.unique()
num_industries = len(unique_industries)
colors = plt.cm.tab20(range(num_industries))

# Create a scatter plot of the t-SNE representation
scatter_handles = []
for i, industry in enumerate(unique_industries):
    scatter = plt.scatter(X_tsne[y == industry, 0], X_tsne[y == industry, 1], color=colors[i], label=industry)
    scatter_handles.append(scatter)

# Add legend outside of the plot
plt.legend(handles=scatter_handles, bbox_to_anchor=(1.04, 1), loc='upper left')

# Add title and axis labels
plt.title('Relationship between Unicorn companies by t-SNE in the United States')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')

# Adjust the figure size to accommodate the legend
fig = plt.gcf()
fig.set_size_inches(8, 6)

# Show the plot
plt.tight_layout()
plt.show()
