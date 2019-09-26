from collections import OrderedDict

import newton_polynominal as poly #import get_x_product, get_div_diff, y_by_x, inputed_x


def get_xy_ordered_dict():
    y_by_x = OrderedDict()
    y_by_x[0.0] = 0.0
    y_by_x[1.0] = 1.0
    y_by_x[2.0] = 4.0
    y_by_x[3.0] = 9.0
    y_by_x[4.0] = 16.0
    return y_by_x

poly.y_by_x = get_xy_ordered_dict()
polynom = 0
poly.inputed_x = 1.5
xs = [x for x in poly.y_by_x.keys()]

for i in range(len(poly.y_by_x)):
    x_prod_part = poly.get_x_product(xs[:i]) if i != 0 else 1
    y_div_part = poly.get_div_diff(xs[:i + 1])
    polynom += x_prod_part * y_div_part 

print(polynom)
assert polynom == 2.25
