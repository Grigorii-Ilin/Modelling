class Data:

    def __init__(self, l, R, Te, F0, k0, kN, alpha0, alphaN, h=1e-2):

        self.l=l
        self.R=R
        self.Te=Te
        self.F0=F0
        self.k0=k0
        self.kN=kN
        self.alpha0=alpha0
        self.alphaN=alphaN
        self.h=h

        self.x0=0

        self.bk = (self.kN * self.l) / (self.kN - self.k0)
        self.ak = - self.k0 * self.bk
        
        self.b_alpha = (self.alphaN * self.l) / (self.alphaN - self.alpha0)
        self.a_alpha = - self.alpha0 * self.b_alpha


    def k(self, x):
        return self.ak / (x - self.bk)

    def alpha(self, x):
        return self.a_alpha / (x - self.b_alpha)

    def Kappa_plus_half(self, x):
        return (self.k(x)+self.k(x+self.h))/2

    def Kappa_minus_half(self, x):
        return (self.k(x)+self.k(x-self.h))/2

    def p(self, x):
        return 2 * self.alpha(x) / self.R

    def f(self, x):
        return 2 * self.alpha(x) / self.R * self.Te

