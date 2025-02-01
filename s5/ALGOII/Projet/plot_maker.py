import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

def graph_temps():
    # Lire le fichier et préparer les données
    file_path = 'eval_temps_exec_16.txt'

    # Initialiser des structures pour les données
    sections = {}
    current_section = None

    # Lire le fichier ligne par ligne
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                current_section = line[1:]  # Enlever le symbole '#' pour obtenir le nom de la section
                sections[current_section] = []  # Initialiser la liste pour cette section
            elif line and current_section is not None:
                values = line.split()
                try:
                    sections[current_section].append([float(v) for v in values])
                except ValueError:
                    continue  # Ignore toute ligne qui ne peut pas être convertie en float

    # Générer un graphe pour chaque section
    for section, values in sections.items():
        # Créer un DataFrame pour faciliter la manipulation des données
        df = pd.DataFrame(values, columns=["S", "K", "Algo1", "Algo2", "Algo3"])

        # Extraire les colonnes nécessaires
        S = df["S"]
        temps_algo_1 = df["Algo1"]
        temps_algo_2 = df["Algo2"]
        temps_algo_3 = df["Algo3"]
        K = df["K"].iloc[0]  # K est constant dans chaque section

        # Calculer les valeurs logarithmiques de S et des temps
          # Logarithme base 2 pour S
        temps_algo_1_log = np.log10(temps_algo_1)  # Logarithme base 10 pour les temps
        temps_algo_2_log = (temps_algo_2)
        temps_algo_3_log = temps_algo_3

        # Créer le graphe
        plt.figure(figsize=(10, 6))
        #plt.plot(S_log, temps_algo_1_log, label='Algo 1 (Log Temps)', marker='o')
        #plt.plot(S, temps_algo_2_log, label='Algo 2 Temps', marker='s')
        plt.plot(S, temps_algo_3_log, label='Algo 3 (Temps)', marker='^')

        # Ajouter des détails au graphe
        plt.xlabel('S')
        plt.ylabel('Temps (s)')
        plt.title(f'temps dexecution pour {section} (K = {K})')
        plt.legend()
        plt.grid(True)
        plt.show()

# Appeler la fonction pour tracer les graphes

graph_temps()

def graph_prop():
# Lire le fichier et charger les données
    file_path = 'eval_30_glouton_proportion.txt'
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Extraire les colonnes K et proportionalite
    K = data['K']
    proportion = data['proportionalite']

    # Créer un graphique
    plt.figure(figsize=(10, 6))
    plt.plot(K, proportion, marker='o', color='b', label='Proportionnalité')

    # Ajouter des détails au graphique
    plt.xlabel('K')
    plt.ylabel('Proportionnalité (%)')
    plt.title('Proportionnalité en fonction de K')
    plt.legend()
    plt.grid(True)
    plt.show()





# Fonction pour lire et traiter les données du fichier
def lire_donnees(fichier):
    systemes = []
    pire_ecarts = []
    ecarts_moyens = []

    with open(fichier, 'r') as file:
        contenu = file.read()
        # Extraire les informations avec des expressions régulières
        systeme_nums = re.findall(r"Systeme non glouton compatible : (\d+)", contenu)
        pire_ecarts_vals = re.findall(r"Pire ecart = (\d+)", contenu)
        ecarts_moyens_vals = re.findall(r"Ecart Moyen = ([\d\.]+)", contenu)

        # Convertir les valeurs en entiers et flottants
        systemes = [int(num) for num in systeme_nums]
        pire_ecarts = [int(ecart) for ecart in pire_ecarts_vals]
        ecarts_moyens = [float(ecart) for ecart in ecarts_moyens_vals]

    return systemes, pire_ecarts, ecarts_moyens


def graph_ecart():
    # Lire les données à partir du fichier
    fichier = 'eval_glouton_compatible.txt'  # Remplacez 'donnees.txt' par le nom de votre fichier
    systemes, pire_ecarts, ecarts_moyens = lire_donnees(fichier)

    # Graphique en barres pour le pire écart
    plt.figure(figsize=(14, 6))
    plt.bar(systemes, pire_ecarts, color='orange', label='Pire écart')
    plt.xlabel('Valeur de k')
    plt.ylabel('Pire écart')
    plt.title('Pire écart pour chaque système')
    plt.xticks(systemes)
    plt.legend()
    plt.show()

    # Graphique en lignes pour l'écart moyen
    plt.figure(figsize=(14, 6))
    plt.plot(systemes, ecarts_moyens, marker='o', color='blue', label='Écart Moyen')
    plt.xlabel('Valeur de k')
    plt.ylabel('Écart Moyen')
    plt.title("Écart Moyen pour chaque système")
    plt.xticks(systemes)
    plt.legend()
    plt.show()

    # Diagramme en dispersion pour comparer les écarts
    plt.figure(figsize=(14, 6))
    plt.scatter(systemes, pire_ecarts, color='red', label='Pire écart', alpha=0.6)
    plt.scatter(systemes, ecarts_moyens, color='green', label='Écart Moyen', alpha=0.6)
    plt.xlabel('Valeur de k')
    plt.ylabel('Valeurs des écarts')
    plt.title("Comparaison des Pires écarts et des Écarts Moyens")
    plt.xticks(systemes)
    plt.legend()
    plt.show()
