
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

# Array math
x =np.array([[1, 2], [3, 4],[5, 6]])
y = np.array([[7, 8], [9, 10],[11, 12]])
# sum; both produce teh array
print(x + y)
print(np.add(x, y))
# difference; both produce the array
print(x - y)
print(np.subtract(x, y))
# product; both produce the array
print(x * y)
print(np.multiply(x, y))
# division; both produce the array
print(x / y)
print(np.divide(x, y))
# square root; produces the array
print(np.sqrt(x))
# inner product of vector; both produce 219
a = np.array([9, 10])
b = np.array([11, 12])
print(a.dot(b))
print(np.dot(a, b))
# matrix / vector product; both produce the rank 1 array [29 67 105]
print(x.dot(a))
print(np.dot(x, a))

# sum function
x = np.array([[1, 2], [3, 4]])
# compute sum of all elements
print(np.sum(x))
# compute sum of each column
print(np.sum(x, axis=0))
# compute sum of each row
print(np.sum(x, axis=1))

# transpose function
print(x)
print(x.T)
# note that taking the transpose of a rank 1 array does nothing
v = np.array([1, 2, 3])
print(v)
print(v.T)

# broadcasting
# create a matrix
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# create a vector
v = np.array([1, 0, 1])
# create an empty matrix with the same shape as a
b = np.empty_like(a)
# add the vector v to each row of the matrix x with an explict loop
for i in range(3):
    b[i, : ] = a[i, : ] + v
print(b)
# broadcasting for large matrix
# stack 3 copies of v on top of each other
vv = np.tile(v, (3, 1))
print(vv)
# add a and vv elementwise
b = a + vv
print(b)

# broadcasting using NumPy
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, 1])
# add v to each row of a using broadcasting
b = a + v
print(b)
# applications of broadcasting
# compute outer product of vectors
# v has shape (3, )
v = np.array([1, 2, 3])
# w has shape (2, )
w = np.array([4, 5])
# to compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3,2), which is the outer product of v and w:
print(np.reshape(v, (3, 1)) * w)

# add a vector to each row of a matrix
x = np.array([[1, 2, 3], [4, 5, 6]])
# x has shape (2, 3) and v has shape (3, ), so they broadcast to (2, 3)
print(x + v)

# add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2, ).
# if we transpose x then it has shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column
print((x.T + w).T)
# another solution is to reshape w toe be a row vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same output
print(x + np.reshape(w, (2, 1)))

# multiply a matrix bt a constant:
# has shape (2, 3). Numpy treats scalars as arrays of shape ();
# these can be broadcast together to shape (2, 3)
print(x * 2)




