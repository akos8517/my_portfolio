import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

unicorn = pd.read_csv('clean_unicorn.csv')

# Select the top 50 companies based on total raised
top_50 = unicorn.nlargest(50, 'Total Raised ($B)')

# Create an empty connectivity matrix
connectivity_matrix = np.zeros((len(top_50), len(top_50)), dtype=int)

# Fill the connectivity matrix based on shared countries
for i, company1 in enumerate(top_50['Company']):
    for j, company2 in enumerate(top_50['Company']):
        if company1 != company2:
            shared_countries = set(unicorn[unicorn['Company'] == company1]['Country']).intersection(
                unicorn[unicorn['Company'] == company2]['Country'])
            if shared_countries:
                # If there are shared countries, set the corresponding value in the connectivity matrix to 1
                connectivity_matrix[i, j] = 1

# Set the diagonal elements to 0 (no connection to itself)
np.fill_diagonal(connectivity_matrix, 0)

# Create a binary matrix for white color (0 for no connection, 1 for shared connection)
color_matrix = np.where(connectivity_matrix == 1, 1, 0)

# Draw the connectivity matrix as a heatmap with colors
plt.figure(figsize=(10, 10))
plt.imshow(color_matrix, cmap='Blues', vmin=0, vmax=1)
plt.title('Connectivity Matrix - Top 50 Companies')

# Set the tick labels to company names
plt.xticks(range(len(top_50)), top_50['Company'], rotation=90)
plt.yticks(range(len(top_50)), top_50['Company'])

plt.show()