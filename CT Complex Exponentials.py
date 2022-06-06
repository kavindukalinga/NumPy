from cmath import pi
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2, figsize=(16,4))

t = np.arange(-3*np.pi, 3*np.pi + np.pi/100, np.pi/100)

c = 1
omega0 = 1
phi = 0 
r=0.2
xt1 = np.abs(c)*np.exp(r*t)*np.cos(omega0*t + phi)
ax[0].plot(t/np.pi, xt1, label='$|c|e^(rt)\cos(\omega_0t + \phi$), $\omega_0={0}$, $\phi={1}\pi$'.format(omega0,phi/np.pi) )
ax[0].plot(t/np.pi, np.exp(r*t),'r--')
ax[0].plot(t/np.pi, -np.exp(r*t),'r--')
ax[0].set_ylabel('$x(t) = |c|e^{rt}\cos(\omega_0 t+ \phi)$, $r = 0.2$', loc='top', rotation=0)

c = 1
omega0 = 1
phi = 0 
r=-0.2
xt2 = np.abs(c)*np.exp(r*t)*np.cos(omega0*t + phi)
ax[1].plot(t/np.pi, xt2, label='$|c|e^(rt) \cos(\omega_0t + \phi)$, $\omega_0={0}$, $\phi={1}\pi$'.format(omega0,phi/np.pi) )
ax[1].plot(t/np.pi, np.exp(r*t),'r--')
ax[1].plot(t/np.pi, -np.exp(r*t),'r--')
ax[1].set_ylabel('$x(t) = |c|e^{rt}\cos(\omega_0 t+ \phi)$, $r = -0.2$', loc='top', rotation=0)

for i in range(2):
    ax[i].spines['left'].set_position('zero')
    ax[i].spines['right'].set_color('none')
    ax[i].spines['bottom'].set_position('zero')
    ax[i].spines['top'].set_color('none')
    ax[i].set_xlabel('$t/\pi$', loc='right')
    ax[i].xaxis.set_label_coords(1.05, 0.5)
    ax[i].yaxis.set_label_coords(0.7, 1.05)
    ax[i].grid(True)
    #ax[i].legend(loc='lower right')

plt.show()

#Python NumPy Tutorial
#Click https://cs231n.github.io/python-numpy-tutorial/ link to open resource.

