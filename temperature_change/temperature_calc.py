from data_getter import Data
import numpy as np
import matplotlib.pyplot as plt


def left_boundary_conditions(d):
    X_half = d.Kappa_plus_half(d.x0)

    p1 = d.p(d.x0 + d.h)
    f1 = d.f(d.x0 + d.h)

    p0 = d.p(d.x0)
    f0 = d.f(d.x0)

    p_half = (p0 + p1) / 2

    K0 = X_half + d.h * d.h * p_half / 8 + d.h * d.h * p0 / 4
    M0 = d.h * d.h * p_half / 8 - X_half
    P0 = d.h * d.F0 + d.h * d.h * (3 * f0 + f1) / 4

    return K0, M0, P0


def right_boundary_conditions(d):
    X_half = d.Kappa_minus_half(d.l)

    pN = d.p(d.l)
    pN1 = d.p(d.l - d.h)

    fN = d.f(d.l)
    fN1 = (2 * d.alpha(d.l - d.h)) / d.R * d.Te

    KN = - (X_half + d.alphaN * d.h) / d.h - d.h * (5 * pN + pN1) / 16
    MN = X_half / d.h - d.h * (pN + pN1) / 16
    PN = - d.alphaN * d.Te - d.h * (3 * fN + fN1) / 8

    return KN, MN, PN


def calc_coefficients(data):
    A = []#e.g. C
    B = []
    C = []#e.g. A
    D = []#e.g. F

    for i in np.arange(data.x0, data.l, data.h):
        An = data.Kappa_minus_half(i) / data.h
        Cn = data.Kappa_plus_half(i) / data.h
        Bn = An + Cn + data.p(i) * data.h
        Dn = data.f(i) * data.h

        A.append(An) 
        B.append(Bn)
        C.append(Cn) 
        D.append(Dn) 

    return A, B, C, D


def calc_T(A, B, C, D, K0, M0, P0, KN, MN, PN):  

    xi = [None, - M0 / K0]
    eta = [None, P0 / K0]

    # Прямой проход
    for i in range(1, len(A)):
        x = C[i] / (B[i] - A[i] * xi[i])
        e = (D[i] + A[i] * eta[i]) / (B[i] - A[i] * xi[i])

        xi.append(x)
        eta.append(e)

    # Обратный проход
    ys = [(PN - MN * eta[-1]) / (KN + MN * xi[-1])]

    for i in range(len(A) - 2, -1, -1):
        y_i = xi[i + 1] *  ys[0] + eta[i + 1]

        ys.insert(0, y_i)

    return ys


def main_proc(data):
    a, b, c, d = calc_coefficients(data)
    k0, m0, p0 = left_boundary_conditions(data)
    kN, mN, pN = right_boundary_conditions(data)
    
    T = calc_T(a, b, c, d, k0, m0, p0, kN, mN, pN)
    x = np.arange(data.x0, data.l, data.h)

    plt.title('Нагревание стержня')
    plt.grid(True)
    plt.plot(x, T, 'r', linewidth=0.8)
    plt.xlabel("Длина (см)")
    plt.ylabel("Температура (K)")

    plt.savefig("plot.png")

    plt.show()


