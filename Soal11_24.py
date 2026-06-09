import numpy as np

def thomas_algorithm(a, b, c, d):
    """
    Thomas Algorithm

    a = sub-diagonal
    b = main diagonal
    c = super-diagonal
    d = right-hand side
    """

    n = len(d)

    # Forward elimination
    for i in range(1, n):
        factor = a[i-1] / b[i-1]

        b[i] = b[i] - factor * c[i-1]
        d[i] = d[i] - factor * d[i-1]

    # Back substitution
    x = np.zeros(n)

    x[-1] = d[-1] / b[-1]

    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]

    return x


print("=== Problem 11.24 ===\n")

# Example 11.1 test system

a = np.array([-0.4, -0.4], dtype=float)
b = np.array([0.8, 0.8, 0.8], dtype=float)
c = np.array([-0.4, -0.4], dtype=float)

d = np.array([41, 25, 105], dtype=float)

solution = thomas_algorithm(
    a.copy(),
    b.copy(),
    c.copy(),
    d.copy()
)

print("Solution:")
for i in range(len(solution)):
    print(f"x{i+1} = {solution[i]:.6f}")