

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the Advertisement data
df = pd.read_csv('/home/Advertising.csv')

# Print column names to check for any discrepancies
print("Column Names:", df.columns)

# Step 2: View the top rows of the dataframe to inspect the data
print("Top Rows of DataFrame:")
print(df.head())

# Step 3: Select the first 7 observations and the columns TV and Sales (adjust based on actual column names)
df_subset = df.iloc[:7][['TV', 'Sales']]

# Verify that the subset contains 7 rows
assert df_subset.shape[0] == 7, 'Expected 7 rows'

# Step 4: Create a scatter plot
plt.scatter(df_subset['TV'], df_subset['Sales'])
plt.xlabel('TV Budget')
plt.ylabel('Sales')
plt.title('Scatter Plot of TV Budget vs Sales')

# Step 5: Display the plot
plt.show()

# Step 6: Create a new DataFrame named df_new
df_new = df[['TV', 'Sales']]
