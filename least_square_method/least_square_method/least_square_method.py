import numpy as np
from pprint import pprint

import gauss


X_ID = 0
Y_ID = 1
RO_ID = 2

def lsm(inp, polynom_degree=1):
   
    N = inp.shape[0]#count of coordinates

    mas = np.zeros(shape=(polynom_degree + 1, N))
    vec = np.zeros(shape=(N))

    for m in range(polynom_degree + 1):
        for a in range(N):
            mas[m][a] = np.sum(inp[i][RO_ID] * inp[i][X_ID] ** (m + a) for i in range(N))

        vec[m] = np.sum(np.prod([inp[i][X_ID] ** m, inp[i][Y_ID], inp[i][RO_ID]]) for i in range(N))

    coefs = gauss.gauss(mas, vec)
    
    xs_for_approx=[]
    for k in range(polynom_degree + 1):
        index = int(k / polynom_degree * (N - 1))
        xs_for_approx.append(inp[index][X_ID])
    xs_for_approx=np.array(xs_for_approx)

    ys_by_coefs = np.zeros(shape=(polynom_degree + 1))
    for i in range(polynom_degree + 1):
        y = 0.0
        for k in range(polynom_degree + 1):         
            y+=coefs[k] * xs_for_approx[i] ** k
        ys_by_coefs[i] = y          

    return xs_for_approx, ys_by_coefs


def get_coords(inp):
    N = inp.shape[0]

    xs = np.zeros(shape=(N))
    for i in range(N):
        xs[i] = inp[i][X_ID]

    ys = np.zeros(shape=(N))
    for i in range(N):
        ys[i] = inp[i][Y_ID]

    return xs, ys





