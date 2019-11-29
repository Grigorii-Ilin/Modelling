


def get_I(U_c_prev, I_prev, R, L_k, h):

        
    def get_k(add_U, add_I):
        U_x=U_c_prev+add_U
        I_y=I_prev+add_I

        k=h*(U_x-R*I_y)/L_k
        return k

    # def get_k1():
    #     k1=(U_c_prev-R*I_prev)/L_k
    #     k1=h*k1
    #     return k1

    # def get_k2():
        
    

    k1=get_k(0, 0)
    k2=get_k(h/2, h/2*k1)
    k3=get_k(h/2, h/2*k2)
    k4=get_k(h, h*k3)

    delta_I=(k1+2*k2+2*k3+k4)/6

    I= I_prev+delta_I
    return I