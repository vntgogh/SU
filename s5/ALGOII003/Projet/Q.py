import math

def read():
    # Lit les données d'entrée de 'data.txt'
    with open("data.txt", "r") as fichier:
        contenu = fichier.read().split()
        S = int(contenu[0])
        K = int(contenu[1])
        V = [int(val) for val in contenu[2:]] 
    return S, K, V

def m(s, i, V):
    """Calcule le nombre minimal de bocaux nécessaires pour atteindre la quantité s.
    
    - Si s == 0 : la solution est 0 (aucun bocal requis).
    - Si s < 0 : impossible (renvoie `math.inf`).
    - Si i == 0 : on ne peut utiliser que le bocal de capacité minimale V[0].
      -> Si s est un multiple de V[0], on calcule une solution.
      -> Sinon, c'est impossible (`math.inf`).
    - Sinon : calcule la solution minimale avec ou sans le bocal courant.
    """
    if s == 0:
        return 0  # Quantité atteinte, aucun bocal nécessaire
    elif s < 0:
        return math.inf  # Quantité non atteignable
    elif i == 0:  # Si AUCUN AUTRE BOCAl  n'est disponible
        if s % V[0] == 0:  # Si divisible par la capacité minimale
            return m(s - V[i], i, V) + 1  # Ajouter autant de fois V[0] que nécessaire
        else:
            return math.inf 
    else:
        # Cas sans utiliser le bocal actuel
        sans_bocal = m(s, i - 1, V)
        # Cas en utilisant le bocal actuel
        avec_bocal = m(s - V[i], i, V) + 1
        return min(sans_bocal, avec_bocal)  # Retourne le meilleur des deux cas



def m_threading(s, i, V,stop_event):
    if(stop_event.is_set()):
        return 0
    if s == 0:
        return 0  # Pas besoin de bocal supplémentaires
    elif s < 0:
        return math.inf  # Cas impossible
    elif i==0:  # Aucun élément utilisable
        if(s % V[0] == 0):
            return(m_threading(s - V[i],i,V,stop_event)+1)
        else:
            return math.inf
    else:
        # Calculer la solution minimale avec ou sans le bocal courant
        sans_bocal = m_threading(s, i - 1, V,stop_event)
        avec_bocal = m_threading(s - V[i], i, V,stop_event) + 1
        return min(sans_bocal, avec_bocal)


def main():
    S, K, V = read()
    m(S,len(V)-1,V)

def main_threading(stop_event):
    S, K, V = read()
    try:
        m_threading(S, len(V)-1, V,stop_event)
    except RecursionError:
        print("Erreur de recursion")
        while(stop_event.is_set()==False):
            continue
        