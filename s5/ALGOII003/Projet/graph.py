import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier et préparer les données
file_path = 'eval_temps_exec_800.txt'

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
    #temps_algo_1 = df["Algo1"]
    temps_algo_2 = df["Algo2"]
    temps_algo_3 = df["Algo3"]
    K = df["K"].iloc[0]  # K est constant dans chaque section

    # Créer le graphe
    plt.figure(figsize=(10, 6))
    #plt.plot(S, temps_algo_1, label='Algo 1', marker='o')
    #plt.plot(S, temps_algo_2, label='Algo 2', marker='s')
    plt.plot(S, temps_algo_3, label='Algo 3', marker='^')

    # Ajouter des détails au graphe
    plt.xlabel('S')
    plt.ylabel('Temps (s)')
    plt.title(f'Comparaison des temps des algorithmes pour {section} (K = {K})')
    plt.legend()
    plt.grid(True)
    plt.show()