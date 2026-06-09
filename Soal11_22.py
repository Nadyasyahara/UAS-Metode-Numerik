import numpy as np

A = np.array([
    [0, 7, -5],
    [0, 4, 7],
    [-4, 3, -7]
], dtype=float)

b = np.array([
    -50,
    -30,
    40
], dtype=float)

# Solution
x = np.linalg.solve(A, b)

# Transpose
AT = A.T

# Inverse
A_inv = np.linalg.inv(A)

print("=== Problem 11.22 ===\n")

print("Coefficient Matrix A:")
print(A)

print("\nSolution:")
print(x)

print("\nTranspose A^T:")
print(AT)

print("\nInverse A^-1:")
print(A_inv)