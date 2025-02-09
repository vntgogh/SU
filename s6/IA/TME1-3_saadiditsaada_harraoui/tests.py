import Projet as Projet
import pytest as pt









# Tests de GS_etu et GS_master avec PrefEtu.txt et PrefSpe.txt
# affect_etu_optimal = Projet.GS_etu(Projet.studentpref("PrefEtu.txt"),Projet.masterpref("PrefSpe.txt"),Projet.capacity_master("PrefSpe.txt"))
# affect_master_optimal = Projet.GS_master(Projet.studentpref("PrefEtu.txt"),Projet.masterpref("PrefSpe.txt"),Projet.capacity_master("PrefSpe.txt"))
# print("Affectation master optimal : ",affect_master_optimal)
# print("Affectation Etudiant optimal : ",affect_etu_optimal)
# print("\n")

# # Test de paires_instables côté étudiant en échangeant les masters de Etu0 et Etu3
# affect_etu_optimal[0] = 0
# affect_etu_optimal[3] = 5
# print ("Paires instables : ",Projet.paires_instables(Projet.studentpref("PrefEtu.txt"),Projet.masterpref("PrefSpe.txt"),affect_etu_optimal))
# print("\n")


# Test de time_gs pour un nombre d'étudiants variant entre 200 et 2000
#Projet.time_gs()

Projet.it_gs()