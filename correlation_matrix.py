import pandas as pd
import matplotlib.pyplot as plt

# Load the Unicorn dataset
unicorn = pd.read_csv('clean_unicorn.csv')

# Select the columns of interest for correlation analysis
columns_of_interest = ['Valuation ($B)', 'Total Raised ($B)', 'Investors Count', 'Deal Terms', 'Portfolio Exits']

# Subset the data with the selected columns
subset_data = unicorn[columns_of_interest]

# Calculate the Pearson correlation coefficient matrix
correlation_matrix = subset_data.corr()

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the correlation matrix
im = ax.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
fig.colorbar(im)

# Set the tick labels and axis labels
ax.set_xticks(range(len(columns_of_interest)))
ax.set_yticks(range(len(columns_of_interest)))
ax.set_xticklabels(columns_of_interest, rotation=90)
ax.set_yticklabels(columns_of_interest)
ax.set_xlabel('Columns')
ax.set_ylabel('Columns')

# Save the correlation matrix as a PNG image with larger size
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')

