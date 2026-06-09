import numpy as np

A = np.array([
    [8, 20, 15],
    [20, 80, 50],
    [15, 50, 60]
], dtype=float)

b = np.array([50, 250, 100], dtype=float)

# Cholesky decomposition
L = np.linalg.cholesky(A)

# Solve Ly = b
y = np.linalg.solve(L, b)

# Solve Lᵀx = y
x = np.linalg.solve(L.T, y)

print("=== Problem 11.6 ===\n")

print("L =")
print(np.round(L, 6))

print("\nSolution:")
print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")