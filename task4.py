# TASK 4
import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega_n_values = [0.5, 1.0, 1.5]  # Different natural frequencies
zeta_values = [0.1, 0.3, 0.5]     # Different damping constants
dt = 0.05      # Time step
T = 20         # Total time
n_steps = int(T / dt)

# Simulation function using Euler's method
def simulate_damped_oscillator(omega_n, zeta):
    # Initial conditions
    u = np.zeros((2, n_steps))
    u[0, 0] = 1  # Initial displacement
    u[1, 0] = 0  # Initial velocity

    # Euler's method to solve the ODE
    for i in range(1, n_steps):
        u[0, i] = u[0, i-1] + dt * u[1, i-1]
        u[1, i] = u[1, i-1] + dt * (-2 * zeta * omega_n * u[1, i-1] - omega_n**2 * u[0, i-1])

    return u

# Plotting the results
fig, axes = plt.subplots(len(zeta_values), len(omega_n_values), figsize=(15, 10), sharex=True, sharey=True)
for i, zeta in enumerate(zeta_values):
    for j, omega_n in enumerate(omega_n_values):
        u = simulate_damped_oscillator(omega_n, zeta)
        ax = axes[i, j]
        t = np.linspace(0, T, n_steps)
        ax.plot(t, u[0, :], label=f'Displacement ($\omega_n$={omega_n}, $\zeta$={zeta})')
        ax.set_title(f'$\omega_n$={omega_n}, $\zeta$={zeta}')
        ax.grid(True)
        ax.set_xlabel('Time (s)')
        if j == 0:
            ax.set_ylabel('Amplitude')

fig.tight_layout()
plt.legend()
plt.show()

# Underdamped: Lower ζ values (e.g., 0.1) lead to oscillatory behavior that slowly decays.
# Critically Damped and Overdamped: Higher ζ values (e.g., 0.5 and above) lead to faster decay without oscillation or very
# subdued oscillation.
# Natural Frequency Impact: Higher ω_n leads to faster oscillations within the same time frame.

# Computational Significance:
# Modeling Physical Systems (dynamic systems mainly)
# Time Series Prediction: understanding the dynamics of such systems helps in predicting future states in time series data

