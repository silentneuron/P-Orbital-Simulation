import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#  Define spherical coordinates first
n_points = 80
theta = np.linspace(0, np.pi, n_points)     # polar angle 0..π
phi = np.linspace(0, 2*np.pi, n_points)     # azimuthal angle 0..2π
r = np.linspace(0, 10, n_points)            # radial distance

theta, phi, r = np.meshgrid(theta, phi, r, indexing='ij')

# 2. Select an orbital ψ (hydrogen-like)  ψ -Gives us the wave function or the probablity of finding an electron
# Lets take. a0 = Bohr radius (et to 1 for simplicity)
a0 = 1.0

def R_1s(r):
    return 2*np.exp(-r/a0)

def R_2s(r):
    return (1/np.sqrt(2))* (1 - r/(2*a0))*np.exp(-r/(2*a0))

def R_2p(r):
    return (1/(2*np.sqrt(6)))* (r/a0)*np.exp(-r/(2*a0))

# Angular parts (spherical harmonics without full normalization constants)
def Y_00(theta, phi):
    return np.ones_like(theta)/(2*np.sqrt(np.pi))

def Y_10(theta, phi):
    return np.sqrt(3/(4*np.pi))*np.cos(theta)

def Y_11(theta, phi):
    return -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(1j*phi)  # complex

# Choose which orbital to plot ur wish
# For Example: 2pz orbital => R_2p * Y_10 (real)
psi = R_2p(r) * Y_10(theta, phi)

# Probability density and phase
psi_real = np.real(psi)
density = psi_real**2

# Next onvert spherical to cartesian for plotting 
x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)

# Plot isosurface using scatter (simpler than true isosurface) isosurface is analogus to contour
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

# Choose an isovalue (just a visual cutoff)
mask = density > 0.005  
# tune for visibility more the value the more the probablity limit
# its like a filter you will understand when u change the values

# Color by sign of wavefunction usefull for understanding hybridisation
colors = np.where(psi_real[mask] > 0, 'red', 'blue')

ax.scatter(x[mask], y[mask], z[mask], c=colors, s=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Hydrogen 2pz orbital")
plt.show()

