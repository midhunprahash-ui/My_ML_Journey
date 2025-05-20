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



```
