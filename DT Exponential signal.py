import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2, figsize=(12,6))

n = np.arange(-20,20+1,1)

c = 1
a = 0.92 # Positive
xn1 = c*a**n
ax[0].stem(n,xn1, linefmt='b',markerfmt='bo', label='$a^n$ , $a = {0}$'.format(a))

a=1.08
xn2 = c*a**n
ax[0].stem(n, xn2, linefmt='r',markerfmt='ro',label='$a^n$ , $a = {0}$'.format(a) )

ax[0].legend(loc='lower right')

ax[0].spines['left'].set_position('zero')
ax[0].spines['right'].set_color('none')
ax[0].spines['bottom'].set_position('zero')
ax[0].spines['top'].set_color('none')
ax[0].set_xlabel('$t$', loc='right')
ax[0].xaxis.set_label_coords(1.05, 0.05)
ax[0].set_ylabel('$x(t)$', loc='top', rotation=0)
ax[0].yaxis.set_label_coords(0.5, 1.05)
ax[0].grid(True)

a = -0.92 # Positive
xn3 = c*a**n
ax[1].stem(n,xn3, linefmt='b',markerfmt='bo', label='$a^n$ , $a = {0}$'.format(a))

a=-1.08
xn4 = c*a**n
ax[1].stem(n, xn4,linefmt='r',markerfmt='ro', label='$a^n$ , $a = {0}$'.format(a) )

ax[1].legend(loc='lower right')

ax[1].spines['left'].set_position('zero')
ax[1].spines['right'].set_color('none')
ax[1].spines['bottom'].set_position('zero')
ax[1].spines['top'].set_color('none')
ax[1].set_xlabel('$t$', loc='right')
ax[1].xaxis.set_label_coords(1.05, 0.5)
ax[1].set_ylabel('$x(t)$', loc='top', rotation=0)
ax[1].yaxis.set_label_coords(0.5, 1.05)
ax[1].grid(True)

plt.show()

#Python NumPy Tutorial
#Click https://cs231n.github.io/python-numpy-tutorial/ link to open resource.

