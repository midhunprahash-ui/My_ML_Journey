# Operations with Arrays in Python

## 📌 Introduction  
Arrays in Python can be handled using the **NumPy** library, which provides efficient storage and operations for numerical data. NumPy arrays (ndarray) are more powerful and flexible than Python lists, making them essential for scientific computing and data processing.

## 📌 Installation  
```bash
pip install numpy
```

## 📌 Creating Arrays  
### ✅ Creating a NumPy Array  
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

### ✅ Creating Multi-dimensional Arrays  
```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
```

### ✅ Creating Special Arrays  
```python
np.zeros((3, 3))  # 3x3 matrix of zeros
np.ones((2, 4))   # 2x4 matrix of ones
np.eye(3)         # 3x3 identity matrix
np.arange(0, 10, 2)  # Array from 0 to 10 with step 2
np.linspace(0, 1, 5) # 5 values between 0 and 1
```

## 📌 Array Operations  
### 🔹 Basic Arithmetic Operations  
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Element-wise addition
print(arr1 - arr2)  # Element-wise subtraction
print(arr1 * arr2)  # Element-wise multiplication
print(arr1 / arr2)  # Element-wise division
print(arr1 ** 2)    # Element-wise exponentiation
```

### 🔹 Aggregate Functions  
```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())      # Sum of all elements
print(arr.mean())     # Mean of the elements
print(arr.min())      # Minimum value
print(arr.max())      # Maximum value
print(arr.std())      # Standard deviation
```

### 🔹 Indexing and Slicing  
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])   # First element
print(arr[-1])  # Last element
print(arr[1:4]) # Elements from index 1 to 3
```

### 🔹 Reshaping and Transposing  
```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix.reshape(3, 2))  # Reshape into 3 rows and 2 columns
print(matrix.T)               # Transpose the matrix
```

### 🔹 Concatenation and Stacking  
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.concatenate((arr1, arr2)))  # Concatenate arrays
print(np.vstack((arr1, arr2)))       # Stack vertically
print(np.hstack((arr1, arr2)))       # Stack horizontally
```

### 🔹 Filtering and Boolean Masking  
```python
arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 20])  # Filter elements greater than 20
```

## 📌 Conclusion  
NumPy provides powerful array operations that optimize performance for numerical computations
