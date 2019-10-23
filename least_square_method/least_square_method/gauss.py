import numpy as np


def _forward_trace(mas_len, m, v):
    #di: diagonal index
    #fdi: from diagonal index
    #ndi: next diagonal index

    for di in range(mas_len):
        diag = m[di][di]

        for fdi in range(di, mas_len):
            m[di][fdi]/=diag

        v[di]/=diag

        for ndi in range(di + 1, mas_len):
            before_next_diag = m[ndi][di]

            for fdi in range(di, mas_len):
                m[ndi][fdi]-=m[di][fdi] * before_next_diag

            v[ndi]-=v[di] * before_next_diag

    return m, v


def _backward_trace(mas_len, m, v):
    coefs = np.zeros(shape=(mas_len))
    
    coefs[mas_len - 1] = v[mas_len - 1]
    for i in reversed(range(mas_len - 1)):
        accum = 0.0
        for j in range(i + 1, mas_len):
            accum+=m[i][j] * coefs[j]
        coefs[i] = v[i] - accum

    return coefs



def gauss(mas, vec):
    mas_len = mas.shape[0]
    mas, vec = _forward_trace(mas_len, mas, vec)
    coefs = _backward_trace(mas_len, mas, vec)
    return coefs
