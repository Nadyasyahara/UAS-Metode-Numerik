def gauss_seidel(es=5.0):

    c1 = 0.0
    c2 = 0.0
    c3 = 0.0

    iteration = 0

    while True:

        old1 = c1
        old2 = c2
        old3 = c3

        # Gauss-Seidel equations
        c1 = (3800 + 3*c2 + c3) / 15

        c2 = (1200 + 3*c1 + 6*c3) / 18

        c3 = (2350 + 4*c1 + c2) / 12

        iteration += 1

        if iteration > 1:

            ea1 = abs((c1 - old1) / c1) * 100
            ea2 = abs((c2 - old2) / c2) * 100
            ea3 = abs((c3 - old3) / c3) * 100

            if max(ea1, ea2, ea3) < es:
                break

    return c1, c2, c3, iteration


print("=== Problem 11.26 ===\n")

c1, c2, c3, iteration = gauss_seidel()

print(f"Iterations = {iteration}")
print(f"c1 = {c1:.3f}")
print(f"c2 = {c2:.3f}")
print(f"c3 = {c3:.3f}")