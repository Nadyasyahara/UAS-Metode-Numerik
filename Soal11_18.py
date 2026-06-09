# Problem 11.18

import numpy as np

A = np.array([
    [4, 3, 2],
    [1, 3, 1],
    [2, 1, 3]
], dtype=float)

b = np.array([
    960,
    510,
    610
], dtype=float)

x = np.linalg.solve(A, b)

print("=== Problem 11.18 ===\n")

print(f"Transistors    = {x[0]:.0f}")
print(f"Resistors      = {x[1]:.0f}")
print(f"Computer Chips = {x[2]:.0f}")