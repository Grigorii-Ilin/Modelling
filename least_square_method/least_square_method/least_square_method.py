import numpy as np
from pprint import pprint

import gauss

N_COUNT = 2 #count of coordinates

X_IND = 0
Y_IND = 1
RO_IND = 2

inp = np.zeros(shape=(N_COUNT,RO_IND+1), dtype=np.longdouble) #0-x, 1-y, 2-ro

inp = [[1, 1, 1],
     [2, 4, 1],
     [3, 9, 1],
     [4, 16, 1],
     [5, 25, 1],
     [6, 36, 1],
     [7, 49, 1],
     [8, 64, 1],
     [9, 81, 1],
     [10, 100, 1]]

pprint(inp)

n = 1#polynominal_degree
mas = np.zeros(shape=(n+1, N_COUNT))
vec=np.zeros(shape=(N_COUNT))


for m in range(n+1):
    for a in range(N_COUNT):
        mas[m][a] = np.sum(inp[i][RO_IND] * inp[i][X_IND] ** (m + a) for i in range(N_COUNT))

    vec[m] = np.sum(np.prod([inp[i][X_IND] ** m, inp[i][Y_IND], inp[i][RO_IND]]) for i in range(N_COUNT))

pprint(mas)
pprint(vec)
    
coefs=gauss.gauss(mas, vec)
pprint(coefs)



