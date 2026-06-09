import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix
A = np.array([
    [-1.2, 0.25, 0.0, 0.0],
    [0.75, -1.2, 0.25, 0.0],
    [0.0, 0.75, -1.2, 0.25],
    [0.0, 0.0, 0.75, -1.2]
])

# Boundary conditions
c0 = 80
c5 = 20

b = np.array([
    -0.75 * c0,
    0,
    0,
    -0.25 * c5
])

# Solve system
c_internal = np.linalg.solve(A, b)

# Complete concentration vector
c = np.concatenate(([c0], c_internal, [c5]))

x = np.array([0, 2, 4, 6, 8, 10])

print("=== Problem 11.27 ===\n")

for i in range(len(x)):
    print(f"x = {x[i]:2d}, c = {c[i]:.4f}")

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, c, marker='o')
plt.xlabel("Distance x")
plt.ylabel("Concentration c")
plt.title("Concentration vs Distance")
plt.grid(True)
plt.show()