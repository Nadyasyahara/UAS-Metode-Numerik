import numpy as np

# L and U from Example 11.1

L = np.array([
    [1.0,     0.0,    0.0,   0.0],
    [-0.49,   1.0,    0.0,   0.0],
    [0.0,   -0.645,   1.0,   0.0],
    [0.0,    0.0,   -0.717,  1.0]
])

U = np.array([
    [2.04, -1.0,   0.0,   0.0],
    [0.0,  1.55, -1.0,   0.0],
    [0.0,  0.0,  1.395, -1.0],
    [0.0,  0.0,  0.0,   1.323]
])

n = 4

A_inv = np.zeros((n, n))

for col in range(n):

    # Unit vector e_i
    e = np.zeros(n)
    e[col] = 1.0

    # Forward substitution: L y = e
    y = np.zeros(n)

    for i in range(n):
        y[i] = e[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # Back substitution: U x = y
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i]

        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]

        x[i] /= U[i, i]

    # Store as a column of A^-1
    A_inv[:, col] = x

print("=== Problem 11.2 ===")
print("\nInverse Matrix A^-1:\n")
print(np.round(A_inv, 6))