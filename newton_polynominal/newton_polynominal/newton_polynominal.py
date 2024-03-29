from collections import OrderedDict
import csv
from decimal import Decimal as D, ROUND_HALF_DOWN

class NewtonPolynominal(object):

    def __init__(self, y_by_x_resourse, inputed_coord, inputed_value, poly_degree):

        if inputed_coord=="x":
            self.y_by_x = y_by_x_resourse 
        else:
            self.y_by_x=OrderedDict()
            for k, v in y_by_x_resourse.items():
                self.y_by_x[v]=k

        #self.polynom_degree = len(self.y_by_x)
        self.inputed_x = inputed_value
        self.polynom = 0.0
        self.polynom_degree=int(poly_degree)+1

    def get_div_diff(self, xs):

        def div_delta_y_by_delta_x(ys, xs):
            delta_y = ys[0] - ys[1]
            delta_x = xs[0] - xs[-1]
        
            if delta_x != 0:
                return delta_y / delta_x
            else:
                return float("inf")


        len_xs = len(xs)

        if len_xs == 1:
            return self.y_by_x[xs[0]]

        elif len_xs == 2:
            ys = [self.y_by_x[x] for x in xs]
            return div_delta_y_by_delta_x(ys, xs)

        else:
            ys = []
            ys.append(self.get_div_diff(xs[:-1]))
            ys.append(self.get_div_diff(xs[1:]))

            return div_delta_y_by_delta_x(ys, xs)


    def get_x_product(self, xs):

        if len(xs) == 1:  
            return self.inputed_x - xs[0]

        else:
            delta_x = self.inputed_x - xs[0]
            return delta_x * self.get_x_product(xs[1:])


    def poly(self):

        xs = [x for x in self.y_by_x.keys()]

        xs.sort(key=lambda x: abs(x-self.inputed_x))
        xs=xs[:self.polynom_degree]
        xs.sort()
        #print(xs)

        for i in range(len(xs)):#self.polynom_degree): 
            x_prod_part = self.get_x_product(xs[:i]) if i != 0 else 1
            y_div_part = self.get_div_diff(xs[:i + 1])
            self.polynom +=  x_prod_part * y_div_part 


        return self.polynom   #+self.y_by_x[0]
