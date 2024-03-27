__author__ = "Ibrahim Hassan"
__copyright__ = "Copyright (C) 2024 Ibrahim Hassan"
__license__ = "Public Domain"
__version__ = "1.0"
__date__ = "3/25/2024"

# Generated file will display the data as follows:
# Data Num. | Total Displacement | Load (N) | Strain (after corrections) | Stress (kPa) | Corrected Displacement

import pandas as pd

# Load the data
# Change file name as needed
# Make sure the first line in the .txt file is the first data point (remove all extra info at the start of original file)
data = pd.read_csv('GROUP10.txt', sep="\s+", header=None)

# Acknowledge the 2nd column value in the first row as a zero point
zero_point = data.iloc[0, 1]

# Add the difference of every corresponding row's 2nd column value
data[1] = data[1] - zero_point

# Original length of the material or testing region in mm
L = 64.12

# Calculate strain and add it to a new 4th column
data[3] = data[1] / L

# Cross-sectional area in mm^2
A = 13.284

# Convert kN to N for stress calculations later on
data[2] = data[2] * 1000

# Considering initial force error / zero-force error (N)
# This should reset all generated values in first row to 1 0.0 0.0 0.0 0.0 0.0
e_IF = 18.13
data[2] = data[2] + e_IF

# Calculate stress (load/area) and add it to a new 5th column
# Convert the stress from N/mm^2 (MPa) to kPa by multiplying by 1000
# Stress values already account the e_IF adjustment made above
data[4] = (data[2] / A) * 1000

# Value of K_INSTRON (N/mm), if not considering machine stiffness, enter 1
K_INSTRON = 6300

# Calculate the machine displacement (U) using formula:
# F = K_INSTRON * U
F = data[2]
U = F / K_INSTRON

# Calculate corrected displacement
total_displacement = data[1]
C_disp = total_displacement - U

# Save as 6th column
data[5] = C_disp

# Fix strain value after all corrections made
data[3] = data[5] / L

# Save the data to another file
# Change file name as needed
data.to_csv('GROUP10-mod.txt', sep=" ", header=None, index=False)
