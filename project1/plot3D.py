import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

N = np.linspace(-2,2,400)

def x(n):
    return (np.e**((1j*np.pi*n))*(np.e**(0*n)))

sinal = x(N)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(N, sinal.real, 0, color="#3d5b59")
ax.plot(N, 0, sinal.imag, color="#5b3d3d")
ax.plot(N, sinal.real, sinal.imag, color="#000000")

ax.set_xlabel('n')
ax.set_ylabel('Re{y(n)}')
ax.set_zlabel('x')

ax.minorticks_on()
ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

plt.show()