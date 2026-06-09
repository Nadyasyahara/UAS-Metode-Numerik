es = 5.0

print("=== WITHOUT RELAXATION ===")

x1 = x2 = x3 = 0.0
iteration = 0

while True:

    old1, old2, old3 = x1, x2, x3

    x1 = (3 + x2 + x3) / 6
    x2 = (40 - 6*x1 - x3) / 9
    x3 = (50 + 3*x1 - x2) / 12

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

print("\n=== WITH RELAXATION (lambda = 0.95) ===")

lam = 0.95

x1 = x2 = x3 = 0.0
iteration = 0

while True:

    old1, old2, old3 = x1, x2, x3

    gs1 = (3 + x2 + x3) / 6
    x1 = lam * gs1 + (1 - lam) * old1

    gs2 = (40 - 6*x1 - x3) / 9
    x2 = lam * gs2 + (1 - lam) * old2

    gs3 = (50 + 3*x1 - x2) / 12
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