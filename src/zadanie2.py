import numpy as np
import matplotlib.pyplot as plt
def Poisson(T,lambd):
    S=[0]
    t=0
    I=0
    while True:
        u= np.random.rand()
        t-=1/lambd*(np.log(u))
        if t<T:
            I+=1
            S.append(t)
        else:
            return S

lambd=2
T=10

def N_t(poiss, T ,lamb):
    p = np.asarray(poiss)
    n = np.zeros(len(T))
    for i in range(len(T)):
        n[i] = (p <= T[i]).sum() - lamb*T[i]
    return n
t = np.arange(0, 10, 0.1)

p1=Poisson(10,2)
n1=N_t(p1,t,2)

plt.plot(t,n1,label="kompensowany")
plt.legend()
plt.show()