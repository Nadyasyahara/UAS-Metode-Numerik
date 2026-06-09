import numpy as np

A = np.array([
    [ 8, -2, -1,  0,  0],
    [-2,  9, -4, -1,  0],
    [-1, -3,  7, -1, -2],
    [ 0, -4, -2, 12, -5],
    [ 0,  0, -7, -3, 15]
], dtype=float)

b = np.array([
    5,
    2,
    0,
    1,
    5
], dtype=float)

# Solve system
x = np.linalg.solve(A, b)

print("=== Problem 11.28 ===\n")

for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.6f}")