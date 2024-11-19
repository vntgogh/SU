import math

def AlgoGlouton():
    with open("data.txt","r") as fichier:
        contenu = fichier.read().split()
        S=int(contenu[0])
        K=int(contenu[1])
        V=[int(val) for val in contenu[2:]]

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