import numpy as np 

import calc

#idea got from:
#https://vunivere.ru/work4464/page9


R=0.5
L=60e-6
C=150e-6
IC0=0
E=1500.0
#UR=0
UC0=0
#UL=E
h=300e-06

ICs=[]
UCs=[]
times=[]

def get_k_I(IC, UC, add_IC, add_UC):
    UC+=add_UC
    IC+=add_IC
    k=h*(E-R*IC-UC)/L/1000
    return k

def get_k_U(IC, add_IC):
    IC+=add_IC
    k=h*IC/C
    return k

def get_delta(ks):
    return (ks[0]+2*ks[1]+2*ks[2]+ks[3])/6


for i in range(100):
    #time_cur=i*h
    #UL=L*(ICs[i]-ICs[i-1])/h if i!=0 else E
    times.append(i*h)

    if i==0:
        ICs.append(IC0)
        UCs.append(UC0)
    else:
        IC=ICs[i-1]
        UC=UCs[i-1]

        ku=[]
        ki=[]

        ku.append(get_k_U(IC, 0))
        ki.append(get_k_I(IC, UC, 0, 0))
        
        ku.append(get_k_U(IC, h/2*ki[-1]))
        ki.append(get_k_I(IC, UC, h/2*ki[-1], h/2*ku[-1]))
     
        ku.append(get_k_U(IC, h/2*ki[-1]))
        ki.append(get_k_I(IC, UC, h/2*ki[-1], h/2*ku[-1]))
      
        ku.append(get_k_U(IC, h*ki[-1]))
        ki.append(get_k_I(IC, UC, h*ki[-1], h*ku[-1]))

        ICs.append(IC+get_delta(ki))
        UCs.append(UC+get_delta(ku))


        # ICs.append(calc.get_I(U_c_prev=UCs[i-1], 
        #                     I_prev=ICs[i-1], 
        #                     R=R, 
        #                     L_k=L, 
        #                     h=h)
        #                     )

        # UCs.append(calc.get_U(U_c_prev=UCs[i-1], 
        #                     I_prev=ICs[i-1],
        #                     C_k=C, 
        #                     h=h)
        #                     )

    print(times[i], ICs[i], UCs[i])




    # I_cur=calc.get_I(U_c_prev=U_old, I_prev=I_old, R=R, L_k=L_k, h=h)
    # U_cur=calc.get_U(U_c_prev=U_old, I_prev=I_old, C_k=C_k, h=h)

    # print(time_cur, I_cur, U_cur)

    # I_old=I_cur
    # U_old=U_old
    
