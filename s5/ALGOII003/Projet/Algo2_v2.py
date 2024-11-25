import math
import copy



""""AlgoOptimise(S,K,V) - Retourne le nombre optimal de bocaux minimaux a utlisé dans V de taille k pour atteindre la quantité s. 
    Solution qui ne recalcule pas plusieurs fois la même valeur et mets les tableau des sous solutions opitmal du problemes dans la matrices"""

def AlgoOptimise(S,K,V) :
    A = [0 for _ in range (K)]
    T=[math.inf for _ in range (K)]
    M = [[T for _ in range(K)] for _ in range(S+1)]
    for s in range(S+1):
        for i in range(K):
            if i == 0 :
                if(s % V[i]==0):
                    M[s][i][i]+=1
                else:
                    M[s][i][i]=math.inf
                M[0][i] = A
            if s == 0 :
                M[s][0] = A
            if V[i] > s : 
                M[s][i]=M[s][i-1]
            else :
                c=min(sum(M[s][i-1]),sum(M[s-V[i]][i])+1) #on fait la somme des bocaux et on prend le minimum
                if c==sum(M[s][i-1]): #si notre minimum est M[s][i-1] alors notre tableau actuelle deviens le tableau contenu dans s,i-1 
                    M[s][i]=M[s][i-1]
                else: 
                    A2 = copy.deepcopy(M[s-V[i]][i]) # on copie le tableau contenu dans M[s-V[i]][i] pour ne pas le modifier
                    A2[i]+=1 # on itere le bocal i
                    M[s][i]=A2 #notre tableau courant devient le tableau A2
    return M[S][K-1]

    
print(AlgoOptimise(5,2,[1, 3, 4, 5, 9, 15, 21, 23]))