import math


""""AlgoOptimise(S,K,V) - Retourne le nombre optimal de bocaux minimaux a utlisé dans V de taille k pour atteindre la quantité s. 
    Solution qui ne recalcule pas plusieurs fois la même valeur"""

def AlgoOptimise(S, K, V):
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