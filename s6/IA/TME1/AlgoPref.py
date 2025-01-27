import exemple as ex
import heapq 
import random
import time

def put(heap, value):
    """Ajoute une valeur au tas."""
    heap.append(value)
    moveup(heap, len(heap) - 1)

def pop(heap):
    """Retire et retourne la plus grande valeur du tas."""
    if not heap:
        raise IndexError("Le tas est vide.")
    # Échanger la racine avec le dernier élément
    echange(heap, 0, len(heap) - 1)
    # Retirer la racine
    max_value = heap.pop()
    # Réorganiser le tas
    movedown(heap, 0)
    return max_value

def valracine(heap):
    """Retourne la plus grande valeur sans la retirer."""
    if not heap:
        raise IndexError("Le tas est vide.")
    return heap[0]

def moveup(heap, index):
    """Remonte un élément pour rétablir la propriété de tas."""
    parent_index = (index - 1) // 2
    while index > 0 and heap[index] > heap[parent_index]:
        echange(heap, index, parent_index)
        index = parent_index
        parent_index = (index - 1) // 2

def movedown(heap, index):
    """Descend un élément pour rétablir la propriété de tas."""
    size = len(heap)
    while True:
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < size and heap[left_child] > heap[largest]:
            largest = left_child
        if right_child < size and heap[right_child] > heap[largest]:
            largest = right_child

        if largest == index:
            break
        echange(heap, index, largest)
        index = largest

def echange(heap, i, j):
    """Échange deux éléments dans le tableau."""
    heap[i], heap[j] = heap[j], heap[i]

def prefetu(fichier):
    contenu = ex.lectureFichier(fichier)
    mat = []
    for i in range(1,int(contenu[0])+1):
        #print(contenu[i])
        etui = [int(j) for j in contenu[i][2:]]
        mat.append(etui)
    return mat

def prefspe(fichier):
    contenu = ex.lectureFichier(fichier)
    mat = []
    for i in range(2,len(contenu)):
        #print(contenu[i])
        spei = [int(j) for j in contenu[i][2:]]
        mat.append(spei)

    return mat


""" question 2
1. O(1), structure : file 
2. O(1), structure : liste (prefetu[i])
3. O(1), structure : matrice des positions des etudiants j pour chaque parcours i
4. O(1), structure : tas(la racine est l'étudiant le - préféré)
5. O(log n), structure : opérations listes (append et remove) + màj des positions dans le tas
"""

def gpetu(prefetu, prefspe, capacitespe):

    libres = [i for i in range(len(prefetu))] #liste etudiants libres
    affectes = [[] for i in range(len(prefspe))] #matrice des etudiantsaffectes a chaque parcours 

    #matrice des positions des etudiants j pour chaque parcours i
    pos = [[-1 for _ in range(len(prefetu))] for _ in range(len(prefspe))]
    for i in range(len(prefspe)):
        for j in range(len(prefetu)):
            pos[i][prefspe[i][j]] = j

    #un tas pour chaque parcours avec comme racine l'etudiant le - prefere
    tas = [[] for i in range(len(prefspe))]

    while libres:
        etucourant = libres[0] #1er etudiant de la file
        libres.pop(0) #étudiant supprimé de la file -> le second est en tete de file

        #tant que etucourant a pas proposé à tous les masters
        for specourant in prefetu[etucourant]:

            #si place dispo
            if capacitespe[specourant] != 0:
                capacitespe[specourant] -= 1 
                affectes[specourant].append(etucourant) #affecte etucourant à specourant

                put(tas[specourant], pos[specourant][etucourant])

                break
            else:
                #position de l'etudiant le - prefere de specourant
                pos_etucompare = valracine(tas[specourant])
                etucompare = prefspe[specourant][pos_etucompare] 

                #si etucourant est prefere à etucompare
                if pos[specourant][etucourant] < pos[specourant][etucompare]:
                    affectes[specourant].remove(etucompare) #supprime le - prefere
                    libres.append(etucompare) #rajoute le - prefere aux etudiants libres
                    affectes[specourant].append(etucourant) #affecte etucourant à specourant
                    last = pop(tas[specourant]) #enleve etucompare 
                    put(tas[specourant], pos[specourant][etucourant]) #affecte etucourant
                    break

        prefetu[etucourant].pop(0) #chaque etu propose une UNIQUE fois à chaque parcours

    return affectes

def gpspe(prefetu, prefspe, capacitespe):
    #matrice des positions des parcours j dans le classement des étudiants i
    pos = [[-1 for _ in range(len(prefspe))] for _ in range(len(prefetu))]
    for i in range(len(prefetu)):
        for j in range(len(prefspe)):
            pos[i][prefetu[i][j]] = j

    #liste des parcours sans etudiants
    libres = [i for i in range(len(prefspe))]

    #tableau parcours actuel de chaque etudiant
    paretu = [-1 for i in range(len(prefetu))]

    #matrice des etudiants affectes a chaque parcours 
    affectes = [[] for i in range(len(prefspe))] 

    #tant qu'il existe des étudiants sans parcours
    while libres:
        specourant = libres[0] #premier etudiant de la file
        print(specourant)
        for etucourant in prefspe[specourant]:
            if capacitespe[specourant] > 0: #si capacité pas remplie
                affectes[specourant].append(etucourant)
                capacitespe[specourant] -= 1  #réduire la capacité du parcours
                print(capacitespe[specourant])
                paretu[etucourant] = specourant #specourant devient parocurs de etucourant
                print(etucourant," est affecte dans ", specourant)
                break
            else:
                specompare = paretu[etucourant]

                #si specourant est préféré à specompare
                if pos[etucourant][specourant] < pos[etucourant][specompare]:
                    print(etucourant, " change ", specompare," pour ", specourant)
                    libres.append(specompare) #ajouter specompare à libres

                    #affecter etucourant à specourant
                    paretu[etucourant] = specourant
                    affectes[specourant].append(etucourant)
                    affectes[specompare].remove(etucourant)
                    break
                libres.remove(specourant)
                print(libres)

    return affectes


"""
question 3 : O(n*m*log m)-> boucle while = O(n), m propositions = O(m), 
                            operations sur le tas = O(log n)
question 4 :
chaque parcours propose à chaque étudiant dans son ordre de préférences
si capacite du parcours i est remplie et si le nv etudiant prefere le parcours i à 
son ancien parcours -> l'étudiant - préféré part et le nv etudiant est affecte. 
sinon on ajoute simplement l'etudiant à son parcours prefere valide
même complexité -> O(n*m*log m) 
"""

def paires_instables(prefetu,prefspe,capacitespe,affectes):
    """sq on veut coté etudiant, il va s'agir de comparer les preferences de l'etudiant i
    aux affectations en parametres. 
    si son parcours pref disponible dont la capacite est remplie et dont l'etudiant le - 
    prefere, affecté à ce mm parcours, est - préféré que l'etudiant i -> paire instable
    """
    p = [] #tableau de paires instables

    #matrice des positions des etudiants j pour chaque parcours i
    pos = [[-1 for _ in range(len(prefetu))] for _ in range(len(prefspe))]
    for i in range(len(prefspe)):
        for j in range(len(prefetu)):
            pos[i][prefspe[i][j]] = j

    for specourant in range(len(affectes)):
        for etu in range(len(affectes[specourant])):
            etucourant = affectes[specourant][etu]

            for i in range(len(prefetu[etucourant])):
                spepref = prefetu[etucourant][i]
                if spepref == specourant: #pas une paire instable
                    break  
                else:
                    etucompare = affectes[spepref][0] #etudiant le - préféré pour specourant
                    for j in range(1, len(affectes[spepref])):
                        if pos[spepref][affectes[spepref][j]] > pos[spepref][etucompare]:
                            etucompare = affectes[spepref][j]

                    #si specourant préfère etu à etucompare
                    if pos[spepref][etucourant] < pos[spepref][etucompare]:
                        print(spepref," : ",etucourant," est preféré à ", etucompare)
                        p.append((etucourant, spepref))

    return p

def generate_cE(n,nb_parcours):
    cE=[[] for _ in range(n)]
    for i in range(n):
        for j in range(nb_parcours):
            cE[i]=list(range(0,nb_parcours))
            random.shuffle(cE[i])
    return cE

def generate_cP(n,nb_parcours):
    cP=[[] for _ in range(nb_parcours)]
    for i in range(nb_parcours):
        for j in range(n):
            cP[i]=list(range(0,n))
            random.shuffle(cP[i])
    return cP

dix_tests_master = [0.0 for i in range(10)]
dix_tests_etu = [0.0 for j in range(10)]

for n in range(200,2000,200):
    cE = generate_cE(n,9)
    cP = generate_cP(n,9)
    capacites = [-1 for i in range(9)]
    tot = n
    for i in range(len(capacites)):
        capacites[i] = random.randint(0,tot)
        tot = tot - capacites[i]
        if sum(capacites) < tot & i == len(capacites)-1:
            capacites[i] = tot
    print(capacites)
    list_etu = [i for i in range(n)]
    debut = time.time()
    #affectes = gpspe(cE,cP, capacites)
    fin = time.time()
    print("coté master : ", fin-debut)
    dix_tests_master.append(fin-debut)
    debut = time.time()
    affectes = gpetu(cE,cP, capacites)
    fin = time.time()
    dix_tests_etu.append(fin-debut)
    print("coté etu : ", fin-debut)


contenu = ex.lectureFichier("PrefSpe.txt")
capacite = [int(x) for x in contenu[1][1:]]
print("coté étudiants :",gpetu(prefetu("PrefEtu.txt"),prefspe("PrefSpe.txt"),capacite))

contenu = ex.lectureFichier("PrefSpe.txt")
capacite = [int(x) for x in contenu[1][1:]]
print("cote parcours :",gpspe(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite))

# res = gpetu(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite)
# print(paires_instables(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite, res))
#si on veut changer de cote -> changer res = gpspe en gpetu et inversement