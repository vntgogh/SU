import math


def AlgoGlouton(S,K,V):
    A = [0 for _ in range(K)]
    i=K-1
    while(i>=0):
        while(S>=V[i]):
            #print(S,V[i])
            A[i]+=1
            S-=V[i]
        i-=1
    return A

def AlgoGlouton2(S,K,V):
    A = [0 for _ in range(K)]
    i=K-1
    while(i>=0):
        while(S>=V[i]):
            #print(S,V[i])
            A[i]+=1
            S-=V[i]
        i-=1
    return sum(A)



