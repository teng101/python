import numpy as np
import pandas as pd

data = np.genfromtxt("data.csv", delimiter=",")

org_matrix = data[1:,1:-1]
column_mean = np.mean(org_matrix, axis=0)
k_matrix = org_matrix-column_mean
cov_matrix = np.cov(org_matrix, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

trace_lambda = np.sum(eigenvalues)
var_vector = eigenvalues/trace_lambda
#print(var_vector)

max_sum = 0.0
max_value = np.max(var_vector)
max_indices = [np.argmax(var_vector)]

while max_sum <= 0.85:
    high_var_vector_indices = max_indices
    max_sum += max_value
    var_vector[max_indices] = -np.inf  # Set max value to -inf to exclude from next iteration
    if max_sum>0.85:
        break
    max_value = np.max(var_vector)
    if max_value > 0:
        max_indices.append(np.argmax(var_vector))

selected_eigenvectors = eigenvectors[high_var_vector_indices]

trans_data = np.dot(k_matrix, np.transpose(selected_eigenvectors))

print(trans_data)

