
T= [454,8,42,184,2,58,415,28]
def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] =T[j+1]
                T[j+1] = temp
    print(T)