# 1D array slicing
arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[2:5])    # Elements from index 2 to 4
print(arr[::2])    # Every second element
print(arr[::-1])   # Reverse array

# 2D array slicing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[:2])        # First two rows
print(arr_2d[:, 1:])     # All rows, columns from index 1
print(arr_2d[1:, 1:])    # Subarray