import math
import copy

"""Solution qui ne recalcule pas plusieurs fois la même valeur et mets les tableaux des sous solutions 
optimales du probleme dans la matrice"""

def AlgoOptimise(S,K,V) :
    """ (solution optimale )
    Retourne un tableau A où chaque A[i] contient le nombre de bocaux de capacité i utilisés
    """
    A = [0 for _ in range (K)] #initialise le tableau de chaque case
    T=[math.inf for _ in range (K)] 
    M = [[T for _ in range(K)] for _ in range(S+1)] #initialise les cases à l'infini
    for s in range(S+1): #parcourt les quantités de 0 à S
        for i in range(K): #V
            if i == 0 : #si on peut utiliser que le plus petit bocal
                if(s % V[i]==0): #s divisible par V[0](sq V[0]!=1)
                    M[s][i][i]+=1 
                else:
                    M[s][i][i]=math.inf #impossible d'atteindre s même avec 0 V[0]
            if s == 0 :
                M[s][0] = A #s=0 -> pas de bocaux nécessaires
            if V[i] > s : #si bocal trop grand -> passer au suivant en gardant le même tableau
                M[s][i]=M[s][i-1] 
            else :
                #calculer le coût des deux options -> avec ou sans le bocal actuel
                c=min(sum(M[s][i-1]),sum(M[s-V[i]][i])+1) #et on fait la somme des bocaux utilisés et on prend le minimum
                if c==sum(M[s][i-1]):  
                    M[s][i]=M[s][i-1]#on copie le tableau de s,i-1 sans le bocal actuel
                else: 
                    A2 = copy.deepcopy(M[s-V[i]][i]) # on copie le tableau pour ne pas le modifier
                    A2[i]+=1 #on itere le nb de bocaux du type actuel
                    M[s][i]=A2 #notre tableau courant devient le tableau A2
    return M[S][K-1]

    
print(AlgoOptimise(5,2,[1, 3, 4, 5, 9, 15, 21, 23]))