# 🔍 Data Inspection with Pandas

Data inspection is one of the first and most critical steps in the data analysis or machine learning workflow. It helps you understand the structure, contents, and potential issues in your dataset.

---

## 📦 1. Load Data


```python
import pandas as pd
# Display basic information about the dataset
print(df.info())

# Get dataset dimensions (rows, columns)
print(df.shape)

# Display column names
print(df.columns)

# Get data types of columns
print(df.dtypes)# Display first few rows
print(df.head())

# Display last few rows
print(df.tail())

# Display random sample of rows
print(df.sample(5))# Basic statistical summary
print(df.describe())

# Include object columns in summary
print(df.describe(include='all'))

# Count unique values in each column
print(df.nunique())# Check for missing values
print(df.isnull().sum())

# Get percentage of missing values
print((df.isnull().sum() / len(df)) * 100)

# Display rows with missing values
print(df[df.isnull().any(axis=1)])
df = pd.read_csv('your_file.csv')

# Calculate correlation matrix
correlation_matrix = df.corr()

# Display correlation matrix
print(correlation_matrix)

# Visualize correlation matrix using seaborn
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Display memory usage of DataFrame
print(df.info(memory_usage='deep'))

# Memory usage by column
print(df.memory_usage(deep=True))

# Check for duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Display duplicate rows
print(df[df.duplicated()])

# Check for infinite values
print("Columns with infinite values:", df.columns[np.isinf(df).any()].tolist())

```
