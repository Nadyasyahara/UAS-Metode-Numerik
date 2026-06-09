import numpy as np
from scipy.linalg import hilbert

# Hilbert matrix 10x10
A = hilbert(10)

# Right-hand side = row sums
b = np.sum(A, axis=1)

# Solve system
x = np.linalg.solve(A, b)

# Spectral condition number (2-norm)
cond_number = np.linalg.cond(A, 2)

# Expected digits lost
digits_lost = np.log10(cond_number)

print("=== Problem 11.19 ===\n")

print("Spectral Condition Number:")
print(cond_number)

print("\nExpected Digits Lost:")
print(digits_lost)

print("\nSolution:")
print(x)

print("\nError from exact solution:")
print(np.abs(x - np.ones(10)))