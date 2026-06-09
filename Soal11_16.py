import numpy as np

print("=== PART (a) ===")

A1 = np.array([
    [1, 4, 9],
    [4, 9, 16],
    [9, 16, 25]
], dtype=float)

b1 = np.array([14, 29, 50], dtype=float)

# Solution
x1 = np.linalg.solve(A1, b1)

# Inverse
A1_inv = np.linalg.inv(A1)

# Row-sum norm (infinity norm)
normA1 = np.linalg.norm(A1, ord=np.inf)
normInv1 = np.linalg.norm(A1_inv, ord=np.inf)

# Condition number
cond1 = normA1 * normInv1

print("Solution:")
print(x1)

print("\nInverse:")
print(A1_inv)

print("\nCondition Number:")
print(cond1)

print("\nResidual:")
print(A1 @ x1 - b1)

print("\n====================\n")

print("=== PART (b) ===")

A2 = np.array([
    [1, 4, 9, 16],
    [4, 9, 16, 25],
    [9, 16, 25, 36],
    [16, 25, 36, 49]
], dtype=float)

b2 = np.array([30, 54, 86, 126], dtype=float)

# Solution
x2 = np.linalg.solve(A2, b2)

# Inverse
A2_inv = np.linalg.inv(A2)

# Row-sum norm (infinity norm)
normA2 = np.linalg.norm(A2, ord=np.inf)
normInv2 = np.linalg.norm(A2_inv, ord=np.inf)

# Condition number
cond2 = normA2 * normInv2

print("Solution:")
print(x2)

print("\nInverse:")
print(A2_inv)

print("\nCondition Number:")
print(cond2)

print("\nResidual:")
print(A2 @ x2 - b2)