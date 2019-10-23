import numpy as np
from pprint import pprint

import gauss

def lsm(inp, polynominal_degree=1):
    
    #n_count = 3 #count of coordinates
    n_count=inp.shape[0]

    X_IND = 0
    Y_IND = 1
    RO_IND = 2

    #inp = np.zeros(shape=(N_COUNT,RO_IND+1), dtype=np.longdouble) #0-x, 1-y, 2-ro

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
    mas = np.zeros(shape=(polynominal_degree+1, n_count))
    vec=np.zeros(shape=(n_count))


    for m in range(polynominal_degree+1):
        for a in range(n_count):
            mas[m][a] = np.sum(inp[i][RO_IND] * inp[i][X_IND] ** (m + a) for i in range(n_count))

        vec[m] = np.sum(np.prod([inp[i][X_IND] ** m, inp[i][Y_IND], inp[i][RO_IND]]) for i in range(n_count))

    #pprint(mas)
    #pprint(vec)
    
    coefs=gauss.gauss(mas, vec)
    #pprint(coefs)
    return coefs



