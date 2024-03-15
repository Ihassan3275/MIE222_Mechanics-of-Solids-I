import matplotlib.pyplot as plt
import numpy as np

# Basquin's equation parameters
a = 1190  # fatigue strength coefficient
b = -0.030  # fatigue strength exponent

N = np.logspace(0, 10, num=5000)
S = a * (2*N)**b  # stress amplitude

# Define the ultimate strength
ultimate_strength = 7957 # to align with Nf=7957

# Define the failure points for the notched and dogbone samples
N_notched = 7957 # lab calculated value
S_notched = a * (2*N_notched)**b
N_dogbone = 29866 # lab calculated value
S_dogbone = a * (2*N_dogbone)**b

# Find the intersection point (approximately)
intersection_indices = np.where(S < fatigue_limit)[0]
if intersection_indices.size > 0:
    N_intersection = N[intersection_indices[0]]
else:
    N_intersection = N[-1]

plt.figure(figsize=(10, 6))
plt.loglog(N, S, label='S-N Curve')

# Add a vertical line indicating the ultimate strength
plt.vlines(ultimate_strength, plt.ylim()[0], plt.ylim()[1], colors='r', linestyles='dotted', label='Ultimate Strength')

# Add the failure points for the notched and dogbone samples
plt.plot(N_notched, S_notched, 'go', label='Notched Sample Failure Point')
plt.plot(N_dogbone, S_dogbone, 'bo', label='Dogbone Sample Failure Point')

# Add dotted lines from the failure points to the axes
plt.loglog([N_notched, N_notched], [plt.ylim()[0], S_notched], 'g--')  # notched sample
plt.loglog([N_dogbone, N_dogbone], [plt.ylim()[0], S_dogbone], 'b--')  # dogbone sample
plt.loglog([plt.xlim()[0], N_notched], [S_notched, S_notched], 'g--')
plt.loglog([plt.xlim()[0], N_dogbone], [S_dogbone, S_dogbone], 'b--')

# Add the failure point line
plt.hlines(fatigue_limit, N_intersection, plt.xlim()[1], colors='b', linestyles='solid')

# Extend a horizontal line from the failure points
plt.hlines(S_notched, N_notched, plt.xlim()[1], colors='g', linestyles='solid')
plt.hlines(S_dogbone, N_dogbone, plt.xlim()[1], colors='b', linestyles='solid')

# Add labels for the fatigue limits
plt.text(10**7, S_notched, 'Notched Sample Fatigue Limit', fontsize=10, va='bottom')
plt.text(10**7, S_dogbone, 'Dogbone Sample Fatigue Limit', fontsize=10, va='bottom')

# Display the coordinates of the failure points
plt.text(N_notched, S_notched, f'({N_notched:.0f}, {S_notched:.2f})', fontsize=10, va='bottom')
plt.text(N_dogbone, S_dogbone, f'({N_dogbone:.0f}, {S_dogbone:.2f})', fontsize=10, va='bottom')

# Display Basquin's equation with the values of 'a' and 'b'
plt.text(10**-1, 10**3, f"Basquin's equation: S = {a} * (2Nf)^{b}", fontsize=10)

# Setting limits of the y-axis to maximize the view of the S-N curves
plt.ylim(min(S), max(S))

plt.xlabel('Number of Cycles to Failure (Nf)')
plt.ylabel('Stress Amplitude (σ_a / MPa)')
plt.title('S-N Curve for 4340 Steel')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()

# Save the figure as a PNG file
plt.savefig('sn_curve.png')
