class Data:

    def __init__(
        self,
        l = 10,           # Length of the rod (cm)
        R = 0.5,          # Radius of the rod (cm)
        Tenv = 300,       # Ambient temperature (K)
        F0 = 100,        # Heat flux density (W / (cm^2 * K))
        k0 = 0.2,         # Coefficient of thermal conductivity at the beginning of the rod (W / (cm * K))
        kN = 0.5,         # Coefficient of thermal conductivity at the end of the rod (W / (cm * K))
        alpha0 = 1e-2,    # Heat transfer coefficient at the beginning of the rod (W / (cm^2 * K))
        alphaN = 9e-3,  # Heat transfer coefficient at the end of the rod (W / (cm^2 * K))
        h=1e-2):

        self.l=l
        self.R=R
        self.Tenv=Tenv
        self.F0=F0
        self.k0=k0
        self.kN=kN
        self.alpha0=alpha0
        self.alphaN=alphaN
        self.h=h

        self.x0=0
        #h = 1e-2
        self.bk = (self.kN * self.l) / (self.kN - self.k0)
        self.ak = - self.k0 * self.bk
        self.b_alpha = (self.alphaN * self.l) / (self.alphaN - self.alpha0)
        self.a_alpha = - self.alpha0 * self.b_alpha


    def k(self, x):
        return self.ak / (x - self.bk)

    def alpha(self, x):
        return self.a_alpha / (x - self.b_alpha)

    def Xn_plus_half(self, x):
        return (2 * self.k(x) * self.k(x + self.h)) / (self.k(x) + self.k(x + self.h))

    def Xn_minus_half(self, x):
        return (2 * self.k(x) * self.k(x - self.h)) / (self.k(x) + self.k(x - self.h))

    def p(self, x):
        return 2 * self.alpha(x) / self.R

    def f(self, x):
        return 2 * self.alpha(x) / self.R * self.Tenv

