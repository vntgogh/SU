import math

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

    return M  # Résultat optimal pour S avec les K bocaux
    
def backward() :
    with open("data.txt","r") as fichier:
        contenu = fichier.read().split()
        S=int(contenu[0])
        K=int(contenu[1])
        V=[int(val) for val in contenu[2:]]

    M=AlgoOptimise(S,K,V)
    A = [0 for _ in range(K)]  # Tableau pour stocker le nombre de bocaux utilisés
    i = K - 1  # Commencer par le dernier type de bocal
    while S > 0 and i >= 0:
        # Si on utilise le bocal `i` pour atteindre la solution optimale
        if (i > 0) and (M[S][i] == M[S][i - 1]):
            i -= 1  # Passer au type de bocal précédent
        else:
            # Ajouter un bocal de type `i`
            A[i] += 1
            S -= V[i]
    
    return A

def backward2(S,K,V) :
    M=AlgoOptimise(S,K,V)
    A = [0 for _ in range(K)]  # Tableau pour stocker le nombre de bocaux utilisés
    i = K - 1  # Commencer par le dernier type de bocal

    while S > 0 and i >= 0:
        # Si on utilise le bocal `i` pour atteindre la solution optimale
        if (i > 0) and (M[S][i] == M[S][i - 1]):
            i -= 1  # Passer au type de bocal précédent
        else:
            # Ajouter un bocal de type `i`
            A[i] += 1
            S -= V[i]
    
    return A

print(backward2(36,8,[1, 2, 4, 5, 9, 15, 21, 23]))