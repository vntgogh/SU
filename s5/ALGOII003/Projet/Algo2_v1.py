import math

def AlgoOptimise(S, K, V):
    """
    Programmation dynamique -> minimiser le nb de bocaux
                            -> peut etre inefficace pr S ou K grand mais envoie TJRS une solution optimale
                            -> Complexité pseudo polynomiale : O(S x K) = 0(2^t x K), t = nb bits de S
    Retourne le nb minimal de bocaux pour atteindre S, ou l'infini sinon
    """
    # Initialiser la matrice
    M = [[math.inf for _ in range(K)] for _ in range(S + 1)]
    
    # Remplir les valeurs de la matrice
    for s in range(S + 1):  # Pour chaque quantité de 0 à S
        for i in range(K):  # Pour chaque type de bocal
            if i == 0:  #Si on utilise que des bocaux de type V[0]
                if s % V[0] == 0 :
                    M[s][i] = s 
                else :
                    M[s][i] = math.inf
            elif s == 0:  # Si la quantité est nulle
                M[s][i] = 0
            elif V[i] > s: #Si la capacité du bocal est trop grande
                M[s][i] = M[s][i - 1]
            else:  # Sinon, calculer le minimum
                M[s][i] = min(M[s][i - 1], M[s - V[i]][i] + 1)

    return M[S][K - 1]  # Résultat optimal pour S avec les K bocaux
    
print(AlgoOptimise(36,8,[1, 2, 4, 5, 9, 15, 21, 23]))