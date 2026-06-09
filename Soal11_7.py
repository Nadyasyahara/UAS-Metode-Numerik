import numpy as np

A = np.array([
    [9, 0, 0],
    [0, 25, 0],
    [0, 0, 4]
], dtype=float)

L = np.linalg.cholesky(A)

print("=== Problem 11.7 ===\n")

print("L =")
print(L)

print("\nVerification (L @ L.T):")
print(L @ L.T)