import numpy as np

# Example matrix
A = np.array([
    [1, 2],
    [3, 4]
])

# Identity matrix
I = np.eye(len(A))

# Augmented matrix [A|I]
Aug = np.hstack((A, I))

print("=== Problem 11.21 ===\n")

print("Matrix A:")
print(A)

print("\nIdentity Matrix I:")
print(I)

print("\nAugmented Matrix [A|I]:")
print(Aug)

print("\nEquivalent MATLAB Command:")
print("Aug = [A eye(size(A))]")