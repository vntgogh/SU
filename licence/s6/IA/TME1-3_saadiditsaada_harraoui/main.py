import Projet as Projet
import PL

def tests():
    # Jeu de tests Gale-Shapley + paires instables

    etupref = [[0, 1, 2], [1, 2, 0], [2, 0, 1], [0, 2, 1]]
    spepref = [[3, 0, 1, 2], [2, 1, 3, 0], [1, 2, 0, 3]]

    affect_etu,_ = Projet.GS_etu(etupref, spepref, [1, 2, 1] )
    affect_master,_ = Projet.GS_master(etupref, spepref, [1, 2, 1] )

    res_affect_etu =  {1:1,2:2,3:0,0:1}
    res_affect_master =  {3:0,2:2,1:1,0:1} #etu0 est le moins satisfait

    assert affect_etu == res_affect_etu, f"Erreur GS_etu: {affect_etu} != {res_affect_etu}"
    assert affect_master == res_affect_master, f"Erreur GS_master: {affect_master} != {res_affect_master}"

    copie = affect_etu.copy()
    copie[0] = 0  # etudiant 0 prend le master 0
    copie[3] = 2  # etudiant 3 prend le master 2

    paires_instables = Projet.paires_instables(etupref, spepref, copie)
    res_paires_instables = [(3,0)]  
    assert paires_instables == res_paires_instables, f"Erreur paires_instables: {paires_instables} != {res_paires_instables}"

    print("Tests OK !")


def main():
    #Exercice 1 
    cE=Projet.studentpref("PrefEtu.txt")
    cP=Projet.masterpref("PrefSpe.txt")
    with open("Exercices.txt","w") as f:
        f.write("Application de GS_etu et GS_master avec PrefEtu.txt et PrefSpe.txt\n\n")
        affect_etu_optimal,_ = Projet.GS_etu(cE,cP,Projet.capacity_master("PrefSpe.txt"))
        affect_master_optimal,_ = Projet.GS_master(cE,cP,Projet.capacity_master("PrefSpe.txt"))
        f.write(f"Affectation master optimal : {affect_master_optimal}\n")
        f.write(f"Affectation Etudiant optimal : {affect_etu_optimal}\n\n")

        f.write("Verification des paires instables sur les affectations résultantes \n\n")
        paire_instables_etu=Projet.paires_instables(cE,cP,affect_etu_optimal)
        paire_instables_master=Projet.paires_instables(cE,cP,affect_master_optimal)
        f.write(f"Paires instables etu : {paire_instables_etu}\n")
        f.write(f"Paires instables master : {paire_instables_master}\n\n")

        while True:
            reponse = input("Voulez vous mesurez le temps de calculs des algorithme de GS ? (Y/N)\n").strip().lower()
            if reponse in ["y", "n"]:
                break
            print("Veuillez entrer 'Y' ou 'N'.")

        #Exercice 2

        if reponse in ["y"]:
            f.write("Mesure du temps de calculs des algorithmes de GS\n")
            f.write("Valeurs de n \t Temps d'éxecution étudiant \t Temps d'éxecution master\n")
            val_n,tests_etu,tests_master=Projet.time_gs()
            for n_v,time_etu,time_master in zip(val_n,tests_etu,tests_master):
                f.write(f"{n_v:<12}\t{time_etu:<30}\t{time_master:<30}\n")
        
        while True:
            reponse = input("\nVoulez vous mesurez le nombre d'iterations des algorithme de GS ? (Y/N)\n").strip().lower()
            if reponse in ["y", "n"]:
                break
            print("Veuillez entrer 'Y' ou 'N'.")

        if reponse in ["y"]:
            f.write("Mesure du nombre d'iterations des algorithmes de GS\n")
            f.write("Valeurs de n \t Nombre d'iterations étudiant \t Nombre d'iterations master\n")
            val_n,tests_etu,tests_master=Projet.it_gs()
            for n_v,ite_etu,ite_master in zip(val_n,tests_etu,tests_master):
                f.write(f"{n_v:<12}\t{ite_etu:<30}\t{ite_master:<30}\n")

            
        #Exercice 3 

        while True:
            reponse = input("Voulez vous resoudre les programmes linéaire et faire la comparaison finale du projet ? (Y/N)\n").strip().lower()
            if reponse in ["y", "n"]:
                break
            print("Veuillez entrer 'Y' ou 'N'.")

        if reponse in ["y"]:
            f.write("Premier PLNE : K premier choix \n\n")
            while True:
                k = (int)(input("Veuillez entrer une valeur de k \n"))
                if k>0 and k<=len(cE):
                    break
                print("Veuillez entrer une valeur entre 1 et ",len(cE))
            affect_PL1,k_prefPL1=PL.PL_resolve_1(k,cE,cP,Projet.capacity_master("PrefSpe.txt"))
            f.write(f"L'affectation trouvé est la suivante : {affect_PL1}\n")
            f.write(f"Les etudiants et le classement du parcours recu : {k_prefPL1}\n\n")

            f.write("Deuxieme PLNE : K premier choix maximisant l'utilité minimale des étudiants\n")
            while True:
                k = (int)(input("Veuillez entrer une valeur de k \n"))
                if k>0 and k<=len(cE):
                    break
                print("Veuillez entrer une valeur entre 1 et ",len(cE))
            affect_PL2,k_prefPL2,util_min_PL2=PL.PL_resolve_2(k,cE,cP,Projet.capacity_master("PrefSpe.txt"))
            f.write(f"L'affectation trouvé est la suivante : {affect_PL2}\n")
            f.write(f"Les etudiants et le classement du parcours recu : {k_prefPL2}\n")
            f.write(f"L'utilite minimal : {util_min_PL2}\n\n")

            f.write("Troisieme PLNE : Maximise la somme des utilité\n\n")
            affect_PL3 ,somme_uti_PL3,moy_uti_PL3 ,util_min_PL3 = PL.PL_resolve_3(cE,cP,Projet.capacity_master("PrefSpe.txt"))
            f.write(f"L'affectation trouvé est la suivante : {affect_PL3}\n")
            f.write(f"La somme des utilité : {somme_uti_PL3}\n")
            f.write(f"Utilité moyenne : {moy_uti_PL3}\n")
            f.write(f"L'utilité minimal : {util_min_PL3}\n\n")

            f.write("Quatrieme PLNE : Maximise la somme des utilité en prenant un des K premier choix \n\n")
            while True:
                k = (int)(input("Veuillez entrer une valeur de k \n"))
                if k>0 and k<=len(cE):
                    break
                print("Veuillez entrer une valeur entre 1 et ",len(cE))
            
            affect_PL4,k_prefPL4,somme_uti_PL4 = PL.PL_resolve_4(k,cE,cP,Projet.capacity_master("PrefSpe.txt"))
            f.write(f"L'affectation trouvé est la suivante : {affect_PL4}\n")
            f.write(f"La somme des utilité : {somme_uti_PL4}\n")
            f.write(f"Les etudiants et le classement du parcours recu : {k_prefPL4}\n\n")

            f.write("Comparaison des différentes solutions obtenues \n\n")
            
            #Utilité des étudiants (score de Borda)
            uti_etu= {}
            for i in range(len(cE)):
                uti_etu[i]={(int)(parcours): (len(cP))-index-1 for index,parcours in enumerate(cE[i])}

            #utilite des parcours (scorede borda)
            uti_spe= {}
            for j in range(len(cP)):
                uti_spe[j]={(int)(etu) : (len(cE))-index-1 for index,etu in enumerate(cP[j])}


            #Definition manquante des paires instable, de la moyenne des utilites et de la plus petite utilite 
            paire_instables_PL1,moy_uti_PL1,util_min_PL1=Projet.analyse_sol(affect_PL1,uti_etu,uti_spe)
            paire_instables_PL2,moy_uti_PL2,_=Projet.analyse_sol(affect_PL2,uti_etu,uti_spe)
            paire_instables_PL3,_,_=Projet.analyse_sol(affect_PL3,uti_etu,uti_spe)
            paire_instables_PL4,moy_uti_PL4,util_min_PL4,=Projet.analyse_sol(affect_PL4,uti_etu,uti_spe)
            _,moy_uti_etu,util_min_etu=Projet.analyse_sol(affect_etu_optimal,uti_etu,uti_spe)
            _,moy_uti_master,util_min_master=Projet.analyse_sol(affect_master_optimal,uti_etu,uti_spe)

            f.write(f"Solution Premier PLNE : \n Paires instables : {paire_instables_PL1}\n Moyenne des utilite : {moy_uti_PL1}\n Utilite minimal : {util_min_PL1}\n\n")
            f.write(f"Solution Deuxieme PLNE : \n Paires instables : {paire_instables_PL2}\n Moyenne des utilite : {moy_uti_PL2}\n Utilite minimal : {util_min_PL2}\n\n")
            f.write(f"Solution Troisieme PLNE : \n Paires instables : {paire_instables_PL3}\n Moyenne des utilite : {moy_uti_PL3}\n Utilite minimal : {util_min_PL3}\n\n")
            f.write(f"Solution Quatrieme PLNE : \n Paires instables : {paire_instables_PL4}\n Moyenne des utilite : {moy_uti_PL4}\n Utilite minimal : {util_min_PL4}\n\n")
            f.write(f"Solution Gale Shapley cote etudiant : \n Paires instables : {paire_instables_etu}\n Moyenne des utilite : {moy_uti_etu}\n Utilite minimal : {util_min_etu}\n\n")
            f.write(f"Solution Gale Shapley cote master : \n Paires instables : {paire_instables_master}\n Moyenne des utilite : {moy_uti_master}\n Utilite minimal : {util_min_master}\n\n")


            f.write("Fin du projet <3 !")



            

            


    

main()
                

        






# # Test de paires_instables côté étudiant en échangeant les masters de Etu0 et Etu3
# affect_etu_optimal[0] = 0
# affect_etu_optimal[3] = 5
# print ("Paires instables : ",Projet.paires_instables(cE,cP,affect_etu_optimal))
# print("\n")


# Test de time_gs pour un nombre d'étudiants variant entre 200 et 2000
#Projet.time_gs()