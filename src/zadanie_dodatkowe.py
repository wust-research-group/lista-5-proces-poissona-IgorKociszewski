import numpy as np
import math
import matplotlib.pyplot as plt
def generuj_poissona(lambda_param):
    n = 1
    a = 1

    while True:
        U = np.random.uniform(0, 1)
        a *= U
        if a >= math.exp(-lambda_param):
            n += 1
        else:
            return n - 1

lambda_param = 1
X=[]
for i in range(1000):
    X.append(generuj_poissona(lambda_param))
print( X)
plt.plot(X)
plt.show()