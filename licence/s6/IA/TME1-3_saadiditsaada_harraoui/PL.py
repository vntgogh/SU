#!/usr/bin/env python3.11
import gurobipy as gp
from gurobipy import GRB

def PL_resolve_1(k,cE,cP,capacity):
    """Les etudiants auront leurs k premiers choix"""
    try:
        n=len(cE) #nombre etudiant
        d=len(cP) #nombre de parcours
        
    
        # Creation du modèle
        m = gp.Model("AllocationEtudiant_1")

        # Variables de décision : x_ij = 1 si étudiant i est assigné à parcours j
        x = m.addVars(n,d,vtype=GRB.BINARY, name="x")
        

        # Fonction objective : maximiser le nombre d'affectations 
        m.setObjective(gp.quicksum(x[i,j] for (i,j) in x), GRB.MAXIMIZE)

        # Contrainte 1 : Chaque étudiant est assigné a au plus 1 parcours
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in range(d))<=1,f"assigne_{i}")

        #Contrainte 2 : Respect des capacités des parcours
        for j in range(d):
            m.addConstr(gp.quicksum(x[i,j] for i in range(n))<=(int)(capacity[j]),f"capacite_{j}")

        #Contrainte 3 : Chaque etudiant doit être assigné a un de ses k premieres préférences
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in ([(int)(valeur) for valeur in cE[i][:k]]))==1,f"preference_{i}")
        
        #ecriture dans un fichier lp
        m.write("AllocationEtudiant_1.lp")
        # Optimize model
        m.optimize()
        affectations={}
        kpref={}
        with open("AllocationEtudiant_1.sol","w") as f:
            if m.status == GRB.OPTIMAL:
                f.write("Solution trouvée :\n")
                for i in range(n):
                    for j in range(d):
                        if x[i, j].x == 1:
                            f.write(f"Étudiant {i} affecté au parcours {j}\n")
                            affectations[i]=j
                f.close()
                for etu,parcours in affectations.items():
                    kpref[etu]=cE[etu].index((str)(parcours)) #etudiant a eu sont k-ieme preferer

        return affectations,kpref 

    except gp.GurobiError as e:
        print(f"Error code {e.errno}: {e}")

    except AttributeError:
        print("Encountered an attribute error")

def PL_resolve_2(k,cE,cP,capacity):
    """Les etudiants auront leurs k premiers choix , on maximise l'utilite minimal, on cherche donc l'équite."""
    try:
        n=len(cE) #nombre etudiant
        d=len(cP) #nombre de parcours
        
        # Creation du modele
        m = gp.Model("AllocationEtudiant_2")

        # Variables de décision : x_ij = 1 si étudiant i est assigné à parcours j
        x = m.addVars(n,d,vtype=GRB.BINARY, name="x")

        #Variable pour l'utilité minimal
        uti_min = m.addVar(vtype=GRB.INTEGER,name="uti_min")

        #Utilité des étudiants (score de Borda)
        uti_etu= {}
        for i in range(n):
            uti_etu[i]={(int)(parcours): d-index-1 for index,parcours in enumerate(cE[i])}

        # Fonction objective : maximiser l'utilite minimal
        m.setObjective(uti_min, GRB.MAXIMIZE)

        # Contrainte 1 : Chaque étudiant est assigné a au plus 1 parcours
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in range(d))==1,f"assigne_{i}")

        #Contrainte 2 : Respect des capacités des parcours
        for j in range(d):
            m.addConstr(gp.quicksum(x[i,j] for i in range(n))==(int)(capacity[j]),f"capacite_{j}")

        #Contrainte 3 : Chaque etudiant doit être assigné a un de ses k premieres préférences
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in ([(int)(valeur) for valeur in cE[i][:k]]))==1,f"preference_{i}")
        
        #Contrainte 4 : Maximiser le min
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j]*uti_etu[i][j] for j in range(d))>= uti_min,f"umin_{i}")


        #ecriture dans un fichier lp
        m.write("AllocationEtudiant_2.lp")
        # Optimize model
        m.optimize()

        affectations={}
        kpref={}
        with open("AllocationEtudiant_2.sol","w") as f:
            if m.status == GRB.OPTIMAL:
                f.write("Solution trouvée :\n")
                for i in range(n):
                    for j in range(d):
                        if x[i, j].x == 1:
                            f.write(f"Étudiant {i} affecté au parcours {j}\n")
                            affectations[i]=j
                f.write(f"Utilite minimal : {uti_min.X}")
                for etu,parcours in affectations.items():
                    kpref[etu]=cE[etu].index((str)(parcours)) #etudiant a eu sont k-ieme preferer
            f.close()

    except gp.GurobiError as e:
        print(f"Error code {e.errno}: {e}")

    except AttributeError:
        print("Encountered an attribute error")

    return affectations,kpref,uti_min.X

def PL_resolve_3(cE,cP,capacity):
    """On maximise la somme des utilite (efficacite)"""
    try:
        n=len(cE) #nombre etudiant
        d=len(cP) #nombre de parcours
        
    
        # Creation du modele
        m = gp.Model("AllocationEtudiant_3")

        # Variables de décision : x_ij = 1 si étudiant i est assigné à parcours j
        x = m.addVars(n,d,vtype=GRB.BINARY, name="x")


        #Utilité des étudiants (score de Borda)
        uti_etu= {}
        for i in range(n):
            uti_etu[i]={(int)(parcours): d-index-1 for index,parcours in enumerate(cE[i])}

        #utilite des parcours (scorede borda)
        uti_spe= {}
        for j in range(d):
            uti_spe[j]={(int)(etu) : n-index-1 for index,etu in enumerate(cP[j])}

        # Fonction objective : maximiser la somme des utilite
        m.setObjective(gp.quicksum(x[i,j]*uti_etu[i][j] + x[i,j]*uti_spe[j][i] for i in range(n) for j in range(d)), GRB.MAXIMIZE)

        # Contrainte 1 : Chaque étudiant est assigné a au plus 1 parcours
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in range(d))==1,f"assigne_{i}")

        #Contrainte 2 : Respect des capacités des parcours
        for j in range(d):
            m.addConstr(gp.quicksum(x[i,j] for i in range(n))==(int)(capacity[j]),f"capacite_{j}")
        

        #ecriture dans un fichier lp
        m.write("AllocationEtudiant_3.lp")
        # Optimize model
        m.optimize()

        uti_res_etu=[]

        affectations={}
        with open("AllocationEtudiant_3.sol","w") as f:
            if m.status == GRB.OPTIMAL:
                f.write("Solution trouvée :\n")
                for i in range(n):
                    for j in range(d):
                        if x[i, j].x == 1:
                            f.write(f"Étudiant {i} affecté au parcours {j}\n")
                            uti_res_etu.append(uti_etu[i][j])
                            affectations[i]=j
                f.write(f"Utilite maximal : {m.ObjVal}\n")
                f.write(f"Utilite moyenne total :  {m.ObjVal/(n)}\n") #On divise par n car il y a n affectations 
                f.write(f"Utilite minimal etudiant : {min(uti_res_etu)}" )
            f.close()
        return affectations,m.ObjVal,m.ObjVal/(n),min(uti_res_etu)

    except gp.GurobiError as e:
        print(f"Error code {e.errno}: {e}")

    except AttributeError:
        print("Encountered an attribute error")
    
    return affectations,0,0,0
def PL_resolve_4(k,cE,cP,capacity):
    """Les etudiants auront leurs k premiers choix et on maxmise la somme des utilites"""
    try:
        n=len(cE) #nombre etudiant
        d=len(cP) #nombre de parcours
        
    
        # Creation du modele
        m = gp.Model("AllocationEtudiant_4")

        # Variables de décision : x_ij = 1 si étudiant i est assigné à parcours j
        x = m.addVars(n,d,vtype=GRB.BINARY, name="x")


        #Utilité des étudiants (score de Borda)
        uti_etu= {}
        for i in range(n):
            uti_etu[i]={(int)(parcours): d-index-1 for index,parcours in enumerate(cE[i])}

        #utilite des parcours (scorede borda)
        uti_spe= {}
        for j in range(d):
            uti_spe[j]={(int)(etu) : n-index-1 for index,etu in enumerate(cP[j])}

        # Fonction objective : maximiser la somme des utilite
        m.setObjective(gp.quicksum(x[i,j]*uti_etu[i][j] + x[i,j]*uti_spe[j][i] for i in range(n) for j in range(d)), GRB.MAXIMIZE)

        # Contrainte 1 : Chaque étudiant est assigné a au plus 1 parcours
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in range(d))==1,f"assigne_{i}")

        #Contrainte 2 : Respect des capacités des parcours
        for j in range(d):
            m.addConstr(gp.quicksum(x[i,j] for i in range(n))==(int)(capacity[j]),f"capacite_{j}")

        #Contrainte 3 : Chaque etudiant doit être assigné a un de ses k premieres préférences
        for i in range(n):
            m.addConstr(gp.quicksum(x[i,j] for j in ([(int)(valeur) for valeur in cE[i][:k]]))==1,f"preference_{i}")
    
        #ecriture dans un fichier lp
        m.write("AllocationEtudiant_4.lp")
        # Optimize model
        m.optimize()

        affectations={}
        kpref={}
        with open("AllocationEtudiant_4.sol","w") as f:
            if m.status == GRB.OPTIMAL:
                f.write("Solution trouvée :\n")
                for i in range(n):
                    for j in range(d):
                        if x[i, j].x == 1:
                            f.write(f"Étudiant {i} affecté au parcours {j}\n")
                            affectations[i]=j
                f.write(f"Utilite maximal : {m.ObjVal}")
                for etu,parcours in affectations.items():
                    kpref[etu]=cE[etu].index((str)(parcours)) #etudiant a eu sont k-ieme preferer
            f.close()
            return affectations,kpref,m.ObjVal

    except gp.GurobiError as e:
        print(f"Error code {e.errno}: {e}")

    except AttributeError:
        print("Encountered an attribute error")

    return affectations,kpref,0