from collections import OrderedDict

from newton_polynominal import NewtonPolynominal


def get_xy_ordered_dict():
    y_by_x = OrderedDict()
    y_by_x[0.0] = 0.0
    y_by_x[1.0] = 1.0
    y_by_x[2.0] = 4.0
    y_by_x[3.0] = 9.0
    y_by_x[4.0] = 16.0
    return y_by_x


p=NewtonPolynominal(y_by_x_resourse=get_xy_ordered_dict(),
                    x_0=0.0,
                    x_n=4.0,
                    step=10,
                    polynom_degree=4,
                    inputed_x=1.5)

p.poly()
print(p.polynom)

assert p.polynom == 2.25
