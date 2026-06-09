es = 5.0

x1 = 0.0
x2 = 0.0
x3 = 0.0

iteration = 0

while True:

    old1 = x1
    old2 = x2
    old3 = x3

    # Gauss-Seidel equations

    x1 = (27 - 2 * x2 + x3) / 10

    x2 = (61.5 - 3 * x1 + 2 * x3) / 6

    x3 = (-21.5 - x1 - x2) / 5

    iteration += 1

    if iteration > 1:

        ea1 = abs((x1 - old1) / x1) * 100
        ea2 = abs((x2 - old2) / x2) * 100
        ea3 = abs((x3 - old3) / x3) * 100

        if max(ea1, ea2, ea3) < es:
            break

print("=== Problem 11.11 ===")
print(f"Iterations = {iteration}")
print(f"x1 = {x1:.3f}")
print(f"x2 = {x2:.3f}")
print(f"x3 = {x3:.3f}")