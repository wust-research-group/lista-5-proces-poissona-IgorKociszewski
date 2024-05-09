import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
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

# S=Poisson(T,lambd)
# plt.step(S, np.arange(0, len(S), 1))

def N_t(poiss, T):
    p = np.asarray(poiss)
    n = np.zeros(len(T))
    for i in range(len(T)):
        n[i] = (p <= T[i]).sum()
    return n


n1 = np.zeros(100)
for i in range(100):
    P1 = Poisson(10,2)
    n1[i] = N_t(P1, [5])[0]

czas=np.arange(0,40,0.1)

sns.ecdfplot(n1, label="empiryczna")
plt.plot(czas,scipy.stats.poisson.cdf(czas,10),label="teoretyczna")
plt.legend()
plt.show()

