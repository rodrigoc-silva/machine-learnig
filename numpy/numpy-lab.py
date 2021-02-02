
#numpy lab

import numpy as np

# Initializing NumPy array

# Create a rank 1 array
a = np.array([0, 1, 2])
print(a)
# Create a rank 2 array
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.shape)
print(b)

# Creating NumPy array

# Create a 3x3 array of all zeros
a = np.zeros(((3, 3)))
print(a)
# Create a 2x2 array of all ones
b = np.ones((2, 2))
print(b)
# Create a 3x3 constant array
c = np.full((3, 3), 7)
print(c)
# Create a 3x3 array filled with random values
d = np.random.random((3, 3))
print(d)
# Create a 3x3 identity matrix
e = np.eye(3)
print(e)
# convert list to array
f = np.array([2, 3, 1, 0])
print(f)
# arange() will create arrays with regularly incrementing values
g = np.arange(20)
print(g)
# note mix of tuple and lists
h = np.array([[0, 1, 2.0], [0, 0, 0], (1+1j, 3.0, 2.0)])
print(h)
# create an array of range with float data type
i = np.arange(1, 8, dtype=np.float)
print(i)
# linspace() will create arrays with a specified number of items which are
# spaced equally between the specified beginning and end values
j = np.linspace(2., 4., 5)
print(j)
# indices() will create a set of arrays stacked as a one-higher
# dimensioned array, one per dimension with each representing variation in that dimension
k = np.indices((2, 2))
print(k)

# NumPy datatype
# let numpy choose the datatype
x = np.array([0, 1])
y = np.array([2.0, 3.0])
# force a particular datatype
z = np.array([5, 6], dtype=np.int64)
print(x.dtype, y.dtype, z.dtype)
# field access
x = np.zeros((3, 3), dtype=[('a', np.int32), ('b', np.float64, (3, 3))])
print("x['a'].shape:", x['a'].shape)
print("x['a'].dtype:", x['a'].dtype)
print("x['b'].shape:", x['b'].shape)
print("x['b'].dtype:", x['b'].dtype)

# basic slicing
x = np.array([5, 6, 7, 8, 9])
print(x[0:5:2])
print(x[-2:5])
print(x[-1:1:-1])
print(x[4:])
# basic slicing
y = np.array([[[1], [2], [3]], [[4], [5], [6]]])
print("shape of y:", y.shape)
print(y[1:3])
# create a rank 2 array with shape (3, 4)
a = np.array([[5, 6, 7, 8], [1, 2, 3, 4], [9, 10, 11, 12]])
print("Array 'a':", a)
# use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2)
# [[2 3]
#   [6 7]]
b = a[:2, 1:3]
print("array 'b':", b)
print(a[0, 1])
b[0, 0] = 77
print(a[0, 1])
# accessing middle row array in two ways
row_r1 = a[1, :] # Rank 1 view of the second row of a
row_r2 = a[1:2, :] # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
# accessing columns
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

# advanced indexing
# an example of integer array indexing.
# the returned array will have shape (2, ) and
print(a[[0, 1], [0, 1]])
# the above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1]]))
# when you use integer array indexing, you can reuse the same element from the source array:
print(a[[0, 0], a[1, 1]])
# equivalent to the previous integer array indexing example:
print(np.array([a[1, 1], a[1, 1]]))
# boolean array indexing:
a = np.array([[1, 2], [3, 4], [5, 6]])
# find the elements of a that are bigger than 2
print(a > 2)
# to get the actual value
print(a[a > 2])



# pg 84 array math



