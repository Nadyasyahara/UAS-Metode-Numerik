import numpy as np

# Coefficient matrix
A = np.array([
    [6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]
], dtype=float)

# Right-hand side vector
b = np.array([
    152.6,
    585.6,
    2488.8
], dtype=float)

# Cholesky decomposition
L = np.linalg.cholesky(A)

# Forward substitution: Ly = b
y = np.zeros(3)

for i in range(3):
    y[i] = b[i]
    for j in range(i):
        y[i] -= L[i, j] * y[j]
    y[i] /= L[i, i]

# Back substitution: Lᵀx = y
a = np.zeros(3)

for i in range(2, -1, -1):
    a[i] = y[i]
    for j in range(i + 1, 3):
        a[i] -= L.T[i, j] * a[j]
    a[i] /= L.T[i, i]

print("=== Problem 11.5 ===\n")

print("L =")
print(np.round(L, 4))

print("\nSolution:")
print(f"a0 = {a[0]:.6f}")
print(f"a1 = {a[1]:.6f}")
print(f"a2 = {a[2]:.6f}")