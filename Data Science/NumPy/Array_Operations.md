# Array Operations in NumPy

## 📌 Introduction
NumPy (Numerical Python) is the fundamental package for numerical computing in Python. It provides powerful tools for working with multi-dimensional arrays and matrices.

## 📌 Creating Arrays
### ✅ Basic Array Creation
```python
import numpy as np

# From Python lists
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Special arrays
zeros = np.zeros((3, 3))       # Array of zeros
ones = np.ones((2, 4))         # Array of ones
empty = np.empty((2, 3))       # Uninitialized array
identity = np.eye(3)           # Identity matrix
range_arr = np.arange(0, 10, 2) # Array with range