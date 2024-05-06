# TASK 3
import numpy as np

#  matrix A
A = np.array([[40, -20, 0],
              [-20, 40, -20],
              [0, -20, 40]])

# initial guess for the eigenvector
x = np.random.rand(3)

# Power Method to find the largest eigenvalue
def power_method(A, x, iterations=100, tolerance=1e-6):
    prev_lambda = 0
    for _ in range(iterations):
        x = np.dot(A, x)  # Multiply A by x
        x = x / np.linalg.norm(x)  # Normalize x
        curr_lambda = np.dot(x.T, np.dot(A, x)) / np.dot(x.T, x)  # Rayleigh quotient
        if np.abs(curr_lambda - prev_lambda) < tolerance:
            break
        prev_lambda = curr_lambda
    return curr_lambda, x

largest_eigenvalue, eigenvector = power_method(A, x)

print("Largest Eigenvalue:", largest_eigenvalue)
print("Corresponding Eigenvector:", eigenvector)

# Results:
# Largest Eigenvalue: 68.28427095449076
# Corresponding Eigenvector: [-0.49992803  0.70710678 -0.50007196]


# Convergence Check: It stops if the change in eigenvalue estimates is less than the tolerance, indicating that
# convergence has been achieved.

# Convergence of 𝜆:
# λ: The Power Method will converge under most conditions, especially for matrices like this one, where the dominant
# eigenvalue is distinct.

# Significance: Determining the largest eigenvalue has computational and physical implications, such as stability
# analysis in systems engineering, principal component analysis in statistics/CV. Helps understand the system's
# principal modes or stability features.
