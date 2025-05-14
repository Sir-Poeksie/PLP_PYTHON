# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean dataset (not needed here, but showing for completeness)
    df = df.dropna()

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

# Grouping by species and calculating mean
grouped = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped)

# Observations
print("\nObservations:")
print("- Setosa has the smallest measurements overall.")
print("- Virginica has the highest petal length and width on average.")

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line chart (simulated time series using index)
plt.figure(figsize=(10, 5))
plt.plot(df.index[:50], df['sepal length (cm)'][:50], label='Sepal Length')
plt.plot(df.index[:50], df['petal length (cm)'][:50], label='Petal Length')
plt.title("Line Chart: Sepal and Petal Length Over First 50 Observations")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
