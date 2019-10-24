import numpy as np
import matplotlib.pyplot as plt

import least_square_method


inp = np.array([[1, 1, 2],
             [2, 4, 1],
             [3, 9, 1]])
             #[4, 16, 1],
             #[5, 25, 1],
             #[6, 36, 1],
             #[7, 49, -10000],
             #[8, 64, 1],
             #[9, 81, 1],
             #[10, 100, 1]]
             #  )

polynominal_degree = 1

#coefs = least_square_method.lsm(inp, polynominal_degree)
#xs, ys, ys_by_coefs = least_square_method.lsm(inp, polynominal_degree)

xs, ys=least_square_method.get_coords(inp)

plt.plot(xs,ys)
plt.scatter(xs, ys) 

xs_for_approx, ys_by_coefs = least_square_method.lsm(inp, polynominal_degree)

plt.plot(xs_for_approx, ys_by_coefs)
plt.scatter(xs_for_approx, ys_by_coefs) 


plt.show()
