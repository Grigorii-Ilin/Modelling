from collections import OrderedDict


def get_xy_ordered_dict():
    y_by_x = OrderedDict()

    y_by_x[0.0] = 0.0
    y_by_x[1.0] = 1.0
    y_by_x[2.0] = 4.0
    y_by_x[3.0] = 9.0
    y_by_x[4.0] = 16.0

    return y_by_x


def div_delta_y_by_delta_x(ys, xs):
    delta_y = ys[0] - ys[1]
    delta_x = xs[0] - xs[-1]
        
    if delta_x != 0:
        return delta_y / delta_x
    else:
        return float("inf")


def get_div_diff(xs):
    len_xs = len(xs)

    if len_xs == 1:
        return y_by_x[xs[0]]

    elif len_xs == 2:
        ys = [y_by_x[x] for x in xs]
        return div_delta_y_by_delta_x(ys, xs)

    else:
        ys = []
        ys.append(get_div_diff(xs[:-1]))
        ys.append(get_div_diff(xs[1:]))

        return div_delta_y_by_delta_x(ys, xs)


def get_x_product(xs):
    if len(xs) == 1:  
        return inputed_x - xs[0]

    else:
        delta_x = inputed_x - xs[0]
        return delta_x * get_x_product(xs[1:])


y_by_x = get_xy_ordered_dict()
polynom = 0
inputed_x = 1.5
xs = [x for x in y_by_x.keys()]

for i in range(len(y_by_x)):
    x_prod_part = get_x_product(xs[:i]) if i != 0 else 1
    y_div_part = get_div_diff(xs[:i + 1])
    polynom +=  x_prod_part * y_div_part 

print(polynom)
