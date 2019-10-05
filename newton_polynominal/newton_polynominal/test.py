from collections import OrderedDict
#import math

from newton_polynominal import NewtonPolynominal


def get_xy_x_square():
    y_by_x = OrderedDict()
    y_by_x[0.0] = 0.0
    y_by_x[1.0] = 1.0
    y_by_x[2.0] = 4.0
    y_by_x[3.0] = 9.0
    y_by_x[4.0] = 16.0
    return y_by_x


def get_xy_cos_x_minus_x():
    y_by_x = OrderedDict()
    y_by_x[0.0] = 1.0
    y_by_x[0.5] = 0.377583
    y_by_x[1.0] = -0.459698
    y_by_x[1.5] = -1.42926
    y_by_x[2.0] = -2.41615
    #y_by_x[3.0] = -3.98999
    #y_by_x[4.0] = -4.465364
    return y_by_x


p=NewtonPolynominal(y_by_x_resourse=get_xy_x_square(), inputed_coord="x", inputed_value=1.5, poly_degree=1)
p.poly()
print(p.polynom)
assert round(p.polynom, 2) == 2.25

p=NewtonPolynominal(y_by_x_resourse=get_xy_cos_x_minus_x(), inputed_coord="y", inputed_value=0, poly_degree=2)
p.poly()
print(p.polynom)
assert round(p.polynom, 2) == 0.74

input()
