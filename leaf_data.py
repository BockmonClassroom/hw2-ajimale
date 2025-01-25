import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
Name: Abdikarim Jimale
Date:01-20-2025
HW-02
"""

# Load the data from CSV to pandas
df = pd.read_csv('data/Jimale-Leaf-size.csv')

# This part for print test.
#print(df)

# Set the plot style
sns.set(style="whitegrid")

# 1. Graph Histograms of the data
plt.figure(figsize=(12, 6))

# Leaf-length histogram
plt.subplot(1, 2, 1)
sns.histplot(data=df, x='Leaf-length (mm)', hue='Plant Name', multiple="stack", kde=True)
plt.title('Leaf-length Distribution')
plt.xlabel('Leaf-length (mm)')
plt.ylabel('Frequency')

# Leaf-Width histogram
plt.subplot(1, 2, 2)
sns.histplot(data=df, x='Leaf-width (mm)', hue='Plant Name', multiple="stack", kde=True)
plt.title('Leaf-width Distribution')
plt.xlabel('Leaf-width (mm)')
plt.ylabel('Frequency')

# Adjust layout to avoid overlapping
plt.tight_layout()
plt.show()

# 2. Graph BoxPlot for Leaf-length
plt.figure(figsize=(12, 6))

# Boxplot for Leaf-length
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Plant Name', y='Leaf-length (mm)')
plt.title('Leaf-length Boxplot')
plt.xlabel('Plant Species')
plt.ylabel('Leaf-length (mm)')

# Boxplot for Leaf-Width
plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='Plant Name', y='Leaf-width (mm)')
plt.title('Leaf-width Boxplot')
plt.xlabel('Plant Species')
plt.ylabel('Leaf-width (mm)')

# Adjust layout to avoid overlapping
plt.tight_layout()
plt.show()

# 3. Scatter plot (leaf length vs. leaf width)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Leaf-length (mm)', y='Leaf-width (mm)', hue='Plant Name', palette='Set2')
plt.title('Scatter Plot of Leaf length vs. Leaf width')
plt.xlabel('leaf Length (mm)')
plt.ylabel('Leaf Width (mm)')
plt.legend(title='Plant Species')
plt.show()

# 4. Statistical Analysis
# Calculate mean, median, standard deviation, and variance for each species
summary_stats = df.groupby('Plant Name').agg(
    Mean_Length=('Leaf-length (mm)','mean'),
    Median_Length=('Leaf-length (mm)', 'median'),
    Sta_Dev_Length=('Leaf-length (mm)', 'std'),
    Var_Length=('Leaf-length (mm)', 'var'),
    Mean_Width=('Leaf-width (mm)','mean'),
    Median_Width=('Leaf-width (mm)', 'median'),
    Sta_Dev_Width=('Leaf-width (mm)', 'std'),
    Var_Width=('Leaf-width (mm)', 'var')
).reset_index()

# Display the summary statistics
print(summary_stats)