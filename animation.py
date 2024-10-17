import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import calc_cnm

#Numero de iteraciones maximas en las suams
n = 10
m = 10
#Definimos el contorno
l1 = 1
l2 = 1
v = 1
#Definimos las iteraciones totales de la simulacion
epochs = 1000


f1 = lambda x,y: np.exp((-x**2-y**2)/0.1)
c = calc_cnm(n,m,)

