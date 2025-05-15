# Mixing different indexing methods
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Boolean mask with slicing
mask = arr_2d > 4
print(arr_2d[mask])

# Fancy indexing with slicing
rows = np.array([0, 2])
print(arr_2d[rows, :2])