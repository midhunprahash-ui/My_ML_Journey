# Using integer arrays for indexing
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([1, 3, 4])
print(arr[indices])      # Select elements at these indices

# Multiple arrays for 2D indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = np.array([0, 1])
cols = np.array([1, 2])
print(arr_2d[rows, cols])