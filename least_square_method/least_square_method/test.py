import numpy as np

import least_square_method

inp = np.array([[1, 1, 1],
                [2, 4, 1]])

coefs = least_square_method.lsm(inp, polynominal_degree=1)

assert coefs[0] == 3.0
assert coefs[1] == -2.0

print('ok')