import numpy as np

# Subdiagonal
a = np.array([0.0,
              -0.020875,
              -0.020875,
              -0.020875])

# Main diagonal
b = np.array([2.01475,
              2.01475,
              2.01475,
              2.01475])

# Superdiagonal
c = np.array([-0.020875,
              -0.020875,
              -0.020875,
              0.0])

# Right-hand side
d = np.array([4.175,
              0.0,
              0.0,
              2.0875])

n = len(d)

# Forward elimination
for i in range(1, n):
    factor = a[i] / b[i - 1]
    b[i] = b[i] - factor * c[i - 1]
    d[i] = d[i] - factor * d[i - 1]

# Back substitution
T = np.zeros(n)

T[n - 1] = d[n - 1] / b[n - 1]

for i in range(n - 2, -1, -1):
    T[i] = (d[i] - c[i] * T[i + 1]) / b[i]

print("=== Problem 11.3 ===")
print(f"T1 = {T[0]:.6f}")
print(f"T2 = {T[1]:.6f}")
print(f"T3 = {T[2]:.6f}")
print(f"T4 = {T[3]:.6f}")