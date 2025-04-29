# analysis_visualization.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset
df = pd.read_csv("Experiment-01-DataAnalysis/employee_data.csv")

# Display top and bottom records
print("Top 5 records:\n", df.head())
print("Bottom 5 records:\n", df.tail())

# Dataset Info
print("\nDataset Info:")
print(df.info())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check for Duplicates
print("\nDuplicate Values:\n", df.duplicated().sum())

# Check for Null Values
print("\nNull Values:\n", df.isnull().sum())

# Fill missing values with mean (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Central Tendency Measures
print("\nCentral Tendency Measures:")
print("Mean Salary:", df['Salary'].mean())
print("Median Salary:", df['Salary'].median())
print("Mode of Department:", df['Department'].mode()[0])

# Shallow and Deep Copy
shallow_copy = df
deep_copy = df.copy()

# Introduce a null and replace with mean (for demo)
df.loc[0, 'Salary'] = np.nan
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Visualization Section

# Bar Chart
sns.barplot(x=df['Department'].value_counts().index, y=df['Department'].value_counts().values)
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Count Plot
sns.countplot(x=df['Department'])
plt.title("Employee Count per Department")
plt.show()

# Pie Chart
df['Department'].value_counts().plot.pie(autopct="%1.1f%%", figsize=(6,6))
plt.title("Department Share")
plt.ylabel("")
plt.show()

# Histogram
df['Salary'].hist(bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
sns.scatterplot(x=df['Age'], y=df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Box Plot
sns.boxplot(x=df['Salary'])
plt.title("Salary Box Plot")
plt.xlabel("Salary")
plt.show()

# Heatmap
numeric_data = df.select_dtypes(include=['number'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
