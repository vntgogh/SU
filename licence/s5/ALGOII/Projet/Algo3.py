import math

"""renvoie le tableau qui prend toujours la plus grande valeur en premier
   complexité temporelle = O(S x K)
"""
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

"""renvoie la somme des éléments du tableau qui prend toujours la plus grande valeur en premier"""
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


print(AlgoGlouton(36,8,[1, 2, 4, 5, 9, 15, 21, 23]))
