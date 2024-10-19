import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter,writers
from utils import calc_cnm,calc_sin_cos,calc_cos_t

#Numero de iteraciones maximas en las suams
n = 10
m = 10
#Definimos el contorno
l1 = 10
l2 = 10
v = 10
#Definimos las iteraciones totales de la simulacion
epochs = 100

t0 = 0
t1 = 2


def f1(x,y):
    return x*(l1-x)*y*(l2-y)*(np.exp(-(x)**2-(y)**2))


res = 200
x0 = np.linspace(0,l1,res)
x1 = np.linspace(0,l2,res)
X,Y = np.meshgrid(x0,x1)
time_t = np.linspace(t0,t1,epochs)


c = calc_cnm(n,m,f1,l1,l2)

def calc_frames():
    frames = []
    s1,s2 = calc_sin_cos(n,m,l1,l2,X,Y)
    for epoch in range(epochs):
        ct = calc_cos_t(n,m,v,time_t[epoch],l1,l2)
        u = np.zeros((res,res))
        for i in range(n):
            for j in range(m):
                u += c[i,j]*s1[i]*s2[j]*ct[i,j]
        frames.append(u)
    return frames


frames = calc_frames()

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()

def animate(i):
    print(i)
    ax.clear()
    ax.pcolormesh(X,Y,frames[i],vmin=np.min(frames),vmax=np.max(frames),cmap='viridis')
    ax.axis("off")
ani = FuncAnimation(fig,animate,epochs,interval=0.1)
#plt.show()

ffmpeg_writer = writers['ffmpeg']

# Ajustes de calidad del video
writer = ffmpeg_writer(fps=32, codec='mpeg4', bitrate=5000)

# Guardar la animación como archivo MP4
ani.save("video.gif", writer=writer,dpi=350)
