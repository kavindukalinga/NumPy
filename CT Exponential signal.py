import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2, figsize=(12,6))

t = np.arange(-1,3,0.01)

c = 1
t0 = 0
a = 1 # Positive
xt1 = c*np.exp(a*t+ t0)
ax[0].plot(t, xt1, label='$e^{t}$' )

a=1.2
xt2 = c*np.exp(a*t+ t0)
ax[0].plot(t, xt2, label='$e^{1.2t}$' )

ax[0].legend(loc='lower right')

ax[0].spines['left'].set_position('zero')
ax[0].spines['right'].set_color('none')
ax[0].spines['bottom'].set_position('zero')
ax[0].spines['top'].set_color('none')
ax[0].set_xlabel('$t$', loc='right')
ax[0].xaxis.set_label_coords(1.05, 0.05)
ax[0].set_ylabel('$x(t)$', loc='top', rotation=0)
ax[0].yaxis.set_label_coords(0.3, 1.05)
ax[0].grid(True)

a=-1
xt3 = c*np.exp(a*t+ t0)
ax[1].plot(t, xt3, label='$e^{-t}$' )

a=-1.2
xt4 = c*np.exp(a*t+ t0)
ax[1].plot(t, xt4, label='$e^{-1.2t}$' )

ax[1].legend(loc='lower right')

ax[1].spines['left'].set_position('zero')
ax[1].spines['right'].set_color('none')
ax[1].spines['bottom'].set_position('zero')
ax[1].spines['top'].set_color('none')
ax[1].set_xlabel('$t$', loc='right')
ax[1].xaxis.set_label_coords(1.05, 0.05)
ax[1].set_ylabel('$x(t)$', loc='top', rotation=0)
ax[1].yaxis.set_label_coords(0.3, 1.05)
ax[1].grid(True)

plt.show()

#Python NumPy Tutorial
#Click https://cs231n.github.io/python-numpy-tutorial/ link to open resource.

