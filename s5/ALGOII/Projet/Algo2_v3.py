import math


"""Solution qui ne recalcule pas plusieurs fois la même valeur"""


def AlgoOptimise(S, K, V):
    """
    Programmation dynamique -> minimiser le nb de bocaux
                            -> peut etre inefficace pr S ou K grand mais envoie TJRS une solution optimale
                            -> Complexité pseudo polynomiale : O(S x K) = 0(2^t x K), t = nb bits de S
    Retourne le nb minimal de bocaux pour atteindre S, ou l'infini sinon
    """
    M = [[math.inf for _ in range(K)] for _ in range(S + 1)] #initialise matrice à l'infini
    
    for s in range(S + 1):  # Pour chaque quantité de 0 à S
        for i in range(K):  
            if i == 0:  #si on peut utiliser que des bocaux de V[0]
                if s % V[0] == 0 : #s divisible par V[0]
                    M[s][i] = s 
                else :
                    M[s][i] = math.inf
            elif s == 0:  #pas de bocal nécessaire
                M[s][i] = 0
            elif V[i] > s: #bocal trop grand -> on garde le même tableau que s,i-1 sans le bocal actuel
                M[s][i] = M[s][i - 1]
            else:  #minimum entre le choix sans bocal et le choix avec bocal
                M[s][i] = min(M[s][i - 1], M[s - V[i]][i] + 1)

    return M #contient toutes les solutions possibles dont l'optimale

def backward(S,K,V) :
    """retourne le tableau de la solution optimale à l'envers""" 

    M=AlgoOptimise(S,K,V) #matrice contenant toutes les solutions
    A = [0 for _ in range(K)]  #nombre de bocaux utilisés
    i = K - 1
    while S > 0 and i >= 0:#tant qu'il reste une quantité s et des types de bocaux à examiner
        if (i > 0) and (M[S][i] == M[S][i - 1]):
            #si s,i et s,i-1 ont le même tableau sv dire qu'on utilise pas le bocal i
            i -= 1  #on passe au bocal suivant
        else:
            #sinon on doit forcément utiliser un bocal i
            A[i] += 1
            S -= V[i] #reduire la quantité de V[i]
    
    return A

def backward2(S,K,V) :
    """retourne la somme des éléments du tableau qui contient la solution optimale à l'envers""" 

    M=AlgoOptimise(S,K,V) #matrice contenant toutes les solutions
    A = [0 for _ in range(K)]  #nombre de bocaux utilisés
    i = K - 1
    while S > 0 and i >= 0:#tant qu'il reste une quantité s et des types de bocaux à examiner
        if (i > 0) and (M[S][i] == M[S][i - 1]):
            #si s,i et s,i-1 ont le même tableau sv dire qu'on utilise pas le bocal i
            i -= 1  #on passe au bocal suivant
        else:
            #sinon on doit forcément utiliser un bocal i
            A[i] += 1
            S -= V[i] #reduire la quantité de V[i]
            
    return sum(A)

print(backward(36,8,[1, 2, 4, 5, 9, 15, 21, 23]))
