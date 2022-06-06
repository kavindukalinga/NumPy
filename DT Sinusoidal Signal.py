import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))

n = np.arange(-48,48+1,1)

A = 1
N = 12
omega0 = 2*np.pi/N
phi = 0
xn1 = A*np.cos(omega0*n + phi)
ax.stem(n,xn1, linefmt='b',markerfmt='bo', label='$A\cos(\omega_0n + \phi)$, $\omega_0 = 2*\pi/N$, $\phi = 0$')

phi = -np.pi/2
xn2 = A*np.cos(omega0*n + phi)
ax.stem(n,xn2, linefmt='r',markerfmt='ro', label='$A\cos(\omega_0n + \phi)$, $\omega_0 = 2*\pi/N$, $\phi = -\pi/2$')

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.set_xlabel('$n$', loc='right')
ax.xaxis.set_label_coords(1.05, 0.5)
ax.set_ylabel('$x[n]$', loc='top', rotation=0)
ax.yaxis.set_label_coords(0.5, 1.05)
ax.grid(True)
ax.legend(loc='lower right')
plt.show()

#Python NumPy Tutorial
#Click https://cs231n.github.io/python-numpy-tutorial/ link to open resource.
