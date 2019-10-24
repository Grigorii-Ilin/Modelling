import numpy as np
from pprint import pprint

import gauss


X_ID = 0
Y_ID = 1
RO_ID = 2

def lsm(inp, polynominal_degree=1):
   
    N = inp.shape[0]#count of coordinates

    mas = np.zeros(shape=(polynominal_degree + 1, N))
    vec = np.zeros(shape=(N))

    for m in range(polynominal_degree + 1):
        for a in range(N):
            mas[m][a] = np.sum(inp[i][RO_ID] * inp[i][X_ID] ** (m + a) for i in range(N))

        vec[m] = np.sum(np.prod([inp[i][X_ID] ** m, inp[i][Y_ID], inp[i][RO_ID]]) for i in range(N))

    #pprint(mas)
    #pprint(vec)
    
    coefs = gauss.gauss(mas, vec)
    #pprint(coefs)
    #return coefs
    
    xs_for_approx=[]
    for k in range(polynominal_degree + 1):
        index = int(k / polynominal_degree * (N - 1))
        xs_for_approx.append(inp[index][X_ID])
    xs_for_approx=np.array(xs_for_approx)

    ys_by_coefs = np.zeros(shape=(polynominal_degree + 1))
    #for x in xs:
    for i in range(polynominal_degree + 1):#(n_count):
        y = 0.0
        for k in range(polynominal_degree + 1):         
            y+=coefs[k] * xs_for_approx[i] ** k
        ys_by_coefs[i] = y          

    #xs=np.array([inp[0][0], inp[1][0]])
    #ys=np.array([inp[0][1], inp[1][1]])

    return xs_for_approx, ys_by_coefs


def get_coords(inp):
    n_count = inp.shape[0]

    xs = np.zeros(shape=(n_count))
    for i in range(n_count):
        xs[i] = inp[i][X_ID]

  
    ys = np.zeros(shape=(n_count))
    for i in range(n_count):
        ys[i] = inp[i][Y_ID]

    return xs, ys





