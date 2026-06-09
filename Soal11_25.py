import numpy as np

def cholesky_decomposition(A, b):

    # Cholesky factorization
    L = np.linalg.cholesky(A)

    # Forward substitution
    y = np.linalg.solve(L, b)

    # Back substitution
    x = np.linalg.solve(L.T, y)

    return L, x


print("=== Problem 11.25 ===\n")

# Example 11.2

A = np.array([
    [6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]
], dtype=float)

b = np.array([
    152.6,
    585.6,
    2488.8
], dtype=float)

L, x = cholesky_decomposition(A, b)

print("Matrix L:")
print(L)

print("\nSolution:")

for i in range(len(x)):
    print(f"a{i} = {x[i]:.6f}")