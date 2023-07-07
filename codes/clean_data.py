import pandas as pd
unicorn = pd.read_csv("Unicorn_Companies.csv")

# Specify the columns to remove the dollar sign from
columns_to_clean = ['Valuation ($B)', 'Total Raised']

# Remove the dollar sign from the specified columns
for column in columns_to_clean:
    unicorn[column] = unicorn[column].str.replace('$', '', regex = False)

## For Total Raised column
# Function to convert symbols and "None" to numeric values
def convert_to_numeric(value):
    if value == "None":
        return 0
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}
    symbol = value[-1]
    if symbol in multipliers:
        actual_value = float(value[0:-1]) * multipliers[symbol]
        return actual_value / 1e9
    else:
        return float(value[0:]) / 1e9

# Apply the function to the 'Total Raised' column
unicorn['Total Raised'] = unicorn['Total Raised'].apply(convert_to_numeric)

# Modify Date Joined and Extract Year Joined only
date = unicorn['Date Joined'].str.split('/', expand = True)
unicorn['Year Joined'] = date[2]
unicorn['Year Joined'] = pd.to_numeric(unicorn['Year Joined'])
unicorn['Date Joined'] = pd.to_datetime(unicorn['Date Joined'])

# Rename the column "Select Inverstors" due to typo
unicorn = unicorn.rename({'Select Inverstors': 'Select Investors'}, axis=1)
unicorn = unicorn.rename({'Total Raised': 'Total Raised ($B)'}, axis=1)

# Modify City, Industry, and Select Investors
for i, row in unicorn.iterrows():
  if (row['Select Investors'] == 'None'):
    if i != 789:
      unicorn.at[i, "Industry"], unicorn.at[i, "Select Investors"] = unicorn.at[i, "Select Investors"], unicorn.at[i, "Industry"]
      unicorn.at[i, "City"], unicorn.at[i, "Industry"] = unicorn.at[i, "Country"], unicorn.at[i, "City"]

# Modify the value "Artificial Intelligence" and "Fintech" in Industry
unicorn['Industry'] = unicorn['Industry'].str.strip().replace('Finttech', 'Fintech', regex=False)
unicorn['Industry'] = unicorn['Industry'].str.strip().replace('Artificial Intelligence', 'Artificial intelligence', regex=False)

# Modify multiple columns to change from string into numeric values
columns_to_convert = ['Valuation ($B)', 'Investors Count', 'Deal Terms', 'Portfolio Exits']
unicorn[columns_to_convert] = unicorn[columns_to_convert].apply(pd.to_numeric, errors='coerce').fillna(0)

# Export csv file
unicorn.to_csv('clean_unicorn.csv', index=False)
