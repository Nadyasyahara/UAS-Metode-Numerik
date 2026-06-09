# Problem 11.17
# Nonlinear Simultaneous Equations

from scipy.optimize import fsolve

def equations(vars):
    x, y = vars

    f = 4 - y - 2*x**2
    g = 8 - y**2 - 4*x

    return [f, g]

print("=== Problem 11.17 ===\n")

# Part (a)
print("PART (a): Finding the two solutions\n")

# First solution
sol1 = fsolve(equations, [-2, -2])

# Second solution
sol2 = fsolve(equations, [1, 3])

print("Solution 1:")
print(f"x = {sol1[0]:.5f}")
print(f"y = {sol1[1]:.5f}")

print("\nSolution 2:")
print(f"x = {sol2[0]:.5f}")
print(f"y = {sol2[1]:.5f}")

# -------------------------------------------------

print("\n\nPART (b): Effect of Initial Guesses\n")

initial_guesses = [
    (-6, -6),
    (-4, -4),
    (-2, -2),
    (-1, -1),
    (0, 0),
    (1, 1),
    (2, 2),
    (4, 4),
    (6, 6)
]

for guess in initial_guesses:

    solution = fsolve(equations, guess)

    print(
        f"Initial Guess {guess} "
        f"-> x = {solution[0]:.5f}, y = {solution[1]:.5f}"
    )