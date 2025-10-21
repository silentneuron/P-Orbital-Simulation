# P-Orbital-Simulation

An interactive Python tool to visualize **electron orbitals** (s, p, d) in 3D space.  
Great for chemistry students and teachers to understand **orbital shapes** and **electron density distribution**.

---

##  Features
-  3D visualization of s, p, and d orbitals  
-  Color-coded orbitals based on phase  
-  Interactive rotation using matplotlib  
-  Mathematical representation of orbitals using **spherical harmonics**  

---

##  How It Works

- Electron orbitals are represented as **wavefunctions** `ψ(r, θ, φ)`  from Schrödinger equation
- The **probability density** is `|ψ(r, θ, φ)|²`  
- Different orbitals:
  - **s-orbital**: spherical symmetry  
  - **p-orbital**: dumbbell-shaped along x, y, or z axes  
  - **d-orbital**: cloverleaf or donut shapes  

The visualization uses **isosurfaces** to represent regions of **constant probability density**, giving a clear 3D shape of the orbital.

---

##  Requirements

Flash the python program download the library done!

```bash
pip install numpy matplotlib ipywidgets

