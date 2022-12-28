import matplotlib.pyplot as plt
import numpy as np

h = 1
t_range = np.arange(1, 1000+1)

def position(t, h):
    return np.sin(t) + np.cos(t)*h

def velocity(t, h):
    return np.cos(t) - np.sin(t)*h

plt.plot(position(t_range, h), velocity(t_range, h), linewidth=0.5)

plt.xlabel('position')
plt.ylabel('y - axis')

plt.axis('equal')

plt.show()
