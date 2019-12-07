from data_getter import Data
from method import thomas_algorithm
from numpy import arange
import matplotlib.pyplot as plt

#d=Data()


def left_boundary_conditions(d):
    X_half = d.Xn_plus_half(d.x0)
    p1 = d.p(d.x0 + d.h)
    f1 = d.f(d.x0 + d.h)

    p0 = d.p(d.x0)
    f0 = d.f(d.x0)

    p_half = (p0 + p1) / 2

    K0 = X_half + d.h * d.h * p_half / 8 + d.h * d.h * p0 / 4
    M0 = d.h * d.h * p_half / 8 - X_half
    P0 = d.h * d.F0 + d.h * d.h * (3 * f0 + f1) / 4

    return K0, M0, P0


def right__boundary_conditions(d):
    X_half = d.Xn_minus_half(d.l)

    pN = d.p(d.l)
    pN1 = d.p(d.l - d.h)
    fN = d.f(d.l)
    fN1 = (2 * d.alpha(d.l - d.h)) / d.R * d.Tenv

    KN = - (X_half + d.alphaN * d.h) / d.h - d.h * (5 * pN + pN1) / 16
    MN = X_half / d.h - d.h * (pN + pN1) / 16
    PN = - d.alphaN * d.Tenv - d.h * (3 * fN + fN1) / 8

    return KN, MN, PN


def calc_coefficients(d):
    A = []
    B = []
    C = []
    D = []

    for i in arange(d.x0, d.l, d.h):
        An = d.Xn_minus_half(i) / d.h
        Cn = d.Xn_plus_half(i) / d.h
        Bn = An + Cn + d.p(i) * d.h
        Dn = d.f(i) * d.h

        A.append(An)
        B.append(Bn)
        C.append(Cn)
        D.append(Dn)

    return A, B, C, D


def main_proc(data):
    a, b, c, d = calc_coefficients(data)
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    k0, m0, p0 = left_boundary_conditions(data)
    # print(k0)
    # print(m0)
    # print(p0)

    kN, mN, pN = right__boundary_conditions(data)
    # print(kN)
    # print(mN)
    # print(pN)

    T = thomas_algorithm(a, b, c, d, k0, m0, p0, kN, mN, pN)
    print(T)
    x = arange(data.x0, data.l, data.h)

    plt.title('Heating the rod')
    plt.grid(True)
    plt.plot(x, T, 'r', linewidth=0.5)
    plt.xlabel("Length (cm)")
    plt.ylabel("Temperature (K)")

    plt.savefig("plot.png")

    plt.show()


