import numpy as np

# Given values
x_values = np.array([4, 2, 7, 10, 3, 5], dtype=float)

# Vandermonde Matrix
A = np.vander(x_values, increasing=True)

# Right-hand side = row sums
b = np.sum(A, axis=1)

# Solve system
x = np.linalg.solve(A, b)

# Spectral condition number
cond_number = np.linalg.cond(A, 2)

# Expected digits lost
digits_lost = np.log10(cond_number)

print("=== Problem 11.20 ===\n")

print("Vandermonde Matrix:\n")
print(A)

print("\nSpectral Condition Number:")
print(cond_number)

print("\nExpected Digits Lost:")
print(digits_lost)

print("\nSolution:")
print(x)

print("\nError from exact solution:")
print(np.abs(x - np.ones(6)))