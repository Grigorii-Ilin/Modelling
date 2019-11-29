
def get_I(U_c_prev, I_prev, R, L_k, h):
        
    def get_k(add_x, add_y):
        U_x=U_c_prev+add_x
        I_y=I_prev+add_y

        k=h*(U_x-R*I_y)/L_k
        return k

    k1=get_k(0, 0)
    k2=get_k(h/2, h/2*k1)
    k3=get_k(h/2, h/2*k2)
    k4=get_k(h, h*k3)

    delta_I=(k1+2*k2+2*k3+k4)/6
    I= I_prev+delta_I

    return I


def get_U(U_c_prev, I_prev, C_k, h):
        
    def get_k(add_y):
        I_y=I_prev+add_y

        k=h*(-1/C_k)*I_y
        return k

    k1=get_k(0)
    k2=get_k(h/2*k1)
    k3=get_k(h/2*k2)
    k4=get_k(h*k3)

    delta_U=(k1+2*k2+2*k3+k4)/6
    U=U_c_prev +delta_U

    return U

    