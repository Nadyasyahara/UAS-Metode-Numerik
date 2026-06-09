import numpy as np

lam = 1.2
es = 5.0

x1 = 0.0
x2 = 0.0
x3 = 0.0

iteration = 0

while True:

    old1 = x1
    old2 = x2
    old3 = x3

    # Gauss-Seidel updates
    x1_gs = (41 + 0.4 * x2) / 0.8

    x1 = lam * x1_gs + (1 - lam) * old1

    x2_gs = (25 + 0.4 * x1 + 0.4 * x3) / 0.8

    x2 = lam * x2_gs + (1 - lam) * old2

    x3_gs = (105 + 0.4 * x2) / 0.8

    x3 = lam * x3_gs + (1 - lam) * old3

    iteration += 1

    if iteration > 1:

        ea1 = abs((x1 - old1) / x1) * 100
        ea2 = abs((x2 - old2) / x2) * 100
        ea3 = abs((x3 - old3) / x3) * 100

        if max(ea1, ea2, ea3) < es:
            break

print("=== Problem 11.8 ===")
print(f"Iterations = {iteration}")
print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")
print(f"x3 = {x3:.6f}")