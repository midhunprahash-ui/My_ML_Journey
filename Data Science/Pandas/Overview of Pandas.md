# Overview of Pandas Library

## 📌 Introduction  
**pandas** is a fast, powerful, and flexible open-source Python library used for data manipulation and analysis. It provides data structures like **Series** and **DataFrame** that make it easy to handle structured data efficiently.  

## 📌 Installation  
```bash
pip install pandas
```

## 📌 Core Data Structures  
1. **Series** – A one-dimensional labeled array.  
2. **DataFrame** – A two-dimensional labeled data structure (like a table).  

## 📌 Creating Data Structures  
### ✅ Creating a Series  
```python
import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(series)
```

### ✅ Creating a DataFrame  
```python
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)
```

## 📌 Essential Operations  
### Reading Data  
```python
df = pd.read_csv('data.csv')   # Read CSV file
df = pd.read_excel('data.xlsx') # Read Excel file
```

### Writing Data  
```python
df.to_csv('output.csv', index=False)  # Save DataFrame to CSV
df.to_excel('output.xlsx', index=False) # Save to Excel
```

### Data Exploration  
```python
df.head()  # First 5 rows
df.tail()  # Last 5 rows
df.info()  # Summary of DataFrame
df.describe()  # Statistical summary
df.shape  # Get number of rows and columns
```

### Data Selection  
```python
df['Name']  # Select a single column
df[['Name', 'Age']]  # Select multiple columns
df.loc[0]  # Select a row by index
df.iloc[0]  # Select a row by position
df[df['Age'] > 30]  # Filter rows based on condition
```

### 🔹 Data Cleaning  
```python
df.dropna()  # Remove missing values
df.fillna(0)  # Fill missing values with 0
df.drop_duplicates()  # Remove duplicate rows
df.rename(columns={'Name': 'Full_Name'})  # Rename column
```

### 🔹 Data Transformation  
```python
df['Age'] = df['Age'] + 1  # Modify column values
df['Age_Group'] = df['Age'].apply(lambda x: 'Senior' if x > 30 else 'Young')
```

### 🔹 Merging and Joining  
```python
df1.merge(df2, on='ID', how='inner')  # Merge two DataFrames
df1.append(df2, ignore_index=True)  # Append DataFrame
```

### 🔹 Grouping and Aggregation  
```python
df.groupby('City')['Age'].mean()  # Group by City and get average Age
df.pivot_table(values='Age', index='City', aggfunc='sum')  # Pivot Table
```

## 📌 Visualization with pandas  
```python
import matplotlib.pyplot as plt

df['Age'].plot(kind='bar')
plt.show()
```

## 📌 Dataframes in Pandas  
```python
import pandas as pd
df=pd.read_csv("File Name")
df.info()
```

## 📌 Conclusion  
pandas is an essential tool for data scientists and analysts, providing powerful capabilities for data manipulation, analysis, and visualization. It integrates well with other libraries like NumPy, Matplotlib, and scikit-learn, making it a must-learn library for anyone working with data in Python.


