import math

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

    return M[S][K - 1] #retourne uniquement la solution optimale
    
print(AlgoOptimise(36,8,[1, 2, 4, 5, 9, 15, 21, 23]))