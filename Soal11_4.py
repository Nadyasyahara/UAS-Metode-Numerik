import numpy as np

# Matrix L from Example 11.2

L = np.array([
    [2.4495, 0.0, 0.0],
    [6.1237, 4.1833, 0.0],
    [22.4540, 20.9170, 6.1101]
])

# Compute A = L * L^T

A = L @ L.T

print("=== Problem 11.4 ===\n")

print("L =")
print(L)

print("\nL^T =")
print(L.T)

print("\nL * L^T =")
print(np.round(A, 4))