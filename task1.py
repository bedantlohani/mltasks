# TASK 1
import time

def f(x, y, z):
    # Function to integrate: f(x, y, z) = z^2 * (x^2 + y^2)
    return z**2 * (x**2 + y**2)

def triple_integral(nx, ny, nz):
    # Integral limits for x, y, and z
    x0, x1 = 0, 2
    y0, y1 = lambda x: 0, lambda x: 2**0.5
    z0, z1 = lambda x, y: 0, lambda x, y: (2 - x**2)**0.5

    # Calculate the size of each division for x, y, z
    dx = (x1 - x0) / nx
    dy = (y1(x0) - y0(x0)) / ny
    dz = (z1(x0, y0(x0)) - z0(x0, y0(x0))) / nz

    integral = 0
    for i in range(nx):
        # Calculate the midpoint for x in the i-th interval
        x = x0 + i * dx + dx / 2
        for j in range(ny):
            # Calculate the midpoint for y in the j-th interval
            y = y0(x) + j * dy + dy / 2
            for k in range(nz):
                # Calculate the midpoint for x in the k-th interval
                z = z0(x, y) + k * dz + dz / 2
                # volume of the small cuboid times the function value at the midpoint added cumulatively
                integral += f(x, y, z) * dx * dy * dz

    return integral

# Parameters: number of divisions in each dimension
divisions = [10, 50, 100, 200]

for n in divisions:
    start_time = time.time()
    result = triple_integral(n, n, n)
    end_time = time.time()
    print(f"Divisions: {n}, Integral: {result:.6f}, Time taken: {end_time - start_time:.2f} seconds")

# increasing the number of divisions increases precision but also increases runtime until the precison starts to
# saturate (run time keeps increasing).

# Divisions: 10, Integral: 5.306700, Time taken: 0.00 seconds
# Divisions: 50, Integral: 5.332267, Time taken: 0.07 seconds
# Divisions: 100, Integral: 5.333067, Time taken: 0.57 seconds
# Divisions: 200, Integral: 5.333267, Time taken: 4.56 seconds (same as 50 divs)

