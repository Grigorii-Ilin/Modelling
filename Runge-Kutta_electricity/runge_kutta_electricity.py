import numpy as np 

import calc

R=0.5
L_k=60e-6
C_k=150e-6
U_0=1500.0
I_0=0.0

I_old=I_0
U_old=U_0
for i in range(20):
    I_cur=calc.get_I(U_c_prev=U_old, I_prev=I_old, R=R, L_k=L_k, h=1)
    U_cur=calc.get_U(U_c_prev=U_old, I_prev=I_old, C_k=C_k, h=1)

    print(i, I_cur, U_cur)

    I_old=I_cur
    U_old=U_old
    
