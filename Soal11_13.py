# Problem 11.13
# Gauss-Seidel Method
# (a) Without relaxation
# (b) With relaxation λ = 1.2

es = 5.0

print("=== WITHOUT RELAXATION ===")

x1 = x2 = x3 = 0.0
iteration = 0

while True:

    old1, old2, old3 = x1, x2, x3

    x1 = (20 + x2 - 2*x3) / 8
    x2 = (38 + 2*x1 - x3) / 6
    x3 = (-34 + 3*x1 + x2) / 7

    iteration += 1

    if iteration > 1:

        ea1 = abs((x1 - old1) / x1) * 100
        ea2 = abs((x2 - old2) / x2) * 100
        ea3 = abs((x3 - old3) / x3) * 100

        if max(ea1, ea2, ea3) < es:
            break

print(f"Iterations = {iteration}")
print(f"x1 = {x1:.3f}")
print(f"x2 = {x2:.3f}")
print(f"x3 = {x3:.3f}")

print("\n=== WITH RELAXATION (lambda = 1.2) ===")

lam = 1.2

x1 = x2 = x3 = 0.0
iteration = 0

while True:

    old1, old2, old3 = x1, x2, x3

    gs1 = (20 + x2 - 2*x3) / 8
    x1 = lam * gs1 + (1 - lam) * old1

    gs2 = (38 + 2*x1 - x3) / 6
    x2 = lam * gs2 + (1 - lam) * old2

    gs3 = (-34 + 3*x1 + x2) / 7
    x3 = lam * gs3 + (1 - lam) * old3

    iteration += 1

    if iteration > 1:

        ea1 = abs((x1 - old1) / x1) * 100
        ea2 = abs((x2 - old2) / x2) * 100
        ea3 = abs((x3 - old3) / x3) * 100

        if max(ea1, ea2, ea3) < es:
            break

print(f"Iterations = {iteration}")
print(f"x1 = {x1:.3f}")
print(f"x2 = {x2:.3f}")
print(f"x3 = {x3:.3f}")