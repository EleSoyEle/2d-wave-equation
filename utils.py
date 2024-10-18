import numpy as np
from scipy.integrate import dblquad
import scipy

#Para el calculo de los coeficientes de Fourier
def calc_cnm(n,m,f,l1,l2):
    c = np.zeros(shape=[n,m])
    for i in range(n):
        for j in range(m):
            freq1 = np.pi*(i+1)/l1
            freq2 = np.pi*(j+1)/l2
            fi = lambda x,y: f(x,y)*np.sin(freq1*x)*np.sin(freq2*y)
            integ = dblquad(fi,0,l1,0,l2)
            c[i,j] = 4*integ[0]/(l1*l2)
    return c

def calc_sin_cos(n,m,l1,l2,x,y):
    s1 = []
    s2 = []
    for i in range(max(n,m)):
        tq = np.pi*(i+1)
        s1.append(np.sin(tq*x/l1))
        s2.append(np.sin(tq*y/l2))
    return s1,s2


def calc_cos_t(n,m,v,t,l1,l2):
    sp = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            sp[i,j] = np.cos(np.pi*v*np.sqrt(pow((i+1)/l1,2)+pow((j+1)/l2,2))*t)

    return sp
