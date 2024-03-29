__author__ = "Ibrahim Hassan"
__copyright__ = "Copyright (C) 2024 Ibrahim Hassan"
__license__ = "Public Domain"
__version__ = "1.0"
__date__ = "3/26/2024"

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Given load values in N and corresponding strain values in microstrain
load_values = [-18.13, 113, 208.7, 323.8, 429.7, 533]  # Applied Load (P) in N
axial_strain_values = [0, 0.000044, 0.000144, 0.000273, 0.000394, 0.000512]  # Axial Strain in microstrain
lateral_strain_values = [0, 0.000035, 0.000077, 0.000124, 0.000167, 0.000208]  # Lateral Strain in microstrain, enter absolute values

# Initial force (zero-force) error in N
e_IF = 18.13
# Saves a new list of corrected load values (in N)
load_values_corrected = [lv + e_IF for lv in load_values]
# Prints the new list just for verification
print("Zero-error corrected load values (in N):", load_values_corrected)

# Create scatter plot for axial strain
axial_scatter = plt.scatter(load_values_corrected, axial_strain_values, color="b", label="Axial Strain")

# Calculate line of best fit for axial strain
axial_slope, axial_intercept, _, _, _ = linregress(load_values_corrected, axial_strain_values)
axial_fit_line = np.poly1d([axial_slope, axial_intercept])
axial_line, = plt.plot(load_values_corrected, axial_fit_line(load_values_corrected), color="b", linestyle="--")
axial_plot = plt.text(0.6, 0.00044, 'y={:.6e}x+{:.6e}'.format(axial_slope, axial_intercept), color='blue')

# Create scatter plot for lateral strain
lateral_scatter = plt.scatter(load_values_corrected, lateral_strain_values, color="r", label="Lateral Strain")

# Calculate line of best fit for lateral strain
lateral_slope, lateral_intercept, _, _, _ = linregress(load_values_corrected, lateral_strain_values)
lateral_fit_line = np.poly1d([lateral_slope, lateral_intercept])
lateral_line, = plt.plot(load_values_corrected, lateral_fit_line(load_values_corrected), color="r", linestyle="--")
lateral_plot = plt.text(0.6, 0.0004, 'y={:.6e}x+{:.6e}'.format(lateral_slope, lateral_intercept), color='red')

# Set labels and title
plt.xlabel("Applied Load, P (N)")
plt.ylabel("Strain, ε")
plt.title("Axial and Lateral Strain vs. Applied Load")

# Adjust the axis to fit the data
# Note: this may produce errors but won't affect the results or plot
# Adjust this section according to your needs
x_min, x_max = min(load_values_corrected), max(load_values_corrected)
y_min, y_max = min(min(axial_strain_values), min(lateral_strain_values)), max(max(axial_strain_values), max(lateral_strain_values))
x_margin = (x_max - x_min) * 0.1
y_margin = (y_max - y_min) * 0.1
plt.xlim(x_min - x_margin, x_max + x_margin)
plt.ylim(y_min - y_margin, y_max + y_margin)

# Create a legend
plt.legend([(axial_scatter, axial_line), (lateral_scatter, lateral_line)], ['Axial Strain', 'Lateral Strain'])

# Show the plot
plt.grid(True)
plt.savefig('Axial and Lateral Strain vs. Applied Load_(Initial-force-error-corrected).png')

# Calculate Poisson's ratio and print the value
# Note: All our values were entered as absolute above, therefore "-" is not needed before the equation below
poissons_ratio = lateral_slope / axial_slope
print("Poisson's ratio: ", poissons_ratio)
