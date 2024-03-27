__author__ = "Ibrahim Hassan"
__copyright__ = "Copyright (C) 2024 Ibrahim Hassan"
__license__ = "Public Domain"
__version__ = "1.0"
__date__ = "3/27/2024"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Several snipets were unnecessary and were commented our for my use,
# but were left in as they may be useful in other cases.

# Read the data from the file
data = pd.read_csv('GROUP10-mod.txt', sep=' ', names=['num', 'extension', 'load', 'strain', 'stress', 'c_disp'])

# Select the initial linear region of the curve
initial_region = data[data['strain'] < 0.05]

# Perform linear regression on the initial region
slope, intercept, r_value, p_value, std_err = linregress(initial_region['strain'], initial_region['stress'])

# The slope of the line is the modulus of elasticity
modulus_of_elasticity = slope

# Calculate the yield point using 0.2% offset method
offset_strain = 0.002
offset_line = initial_region['strain'] * slope + intercept - offset_strain
yield_point_index = np.where(data.loc[initial_region.index, 'stress'] >= offset_line)[0][0]
yield_point = data.loc[initial_region.index[yield_point_index]]

# Calculate the ultimate load point
ultimate_tensile_point = data.loc[data['load'].idxmax()]

# Define the fracture point as given
fracture_point = {'strain': 0.3106405115903711, 'stress': 123982.2342667871}

# Plot the stress-strain diagram
plt.figure(figsize=(10, 6))
plt.plot(data['strain'], data['stress'])
plt.xlabel('Strain, ε')
plt.ylabel('Stress, σ (kPa)')
plt.title('Stress-Strain Diagram (Aluminium 6061)')

# Add indications for yield point, fracture point
# plt.axhline(y=yield_point['stress'], color='r', linestyle='--', label='Yield Point')
# plt.axhline(y=fracture_point['strain'], color='m', linestyle='--', label='Fracture Point')

# Add indications for yield point, fracture point
plt.scatter(yield_point['strain'], yield_point['stress'], color='r', marker='x', s=100, label='Yield Point')
plt.scatter(fracture_point['strain'], fracture_point['stress'], color='m', marker='x', s=100, label='Fracture Point')
plt.scatter(ultimate_tensile_point['strain'], ultimate_tensile_point['stress'], color='orange', marker='x', s=100, label='Ultimate Tensile Strength (point)')

# Dotted line showing Ultimate Tensile Strength
plt.plot([0, ultimate_tensile_point['strain']], [ultimate_tensile_point['stress'], ultimate_tensile_point['stress']], 'g--', label='Ultimate Tensile Strength')

# Set the x and y limits to pan the graph correctly according to data
plt.xlim(0, data['strain'].max() * 1.1)  # 10% padding
plt.ylim(0, data['stress'].max() * 1.1)  # 10% padding

# Add text annotations for yield point, ultimate load point, fracture point
# Note, adjustments were added to avoid value figures from overlapping
plt.text(yield_point['strain'], yield_point['stress'], "σ_y: " f'{yield_point["stress"]} kPa at {yield_point["strain"]} strain', verticalalignment='bottom')
plt.text(ultimate_tensile_point['strain'] - 0.2, ultimate_tensile_point['stress'] + 5000, "σ_UTS: " f' {ultimate_tensile_point["stress"]} kPa at {ultimate_tensile_point["strain"]} strain', verticalalignment='top')
plt.text(fracture_point['strain'] - 0.15, fracture_point['stress'] - 5000, "Fracture point: " f' {fracture_point["stress"]} kPa at {fracture_point["strain"]} strain', verticalalignment='top')

# Manually add a triangle for Modulus of Elasticity (E)
# Define the points for the triangle
point1 = (0.0027, 40185.9380)
point2 = (0.0027, 10000)
point3 = (0.0001, 10000)

# Call the function to draw the triangle
draw_triangle(point1, point2, point3)

# Define the position for the letter 'E'
e_position = (0.004, 24000)  # Adjust these values as needed

# Add the letter 'E' to the plot
plt.text(*e_position, 'E = Modulus of Elasticity', fontsize=12, color='b')
# Adjust fontsize as needed

# Add a red solid line to indicate 0.2% offset
plt.plot([0.002, yield_point['strain']], [0, yield_point['stress']], 'r-', label='0.2% Offset')

plt.legend()
plt.grid(True)
plt.savefig('Stress-Strain Diagram (Aluminium 6061).png')

# Print the values
print(f"Yield Point: {yield_point['stress']} kPa at {yield_point['strain']} strain")
print(f"Ultimate Load Point: {ultimate_tensile_point['stress']} kPa at {ultimate_tensile_point['strain']} strain")
print(f"Fracture Point: {fracture_point['stress']} kPa at {fracture_point['strain']} strain")
