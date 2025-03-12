# -*- coding: utf-8 -*-

"""
Package: iads
File: evaluation.py
Année: LU3IN026 - semestre 2 - 2024-2025, Sorbonne Université
"""

# ---------------------------
# Fonctions d'évaluation de classifieurs

# import externe
import numpy as np
import pandas as pd
import copy 

# ------------------------ 
def crossval(X, Y, n_iterations, iteration):
    """sépare un dataset en un ensemble d'apprentissage et un ensemble de tests
    - X, Y sont les données du dataset **mélangées aléatoirement** (on ne mélange pas physiquement les données, mais seulement leurs indices)
    - n_iterations est le nombre d'ensembles de test au total.
    - iteration est l'itération concernée: on ne renvoit pas les mêmes données en fonction des itérations.
    """
    debut = int(iteration * len(X)//n_iterations) #len(X)//n_iterations est la taille d'un test
    if iteration == n_iterations -1:
        fin = int(len(X))
    else :
        fin = int(len(X)*iteration*(iteration+1)/n_iterations)

    Xtest = X[debut:fin]
    Ytest = Y[debut:fin]
    Xapp = np.concatenate((X[:debut],X[fin:]), 0)
    Yapp = np.concatenate((Y[:debut],Y[fin:]),0)

    return Xapp, Yapp, Xtest, Ytest

# ------------------------ 

# code de la validation croisée (version qui respecte la distribution des classes)

def crossval_strat(X, Y, n_iterations, iteration):
    """permet de s'assurer que chaque ensemble d'apprentissage et de test ont la meme proportion de classes
    - X : descripteurs 
    - Y : labels 
    - n_iterations : nombre de partitions à effectuer
    - iteration : indice de l'itération actuelle

    """

    idx_class1 = np.where(Y == 1)[0]
    idx_class_1 = np.where(Y == -1)[0]

    np.random.shuffle(idx_class1)
    np.random.shuffle(idx_class_1)

    n_class1 = len(idx_class1)//n_iterations
    n_class_1 = len(idx_class_1)//n_iterations

    start1, end1 = iteration * n_class1, (iteration + 1) * n_class1
    start_1, end_1 = iteration * n_class_1, (iteration + 1) * n_class_1

    idx_test = np.concatenate((idx_class1[start1:end1], idx_class_1[start_1:end_1]))
    idx_train = np.setdiff1d(np.arange(len(Y)), idx_test)

    Xtest, Ytest = X[idx_test], Y[idx_test]
    Xapp, Yapp = X[idx_train], Y[idx_train]

    return Xapp, Yapp, Xtest, Ytest


# ------------------------ 
def analyse_perfs(L):
    """ L : liste de nombres réels non vide
        rend le tuple (moyenne, écart-type)
    """
    return (np.mean(L), np.std(L))    

# ------------------------ 
def validation_croisee(C, DS, nb_iter):
    """ Classifieur * tuple[array, array] * int -> tuple[ list[float], float, float]
    """
   
    X, Y = DS  # Récupération des données et labels
    perf = []  # Stocke les performances pour chaque itération
    
    for _ in range(nb_iter):
        # Mélange des indices pour randomiser l'ordre des exemples
        indices = np.arange(len(X))
        np.random.shuffle(indices)
        X_shuffled, Y_shuffled = X[indices], Y[indices]
        
        # Séparation en apprentissage (80%) et test (20%)
        split_idx = int(0.8 * len(X_shuffled))
        X_train, X_test = X_shuffled[:split_idx], X_shuffled[split_idx:]
        Y_train, Y_test = Y_shuffled[:split_idx], Y_shuffled[split_idx:]
        
        # Création et entraînement du classifieur
        classifier = copy.deepcopy(C)  # Duplication du classifieur
        classifier.train(X_train, Y_train)
        
        # Évaluation sur l'ensemble de test
        accuracy = classifier.accuracy(X_test, Y_test)
        perf.append(accuracy)
    
    # Calcul des statistiques de performance
    perf_moyenne = np.mean(perf)
    perf_ecart = np.std(perf)
    
    return perf, perf_moyenne, perf_ecart
