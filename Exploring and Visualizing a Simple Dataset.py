# Load the dataset using the pandas library. 
import pandas as pd # This line brings in a library called pandas. 
                    # Think of pandas as your main tool for handling data (tables, CSV files, spreadsheets).
                    # as pd is just a shortcut name.

# Load the iris dataset from the available CSV file
iris_df = pd.read_csv('/content/iris.csv') # pd.read_csv() → tells Python: “Go read a CSV file”
                                           # '/content/iris.csv' → the file path (where your dataset is stored)
                                           # iris_df → a variable where the data is stored (Variable name)

# Display the first few rows of the DataFrame to confirm loading
print("Dataset loaded successfully!")
print(iris_df.head())  # .head() → shows the first 5 rows of your dataset

# ---------------------------------------------------- #
# Display dataset structure using .shape, .columns, and .head(). 

# .shape Display the shape of the DataFrame (rows, columns)
print("DataFrame Shape:", iris_df.shape)

# .column Display the column names and .tolist converts them into a normal Python list
print("\nColumn Names:", iris_df.columns.tolist())

# Display the first 5 rows again (as requested, even though head() was used before)
print("\nFirst 5 Rows (using .head()):") # \n = new line (creates space between lines)
print(iris_df.head())

#----------------------------------------------------- #
# Create Scatter plot to analyze relationships between variables. 

import matplotlib.pyplot as plt # used for plotting controls (figure, labels, show)
import seaborn as sns # seaborn → built on top of matplotlib, cleaner and smarter visuals
                      # used for advanced plots like scatterplot

# Create a scatter plot to visualize the relationship between sepal_length and sepal_width
plt.figure(figsize=(8, 6)) # Creates a blank space for your plot
                           # figsize=(8, 6) → width = 8 inches, height = 6 inches
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris_df, s=80, alpha=0.7)
                # "hue" gives different color to different species
                # "s" means size of the dot
                # "alpha" means Transparency (0 = invisible, 1 = solid)
plt.title('Scatter Plot of Sepal Length vs. Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.grid(True, linestyle='--', alpha=0.6) # adds lines to the graph
plt.show()                                # non-negotiable: Without it → nothing appears

# ---------------------------------------------------- #
# Histogram to examine data distribution. 

import matplotlib.pyplot as plt
import seaborn as sns

# Create a histogram for sepal_length to visualize its distribution
plt.figure(figsize=(8, 6))
sns.histplot(iris_df['sepal_length'], kde=True, bins=10, color='skyblue')
                # "iris_df" is the variable name which stores the data and "sepal_length" is one column selected to draw histogram for.
                # "bins" Splits data into 10 intervals
                # "kde" adds smooth curve that estimates the probability distribution to the histogram
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ---------------------------------------------------- # 
# Box plot to detect outliers and spread of values. 

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 7))
sns.boxplot(x='species', y='petal_length', data=iris_df, palette='viridis', hue='species', legend=False)
            # "palette" is used for set of colors used to represent different categories (especially when using hue)
plt.title('Box Plot of Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()