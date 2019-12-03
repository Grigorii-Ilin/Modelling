


#idea got from:
#https://vunivere.ru/work4464/page9

def rke(R=0.5,
        L=60e-6,
        C=150e-6,
        IC0=0,
        E=1500.0,
        UC0=0,
        h=300e-06):

    ICs=[]
    UCs=[]
    times=[]

    def get_k_I(IC, UC, add_IC, add_UC):
        UC+=add_UC
        IC+=add_IC
        k=h*(-R*IC+UC)/L
        return k

    def get_k_U(IC, add_IC):
        IC+=add_IC
        k=h*(-IC/C)
        return k

    def get_delta(ks):
        return (ks[0]+2*ks[1]+2*ks[2]+ks[3])/6


    for i in range(2300):
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

        print(times[i], ICs[i], UCs[i])

    return times, ICs, UCs