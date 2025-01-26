import exemple as ex
import heapq 

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
5. O(1), structure : opérations des listes (append et remove)
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

                #heappush trie automatiquement les etudiants par preference de specourant
                heapq.heappush(tas[specourant], etucourant)

                break
            else:
                #etudiant moins prefere de specourant
                etucompare = tas[specourant][0]

                #si etucourant est prefere à etucompare
                if pos[specourant][etucourant] < pos[specourant][etucompare]:
                    affectes[specourant].remove(etucompare) #supprime le - prefere
                    libres.append(etucompare) #rajoute le - prefere aux etudiants libres
                    affectes[specourant].append(etucourant) #affecte etucourant à specourant
                    heapq.heapreplace(tas[specourant], etucourant) #enleve le - prefere et ajoute etucourant
                    break

        prefetu[etucourant].pop(0) #chaque etu propose une UNIQUE fois à chaque parcours

    return affectes

def gpspe(prefetu, prefspe, capacitespe):
    #matrice des positions des parcours dans le classement des étudiants
    pos = [[-1 for _ in range(len(prefspe))] for _ in range(len(prefetu))]
    for i in range(len(prefetu)):
        for j in range(len(prefspe)):
            pos[i][prefetu[i][j]] = j

    #tableau qui attribue un parcours à chaque étudiant 
    paretu = [-1 for _ in range(len(prefetu))]

    #liste des étudiants sans parcours
    libres = [i for i in range(len(prefetu))]

    #un tas pour chaque parcours avec comme racine l'etudiant le - prefere
    tas = [[] for i in range(len(prefspe))]

    #tant qu'il existe des étudiants sans parcours
    while libres:
        etucourant = libres[0] #premier etudiant de la file
        libres.pop(0) 

        for specourant in prefetu[etucourant]:
            if capacitespe[specourant] > 0: #si capacité pas remplie
                paretu[etucourant] = specourant  #affecter l'étudiant au parcours
                capacitespe[specourant] -= 1  #réduire la capacité du parcours

                #heappush trie automatiquement les etudiants par preference de specourant
                heapq.heappush(tas[specourant], etucourant)

                break
            else:
                #trouver l'étudiant le moins préféré affecté au parcours actuel
                etucompare = tas[specourant][0]

                #si etucourant est préféré à etucompare
                if pos[etucourant][specourant] < pos[etucompare][specourant]:
                    #enlever le parcours de etucompare
                    paretu[etucompare] = -1
                    libres.append(etucompare) #ajouter etucompare à libres

                    #enleve le - prefere et ajoute etucourant
                    heapq.heapreplace(tas[specourant], etucourant) 

                    #affecter etucourant à specourant
                    paretu[etucourant] = specourant
                    break

    affectes = [[] for _ in range(len(prefspe))]
    for etudiant, parcours in enumerate(paretu):
        if parcours != -1:
            affectes[parcours].append(etudiant)

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
    aux affectations en parametres. si l'etudiant n'a pas ete ajt a son parcours pref
    dont la capacité n'est pas remplie -> paire instable
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

                #si place dispo dans spepref ->  paire instable
                if len(affectes) < capacitespe[spepref]: 
                    p.append((etucourant, spepref))
                    print(etucourant,"-",spepref,"il restait de la place")
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

contenu = ex.lectureFichier("PrefSpe.txt")
capacite = [int(x) for x in contenu[1][1:]]
#print("coté étudiants :",gpetu(prefetu("PrefEtu.txt"),prefspe("PrefSpe.txt"),capacite))

contenu = ex.lectureFichier("PrefSpe.txt")
capacite = [int(x) for x in contenu[1][1:]]
#print("cote parcours :",gpspe(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite))
res = gpetu(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite)
print(paires_instables(prefetu("PrefEtu.txt"), prefspe("PrefSpe.txt"), capacite, res))
#si on veut changer de cote -> changer res = gpspe en gpetu et inversement