import exemple as ex
from copy import deepcopy
import random
import queue
import time




""" question 2
1. O(1), structure : file (UTILISER QUEUE)
2. O(1), structure : tableau de mise a jour du suivi des demandes
3. O(1), structure : matrice des positions des etudiants j pour chaque parcours i
4. O(1), structure : tas(la racine est l'étudiant le - préféré)
5. O(1.log(n)), structure : opérations des listes (append et remove) O(1) (négligable) et Mise a jour du tas en O(log(n))
"""

""" question 4
1. O(1), structure : file (UTILISER QUEUE)
2. O(1), structure : liste (prefetu[i])
3. O(1), structure : matrice des positions des etudiants j pour chaque parcours i
4. O(1), structure : tableau de positions
5. O(1.log(n)), structure : opérations des listes (append et remove) O(1) (négligable) et Mise a jour du tas en O(log(n))
"""

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
    movedown(heap, 0) #Le dernier élement est en haut du tas on doit le ramener en bas
    return max_value

def valracine(heap):
    """Retourne la plus grande valeur sans la retirer."""
    if not heap:
        raise IndexError("Le tas est vide.")
    return heap[0]

def moveup(heap, index):
    """Remonte un élément pour rétablir la propriété de tas."""
    parent_index = (index - 1) // 2
    while index > 0 and heap[index] > heap[parent_index]: # Tant que le fils est plus grand que le parent on monte le fils
        echange(heap, index, parent_index)
        index = parent_index
        parent_index = (index - 1) // 2

def movedown(heap, index):
    """Descend un élément pour rétablir la propriété de tas."""
    size = len(heap)
    while True: #Tant que le fils gauche ou le fils droit est plus grand que la valeur courante on fait descendre la valeur courant dans le tas
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


def studentpref(file):
    content = ex.lectureFichier(file)
    #print((int)(content[0][0]))
    cE= [[0]*9 for i in range ((int)(content[0][0]))]
    #print(cE)
    i=0
    for k in range(1,len(content)):
        #print(content[k])
        w=2
        for j in range (9):
            #print(content[k][w])
            cE[i][j]=content[k][w]
            w+=1
        i+=1
    #print (content)
    #print(cE)
    return cE


def masterpref(file):
    content = ex.lectureFichier(file)
    cP= [[0]*(int)(content[0][1]) for i in range (9)]
    i=0
    for k in range (2,len(content)):
        w=2
        for j in range((int)(content[0][1])):
            cP[i][j]=content[k][w]
            w+=1
        i+=1
    #print (cP)
    return cP


def capacity_master(file):
    content = ex.lectureFichier(file)
    content[1].remove("Cap")
    return(content[1])


def GS_etu(cE,cP,capacity):
    #Initialisation des des étudiants et Master commme libre, pour chaque master un tas représentant les éleves du moins préferer au plus préferer
    # et une liste pour chaque master avec la position dans le master de chaque éleve i a sont indice i en O(1)
    # La recherche des préferences du master se fera dans le tas et on utilisera le tableau de verification en O(1)
    #Retourne pour un tableau qui contient pour le i-eme étudiant sont parcours assigné

    #Initialisation de la liste des etudiants
    list_etu=[i for i in range (len(cE))]

    #Initialisation matrice des positions des étudiants dans chaque master
    tabPref=deepcopy(cP)
    for i in range(len(cP)):
        for j in range(len(cP[0])):
            tabPref[i][(int)(cP[i][j])]=(int)(j)

    #print("Tab pref : ",tabPref)

    #Initialisation des tas du pire eleve dans chaque master
    tas = [[] for _ in range(len(cP))]

    #Tableau d'affectation pour le i-eme étudiant
    affectation=[[] for _ in range (len(cP))]

    #Initialisation de la Queue 
    q = queue.Queue(len(list_etu))
    for etu in list_etu:
        q.put((int)(etu))

    #Initialisation du tableau de suivi
    suivi=[0 for i in range (len(list_etu))]
    
    while(not q.empty()):
        etu_courant=q.get()
        while(len(cE[etu_courant])!=0):
            #print(cE[etu_courant],list_etu[0])
            #print(tas)
            
            ask=(int)(cE[etu_courant][suivi[etu_courant]])
            #Si il y a de la place on affecte le premier étudiant de la liste a sont i eme choix 
            if ((int)(capacity[ask])>0):
                #fichier.write(f"Tas courant : {tas[ask]} Etudiant courant : {list_etu[0]} Master courant : {ask}\n")
                #breakpoint()
                #print(i,cE[etu_courant],(int)(tabPref[ask][etu_courant]))
                affectation[ask].append(etu_courant)
                put(tas[ask],(int)(tabPref[ask][etu_courant]))
                capacity[ask]=(int)(capacity[ask])-1
                suivi[etu_courant]+=1
                #print("L'etudiant ",list_etu[0]," a ete pop et a été mis dans le master ", ask)
                #fichier.write(f"Tas courant : {tas[ask]} Etudiant courant : {list_etu[0]} Master courant : {ask}\n")
                #breakpoint()\
                break
            
            #Sinon on doit comparer le dernier etudiant dans la liste du master (sont moins préferer)
            else:
                #print("dans else")
                pos_last_etu=valracine(tas[ask])
                
                last_etu=cP[ask][pos_last_etu]
                #print(len(list_etu))
                #fichier.write(pos_last_etu,tabPref[ask][etu_courant])
                if tas[ask]:
                    #Si le nouvel étudiant a une meilleure position (pris dans la tableau de verification) que l'etudiant pris dans le tas alors on le remplace.
                    if(tabPref[ask][etu_courant]<pos_last_etu):
                        #fichier.write(f"Tas courant : {tas[ask]} Master courant : {ask} Etudiant courant : {list_etu[0]} Pire etudiant : {last_etu}\n")
                        #breakpoint()
                        #print("on choisis l'etu : ",list_etu[0]," a la place de ",last_etu,"pour le master : ", ask)
                        pop(tas[ask])
                        put(tas[ask],tabPref[ask][etu_courant])
                        
                        affectation[ask].append(etu_courant)
                        affectation[ask].remove((int)(last_etu))
                        #on ajoute dans le tas le nouvel étudiant et on remet l'etudiant déjà choisis dans la liste_etu
                        suivi[etu_courant]+=1
                        
                        q.put((int)(last_etu))
                        #fichier.write(f"Tas courant : {tas[ask]} Master courant : {ask} Etudiant courant : {list_etu[0]} Pire etudiant : {last_etu}\n")

                        #breakpoint()
                        break
                    else:
                        suivi[etu_courant]+=1
                        continue

    return affectation



def GS_master(cE,cP,capacity,list_master):

    """Tant qu'il existe un Master libre qui n'a pas proposer a tout les étudiants, il choisis le premier étudiant E
        dans sa liste, si le master n'a pas atteint sa capacite max et que l'étudiant est dans aucun master 
        alors on prend l'etudiant E. Sinon on doit comparer si l'etudiant prefere sont master actuelle ou le master qui propose.
        Si il prefere le master courant on remplace le pire master de l'étudiant par le master courant. Sinon E reste dans son master

    """
    #Initialisation matrice des preferences des etudiants pour chaque master
    tabPref=deepcopy(cE)
    for i in range(len(cE)):
        for j in range(len(cE[0])):
            tabPref[i][(int)(cE[i][j])]=(int)(j)


    #Initialisation d'une liste des master actuelle pour chaque eleve
    eleve_affect = [-1 for _ in range(len(cE))]

    #Tableau d'affectation pour le i-eme master
    affectation=[[] for _ in range (len(cP))]

        #Initialisation de la Queue 
    q = queue.Queue(len(list_master))
    for etu in list_etu:
        q.put((int)(etu))

    #Initialisation du tableau de suivi
    suivi=[0 for i in range (len(list_etu))]
    
    while(list_master):
        #print("Affectation des eleves : ",eleve_affect)
        while((int)(capacity[list_master[0]])>0):
            #print("Liste de preferences du master : ",list_master[0]," ",cP[list_master[0]])
            #Si l'eleve est affecter a aucun master on l'affecte au master courant et on retire l'eleve des eleve parcouru
            if((int)(eleve_affect[(int)((int)(cP[list_master[0]][0]))])==-1):
                #print("affectation : ",affectation,"Master : ",list_master[0])
                eleve_affect[(int)(cP[list_master[0]][0])]=list_master[0] #l'eleve est affecter au master list_master[0]
                
                #affectation[list_master[0]].append((int)(cP[list_master[0]][0])) #le master rajoute  l'eleve dans sa liste d'affecter
    
                affectation[list_master[0]].append((int)(cP[list_master[0]][0]))

                cP[list_master[0]].pop(0) #on retire l'eleve de la liste des eleves disponible du master
                #print("Anciene capacite du master : ",list_master[0], " ", capacity[list_master[0]])
                capacity[list_master[0]]=(int)(capacity[list_master[0]])-1
                #print("Nouvelle Capacite : ", capacity[list_master[0]])#," Master : ",list_master[0])
            else:
                #print("affectation : ",affectation,"Master courant : ",list_master[0],"Ancience master : ",eleve_affect[(int)(cP[list_master[0]][0])])
                #on compare le master de l'etudiant actuelle avec celui courant et l'etudiant refuse ou non le master courant
                post_actual_master=tabPref[(int)(cP[list_master[0]][0])][list_master[0]]
                pos_last_master=tabPref[(int)(cP[list_master[0]][0])][eleve_affect[(int)(cP[list_master[0]][0])]]
                ancienmaster=eleve_affect[(int)(cP[list_master[0]][0])]
                #print(ancienmaster)
                
                if(post_actual_master<pos_last_master):

                    #le master courant est accepter
                    eleve_affect[(int)(cP[list_master[0]][0])]=list_master[0] #l'eleve est affecter au master courant
                    capacity[list_master[0]]=(int)(capacity[list_master[0]])-1 #on retire la capacite au master courant
                    affectation[list_master[0]].append((int)(cP[list_master[0]][0])) # on ajoute a la liste d'affectation du master courant l'etudiant 

                    #affectation[(int)(cP[list_master[0]][0])]=[(int)(cP[list_master[0]][0]),(int)(list_master[0])]
                    
                    capacity[ancienmaster]=(int)(capacity[ancienmaster])+1 # on remets de la capacite a l'ancien master
                    list_master.append(ancienmaster)#on ajoute l'ancien master aux master a visiter

                    affectation[ancienmaster].remove((int)(cP[list_master[0]][0])) #on retire de la liste d'affectation l'eleve qui part
                    #print("Anciene capacite du master : ",list_master[0], " ", capacity[list_master[0]])
                    cP[list_master[0]].pop(0)
                    #print("Capacite : ", capacity[list_master[0]]," Master : ",list_master[0])
                    #print("Nouvelle Capacite : ", capacity[list_master[0]])#," Master : ",list_master[0])
                else:
                    cP[list_master[0]].pop(0) #L'etudiant rejette la proposition du master donc on le retire de la liste du master
                    #le master courant est refusé
        list_master.pop(0)
    
    return affectation



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
            pos[i][(int)(prefspe[i][j])] = j

    for specourant in range(len(affectes)):
        for etu in range(len(affectes[specourant])):
            etucourant = (int)(affectes[(int)(specourant)][(int)(etu)])

            for i in range(len(prefetu[etucourant])):
                spepref = (int)(prefetu[etucourant][i])
                if spepref == specourant: #pas une paire instable
                    break  

                #si place dispo dans spepref ->  paire instable
                #if len(affectes) < capacitespe[spepref]: 
                    #p.append((etucourant, spepref))
                    #print(etucourant,"-",spepref,"il restait de la place")
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

for n in range(200,2200,200):
    cE = generate_cE(n,9)
    cP = generate_cP(n,9)

    capacites = [random.randint(1, n//2) for _ in range(9)] #capacites entre 1 et n/2 pour equité
    while sum(capacites) != n:
        diff = n-sum(capacites)
        if diff > 0: #on met diff dans une capacite random
            capacites[random.randint(0, 8)] += diff
        if diff < 0: #si sum(capacites) > n
            #on ajt diff(negatif) à une capacite random
            ind = random.randint(0, 8)
            capacites[ind] = max(1, capacites[ind] + diff) #max entre 1 pr eviter les res negatifs
   
    print(capacites)

    list_etu = [i for i in range(n)]
    debut = time.time()
    affectes = GS_master(cE,cP, capacites,list_etu)
    fin = time.time()
    print("coté master : ", fin-debut)
    dix_tests_master.append(fin-debut)
    debut = time.time()
    affectes = GS_etu(cE,cP, capacites)
    fin = time.time()
    dix_tests_etu.append(fin-debut)
    print("coté etu : ", fin-debut)

print("moyenne temps parcours = ", sum(dix_tests_master) / len(dix_tests_master)," secondes")
print("moyenne etu = ", sum(dix_tests_etu) / len(dix_tests_etu)," secondes")

affect_etu_optimal = GS_etu(studentpref("PrefEtu.txt"),masterpref("PrefSpe.txt"),capacity_master("PrefSpe.txt"),[0,1,2,3,4,5,6,7,8,9,10])
affect_master_optimal = GS_master(studentpref("PrefEtu.txt"),masterpref("PrefSpe.txt"),capacity_master("PrefSpe.txt"),[0,1,2,3,4,5,6,7,8])


#print("Affectation master optimal : ",affect_master_optimal)
print("Affectation Etudiant optimal : ",affect_etu_optimal)
#print ("Paire instable : ",paires_instables(studentpref("PrefEtu.txt"),masterpref("PrefSpe.txt"),capacity_master("PrefSpe.txt"),affect_etu_optimal))

#print("Creation cE :  ",generate_cE(10,9))
#print("Creation cP : ",generate_cP(10,9))


#studentpref("PrefEtu.txt")
#print(masterpref("PrefSpe.txt"))

