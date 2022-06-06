import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,4))

t = np.arange(-3*np.pi, 3*np.pi + np.pi/100, np.pi/100)

A = 1
omega0 = 1
phi = 0
xt1 = A*np.cos(omega0*t + phi)
ax.plot(t/np.pi, xt1, label='$A\cos(\omega_0t + \phi)$, $\omega_0 = {0}$, $\phi = 0$'.format(omega0))

phi = -np.pi/2
xt2 = A*np.cos(omega0*t + phi)
ax.plot(t/np.pi, xt2, label='$A\cos(\omega_0t + \phi)$, $\omega_0 = {0}$, $\phi = {1}\pi$'.format(omega0, phi/np.pi))

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.set_xlabel('$t/\pi$', loc='right')
ax.xaxis.set_label_coords(1.05, 0.5)
ax.set_ylabel('$x(t)$', loc='top', rotation=0)
ax.yaxis.set_label_coords(0.5, 1.05)
ax.grid(True)
ax.legend(loc='lower right')
plt.show()

#Python NumPy Tutorial
#Click https://cs231n.github.io/python-numpy-tutorial/ link to open resource.
