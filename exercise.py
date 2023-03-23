import pandas as pd
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,6,7,8,9])

print(x*y) # element-wise multiplication

x1 = np.array([[1, 2], [3, 4]])
y1 = np.array([[5, 6], [7, 8]])

z = x1@y1 #/z = np.dot(x1, y1) matrix multiplication
print(z)

a = 2 # scalar
z1 = a * x1 # broadcasting
print(z1)

#Identity matrix
identity_mat = np.eye(3) #3*3 identity matrix
print(identity_mat)


#zero matrix
zero_mat = np.zeros((2,3))
print(zero_mat)


#ones matrix
ones_mat = np.ones((2,3))
print(ones_mat)


#diagonal matrix with diagonal elements [1,2,3]
diagonal_mat = np.diag([1,2,3])
print(diagonal_mat)

#upper triangular matrix
up_tri_mat = np.triu(np.ones((3,3)), k=0)
print(up_tri_mat)

# create a 3x3 lower triangular matrix with 2s on the diagonal
arr = np.tril(np.full((3, 3), 2), k=0)
print(arr)


