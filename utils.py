import numpy as np
from scipy.integrate import dblquad
import scipy

#Para el calculo de los coeficientes de Fourier
def calc_cnm(n,m,f,l1,l2):
    c = np.zeros(n,m)
    freq1 = np.pi*n/l1
    freq2 = np.pi*m/l2
    fi = lambda x,y: f(x,y)*np.sin(freq1*x)*np.sin(freq2*y)
    for i in range(n):
        for j in range(m):
            c[i,j] = dblquad(fi,0,l1,0,l2)
    return c

