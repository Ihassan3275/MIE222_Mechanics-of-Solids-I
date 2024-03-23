import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Given load values in N and corresponding strain values in microstrain
load_values = [0, 113, 208.7, 323.8, 429.7, 533]  # Applied Load (P) in N
axial_strain_values = [0, 0.000044, 0.000144, 0.000273, 0.000394, 0.000512]  # Axial Strain in microstrain
lateral_strain_values = [0, 0.000035, 0.000077, 0.000124, 0.000167, 0.000208]  # Lateral Strain in microstrain

# Create scatter plot for axial strain
axial_scatter = plt.scatter(load_values, axial_strain_values, color="b", label="Axial Strain")

# Calculate line of best fit for axial strain
axial_slope, axial_intercept, _, _, _ = linregress(load_values, axial_strain_values)
axial_fit_line = np.poly1d([axial_slope, axial_intercept])
axial_line, = plt.plot(load_values, axial_fit_line(load_values), color="b", linestyle="--")
plt.text(0.6, 0.00044, 'y={:.6e}x+{:.6e}'.format(axial_slope, axial_intercept), color='blue')

# Create scatter plot for lateral strain
lateral_scatter = plt.scatter(load_values, lateral_strain_values, color="r", label="Lateral Strain")

# Calculate line of best fit for lateral strain
lateral_slope, lateral_intercept, _, _, _ = linregress(load_values, lateral_strain_values)
lateral_fit_line = np.poly1d([lateral_slope, lateral_intercept])
lateral_line, = plt.plot(load_values, lateral_fit_line(load_values), color="r", linestyle="--")
plt.text(0.6, 0.0004, 'y={:.6e}x+{:.6e}'.format(lateral_slope, lateral_intercept), color='red')

# Set labels and title
plt.xlabel("Applied Load (N)")
plt.ylabel("Strain")
plt.title("Axial and Lateral Strain vs. Applied Load")

# Adjust the axis to fit the data
x_min, x_max = min(load_values), max(load_values)
y_min, y_max = min(min(axial_strain_values), min(lateral_strain_values)), max(max(axial_strain_values), max(lateral_strain_values))
x_margin = (x_max - x_min) * 0.1
y_margin = (y_max - y_min) * 0.1
plt.xlim(x_min - x_margin, x_max + x_margin)
plt.ylim(y_min - y_margin, y_max + y_margin)

# Create a legend
plt.legend([(axial_scatter, axial_line), (lateral_scatter, lateral_line)], ['Axial Strain', 'Lateral Strain'])

# Show the plot
plt.grid(True)
plt.savefig('Axial and Lateral Strain vs. Applied Load.png')
