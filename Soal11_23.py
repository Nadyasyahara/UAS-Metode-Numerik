import numpy as np
import matplotlib.pyplot as plt

n = np.arange(2, 21)

# Approximate operation counts
gauss = (2/3) * n**3
thomas = 8*n - 7

print("=== Problem 11.23 ===\n")

print(" n    Gaussian      Thomas")
print("----------------------------")

for i in range(len(n)):
    print(f"{n[i]:2d}   {gauss[i]:10.2f}   {thomas[i]:8.2f}")

plt.figure(figsize=(8,5))

plt.plot(n, gauss, marker='o', label='Gaussian Elimination')
plt.plot(n, thomas, marker='s', label='Thomas Algorithm')

plt.xlabel('n')
plt.ylabel('Number of Operations')
plt.title('Operations vs n')
plt.grid(True)
plt.legend()

plt.show()