# Operations with Arrays in pandas

## 📌 Introduction  
pandas provides powerful tools to work with arrays (Series and DataFrame structures) efficiently. It enables vectorized operations, data transformations, and aggregations with ease.

## 📌 Creating Arrays in pandas  
### ✅ Creating a Series (1D Array)  
```python
import pandas as pd
import numpy as np

series = pd.Series([10, 20, 30, 40, 50])
print(series)
```

### ✅ Creating a DataFrame (2D Array)  
```python
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)
```

## 📌 Array Operations in pandas  
### 🔹 Arithmetic Operations  
```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

print(s1 + s2)  # Element-wise addition
print(s1 - s2)  # Element-wise subtraction
print(s1 * s2)  # Element-wise multiplication
print(s1 / s2)  # Element-wise division
```

### 🔹 Applying Functions  
```python
def square(x):
    return x ** 2

series.apply(square)  # Apply function to each element
```

### 🔹 Aggregate Functions  
```python
print(series.sum())    # Sum of elements
print(series.mean())   # Mean value
print(series.min())    # Minimum value
print(series.max())    # Maximum value
print(series.std())    # Standard deviation
```

### 🔹 Indexing and Slicing  
```python
print(series[0])    # First element
print(series[-1])   # Last element
print(series[1:4])  # Elements from index 1 to 3
```

### Filtering with Conditions  
```python
print(series[series > 20])  # Elements greater than 20
```

### Handling Missing Values  
```python
series_with_nan = pd.Series([1, np.nan, 3, np.nan, 5])
print(series_with_nan.dropna())  # Remove NaN values
print(series_with_nan.fillna(0)) # Replace NaN with 0
```

### DataFrame Operations  
```python
df['D'] = df['A'] + df['B']  # Create new column with sum
print(df)

df.drop(columns=['C'], inplace=True)  # Remove column
print(df)
```

## 📌 Conclusion  
pandas provides intuitive and efficient operations for working with arrays in Series and DataFrame formats. These operations make it a fundamental tool for data manipulation and analysis.

