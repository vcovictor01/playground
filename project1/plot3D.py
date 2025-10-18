#-------------------------------------------
#IMPORTS
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib.animation import FuncAnimation

#-------------------------------------------
#FUNCTION
T = np.linspace(-2,2,800) #X AXE: TEMPORAL
xAxe = T 

def signalFunction(n):
    #return (np.e**((1j*2*np.pi*n))*(np.e**(0*n)))
    return (np.e**((1j*2*np.pi*n)+(np.pi*1j*1/2)))*(np.e**(-1*n))

signal = signalFunction(T)
yAxe = signal.real #Y AXE: REAL
zAxe = signal.imag#Z AXE: IMAG

#-------------------------------------------
#PLOT

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#ax.plot(xAxe, yAxe, -1, color="#3d5b59")
#ax.plot(xAxe, -1, zAxe, color="#5b3d3d")
#ax.plot(xAxe, yAxe, zAxe, color="#000000") #COMPLETE PLOT OF THE SIGNAL

ax.plot(0, 0, zAxe, color="#0000006A")
ax.plot(0, yAxe, 0, color="#0000006A")
ax.plot(xAxe, 0, 0, color="#0000006A") #PLOT OF AXES

ax.set_xlabel('t (s)')
ax.set_ylabel('Real')
ax.set_zlabel('Imaginario') #LABELS

ax.grid(False)
#ax.minorticks_on()
#ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
#ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

ax.set_axis_off()

ax.set_xlim(np.min(xAxe), np.max(xAxe))
ax.set_ylim(np.min(yAxe), np.max(yAxe))
ax.set_zlim(np.min(zAxe), np.max(zAxe)) #AXES LIMITS

#-------------------------------------------

linha3D, = ax.plot([], [], [], color="#181313FF", lw=2)
linha2Dreal, = ax.plot([], [], [], color="#3d5b59", lw=2,linestyle='--')
linha2Dimag, = ax.plot([], [], [], color="#5b3d3d", lw=2,linestyle='--') #LINE ANIMATIONS

N = len(T)
total_frames = 2 * N

def update(frame):
    if frame < N:
        # desenha até o índice `frame` (0 .. frame-1)
        linha3D.set_data([], [])     # X = tempo, Y = parte real
        linha3D.set_3d_properties(0)          # Z = parte imaginária

        linha2Dreal.set_data(xAxe[:frame], yAxe[:frame])
        linha2Dreal.set_3d_properties(0) 

        linha2Dimag.set_data(xAxe[:frame], np.zeros_like(T[:frame]))
        linha2Dimag.set_3d_properties(zAxe[:frame]) 

        #ax.view_init(elev=30, azim=frame * 0.5)

    else:
        idx = frame - N
        #desenha até o índice `frame` (0 .. frame-1)
        linha3D.set_data(xAxe[:idx], yAxe[:idx])     # X = tempo, Y = parte real
        linha3D.set_3d_properties(zAxe[:idx])          # Z = parte imaginária

        linha2Dreal.set_data(xAxe, yAxe)
        linha2Dreal.set_3d_properties(0) 

        linha2Dimag.set_data(xAxe, np.zeros_like(T))
        linha2Dimag.set_3d_properties(zAxe) 

        #ax.view_init(elev=30, azim=frame * 0.5)

    return linha3D, linha2Dreal, linha2Dimag

ani = FuncAnimation(fig, update, frames=total_frames, interval=15, blit=False, repeat=False)

plt.show()