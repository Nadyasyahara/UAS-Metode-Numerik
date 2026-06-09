"""
Problem 11.1
Chapter 11 - Special Matrices and Gauss-Seidel

Solve the tridiagonal system using the Thomas Algorithm.
"""

import numpy as np

# Coefficients of the tridiagonal matrix
a = np.array([0.0, -0.4, -0.4])   # subdiagonal
b = np.array([0.8, 0.8, 0.8])     # main diagonal
c = np.array([-0.4, -0.4, 0.0])   # superdiagonal

# Right-hand side vector
d = np.array([41.0, 25.0, 105.0])

n = len(d)

# Forward elimination
for i in range(1, n):
    factor = a[i] / b[i - 1]
    b[i] = b[i] - factor * c[i - 1]
    d[i] = d[i] - factor * d[i - 1]

# Back substitution
x = np.zeros(n)

x[n - 1] = d[n - 1] / b[n - 1]

for i in range(n - 2, -1, -1):
    x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

# Output
print("=== Problem 11.1 ===")
print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")