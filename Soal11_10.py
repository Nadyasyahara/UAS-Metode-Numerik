es = 5.0

# Initial guesses
c1 = 0.0
c2 = 0.0
c3 = 0.0

iteration = 0

while True:

    # Simpan nilai iterasi sebelumnya
    old1 = c1
    old2 = c2
    old3 = c3

    # Jacobi update
    new1 = (3800 + 3 * old2 + old3) / 15
    new2 = (1200 + 3 * old1 + 6 * old3) / 18
    new3 = (2350 + 4 * old1 + old2) / 12

    # Update semua sekaligus
    c1 = new1
    c2 = new2
    c3 = new3

    iteration += 1

    if iteration > 1:

        ea1 = abs((c1 - old1) / c1) * 100
        ea2 = abs((c2 - old2) / c2) * 100
        ea3 = abs((c3 - old3) / c3) * 100

        if max(ea1, ea2, ea3) < es:
            break

print("=== Problem 11.10 ===")
print(f"Iterations = {iteration}")
print(f"c1 = {c1:.3f}")
print(f"c2 = {c2:.3f}")
print(f"c3 = {c3:.3f}")