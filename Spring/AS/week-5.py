import numpy as np

def init_function(x, k, b):
    return k*x+b

def data_set(n):
    data_y = []
    for i in range(0, n):
        a = init_function(i*0.1, 3, 6)
        data_y.append((i*0.1, a))
    return data_y
def G(k0,b0,x,y, alpha=0.01):

    k = k0 - alpha*2(k0*x+b0-y)
    b = b0 - alpha*2(k0*x+b0-y)
    return (k, b)



mat = data_set(200)
print(mat)

for i in range(200):
    print(G(mat[0][0],mat[0][1],))

