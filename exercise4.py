import numpy as np

#create matrix
A = np.array([[10, 40, 0, 0],
              [0, 40, -10, 0],
              [0, 0, -10, 50],
              [10, 0, 0, 50]])

B = np.array([50,30,40,60])

augmented_AB = np.column_stack((A,B))

rank_A = np.linalg.matrix_rank(A)
rank_AB = np.linalg.matrix_rank(augmented_AB)
rank_AnB = np.linalg.matrix_rank(A,B)

print(f"Rank(A) = {rank_A}")
print(f"Rank(A/B) = {rank_AB}")
print(f"Rank nullity = {A.shape[1] - rank_A}")
