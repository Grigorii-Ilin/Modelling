import numpy as np
from pprint import pprint

N_COUNT = 2 #count of coordinates
X = 0
Y = 1
RO = 2

inp = np.zeros(shape=(N_COUNT,3), dtype=float) #0-x, 1-y, 2-ro
inp = [[1, 1, 0.5],
     [2, 4, 0.5],
     [3, 9, 0.5],
     [4, 16, 0.5],
     [5, 25, 0.5],
     [6, 36, 0.5],
     [7, 49, 0.5],
     [8, 64, 0.5],
     [9, 81, 0.5],
     [10, 100, 0.5]]

pprint(inp)

n = 1#polynominal_degree=
mas = np.zeros(shape=(N_COUNT+1, N_COUNT))

for m in range(N_COUNT):
    for a in range(N_COUNT):
        mas[a][m] = np.sum(inp[RO][i] * inp[X][i] ** (m + a) for i in range(N_COUNT))

    #i=2
    #tmp=inp[X][i] ** m * inp[Y][i] * inp[RO][i] 
    mas[N_COUNT][m] = np.sum(inp[X][i] ** m * inp[Y][i] * inp[RO][i] for i in range(N_COUNT))

pprint(mas)
    




