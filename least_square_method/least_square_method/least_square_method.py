import numpy as np
from pprint import pprint

import gauss


X_IND = 0
Y_IND = 1
RO_IND = 2

def lsm(inp, polynominal_degree=1):
    
    #n_count = 3 #count of coordinates
    n_count = inp.shape[0]


    #inp = np.zeros(shape=(N_COUNT,RO_IND+1), dtype=np.longdouble) #0-x, 1-y,
    #2-ro

    #inp = [[1, 1, 1],
    #     [2, 4, 1],
    #     [3, 9, 1],
    #     [4, 16, 1],
    #     [5, 25, 1],
    #     [6, 36, 1],
    #     [7, 49, 1],
    #     [8, 64, 1],
    #     [9, 81, 1],
    #     [10, 100, 1]]

    #pprint(inp)

    #polynominal_degree = 2
    mas = np.zeros(shape=(polynominal_degree + 1, n_count))
    vec = np.zeros(shape=(n_count))


    for m in range(polynominal_degree + 1):
        for a in range(n_count):
            mas[m][a] = np.sum(inp[i][RO_IND] * inp[i][X_IND] ** (m + a) for i in range(n_count))

        vec[m] = np.sum(np.prod([inp[i][X_IND] ** m, inp[i][Y_IND], inp[i][RO_IND]]) for i in range(n_count))

    #pprint(mas)
    #pprint(vec)
    
    coefs = gauss.gauss(mas, vec)
    #pprint(coefs)
    #return coefs
    
    xs_for_approx=[]
    for k in range(polynominal_degree + 1):
        index = int(k / polynominal_degree * (n_count - 1))
        xs_for_approx.append(inp[index][X_IND])
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
        xs[i] = inp[i][X_IND]

  
    ys = np.zeros(shape=(n_count))
    for i in range(n_count):
        ys[i] = inp[i][Y_IND]

    return xs, ys





