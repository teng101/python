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
