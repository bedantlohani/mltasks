# TASK 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system of equations as residuals
def residuals(x):
    x1, x2 = x
    r1 = x1 + 3*x2 + 2  # Corresponds to x1 + 3x2 = -2
    r2 = 3*x1 - x2 - 4  # Corresponds to 3x1 - x2 = 4
    r3 = 2*x1 + 2*x2 - 1 # Corresponds to 2x1 + 2x2 = 1
    return [r1, r2, r3]

# Function to compute the sum of squared residuals
def sum_of_squares(x):
    r = residuals(x)
    return np.sum(np.square(r))

# Using minimize from scipy.optimize to find the minimum SSE
result_sse = minimize(sum_of_squares, [0, 0]) # Initial guess [0, 0]

# Method 2: Solve using pseudo-inverse
A = np.array([[1, 3], [3, -1], [2, 2]])
b = np.array([-2, 4, 1])
pseudo_inverse = np.linalg.pinv(A) # Compute the pseudo-inverse of A
x_pseudo = np.dot(pseudo_inverse, b)

# Display results
print("Method 1 - SSE Optimization:")
print("x1, x2 =", result_sse.x)
print("Sum of squared residuals:", result_sse.fun)

print("\nMethod 2 - Pseudo-inverse:")
print("x1, x2 =", x_pseudo)

# Visualization
x_vals = np.linspace(-10, 10, 400)
y_vals1 = (-x_vals - 2) / 3
y_vals2 = (3*x_vals - 4)
y_vals3 = (1 - 2*x_vals) / 2

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals1, label='x1 + 3x2 = -2')
plt.plot(x_vals, y_vals2, label='3x1 - x2 = 4')
plt.plot(x_vals, y_vals3, label='2x1 + 2x2 = 1')
plt.scatter([result_sse.x[0]], [result_sse.x[1]], color='red', label='SSE Minimization')
plt.scatter([x_pseudo[0]], [x_pseudo[1]], color='blue', label='Pseudo-inverse Solution')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Solution to the Over-determined System')
plt.grid(True)
plt.show()

# Results:
# Method 1 - SSE Optimization:
# x1, x2 = [ 1.11111111 -0.88888889]
# Sum of squared residuals: 0.5555555555555565
#
# Method 2 - Pseudo-inverse:
# x1, x2 = [ 1.11111111 -0.88888889]


# Uniqueness of Solution:
# The visualization shows that both solutions align at the same point where the lines representing the equations are
# closest to each other.
# The graph suggests that the three lines do not intersect at a single point, which implies that there is no unique
# solution that simultaneously satisfies all three equations exactly. This is typical in over-determined systems
# (more equations than variables), where an exact solution might not exist

# Sum of Squared Residual Errors: The SSE method specifically searches for a point  (𝑥1,𝑥2)  that minimizes the sum of
# squared differences between the left and right sides of each equation. This is why the sum of squared residuals was
# significant but not zero. it's a measure of how close the solution is to an exact fit.
#
# Pseudo-inverse Solution: This method computes the solution that minimally projects the error onto the subspace defined
# by the matrix of coefficients. It essentially finds a projection of the b vector onto the column space of the matrix A,
# which is the best approximation given the over-determined nature of the system.
