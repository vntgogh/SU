# -*- coding: utf-8 -*-

"""
Package: iads
File: utils.py
Année: LU3IN026 - semestre 2 - 2024-2025, Sorbonne Université
"""


# Fonctions utiles
# Version de départ : Février 2025

# import externe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------ 

def genere_dataset_uniform(d, nc, binf=-1, bsup=1):
    """ int * int * float^2 -> tuple[ndarray, ndarray]
        Hyp: n est pair
        d: nombre de dimensions de la description
        nc: nombre d'exemples de chaque classe
        les valeurs générées uniformément sont dans [binf,bsup]
    """
    
    data_desc = np.random.uniform(binf,bsup,(2*nc,d))

    data_label = np.array([-1 for i in range(0,nc)] + [+1 for i in range(0,nc)])

    return (data_desc,data_label)

# ------------------------ 

def genere_dataset_gaussian(positive_center, positive_sigma, negative_center, negative_sigma, nc):
    """ les valeurs générées suivent une loi normale
        rend un tuple (data_desc, data_labels)
    """
    data_negatifs = np.random.multivariate_normal(negative_center, negative_sigma, nc)
    data_positifs = np.random.multivariate_normal(positive_center, positive_sigma, nc)

    data_desc = np.vstack((data_negatifs, data_positifs))

    data_labels = np.array([-1 for i in range(0,nc)] + [+1 for i in range(0,nc)])

    return data_desc, data_labels

# ------------------------ 

def plot2DSet(desc,labels,nom_dataset= "Dataset", avec_grid=False):    
    """ ndarray * ndarray * str * bool-> affichage
        nom_dataset (str): nom du dataset pour la légende
        avec_grid (bool) : True si on veut afficher la grille
        la fonction doit utiliser la couleur 'red' pour la classe -1 et 'blue' pour la +1
    """

    data2_negatifs = desc[labels == -1]
    data2_positifs = desc[labels == +1]

    # Tracé de l'ensemble des exemples :
    plt.scatter(data2_negatifs[:,0],data2_negatifs[:,1],marker='o', color="red", label='classe -1') # 'o' rouge pour la classe -1
    plt.scatter(data2_positifs[:,0],data2_positifs[:,1],marker='x', color="blue", label='classe +1') # 'x' bleu pour la classe +1

    # Informations d'affichage :
    plt.title("data2")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.grid()  # Grille: à mettre, ou pas

    # Visualisation du résultat
    plt.show()

# ------------------------ 

def plot_frontiere(desc_set, label_set, classifier, step=30):
    """ desc_set * label_set * Classifier * int -> NoneType
        Remarque: le 4e argument est optionnel et donne la "résolution" du tracé: plus il est important
        et plus le tracé de la frontière sera précis.        
        Cette fonction affiche la frontière de décision associée au classifieur
    """
    mmax=desc_set.max(0)
    mmin=desc_set.min(0)
    x1grid,x2grid=np.meshgrid(np.linspace(mmin[0],mmax[0],step),np.linspace(mmin[1],mmax[1],step))
    grid=np.hstack((x1grid.reshape(x1grid.size,1),x2grid.reshape(x2grid.size,1)))
    
    # calcul de la prediction pour chaque point de la grille
    res=np.array([classifier.predict(grid[i,:]) for i in range(len(grid)) ])
    res=res.reshape(x1grid.shape)
    # tracer des frontieres
    # colors[0] est la couleur des -1 et colors[1] est la couleur des +1
    plt.contourf(x1grid,x2grid,res,colors=["darksalmon","skyblue"],levels=[-1000,0,1000])

# ------------------------ 

def create_XOR(n, var):
    """ int * float -> tuple[ndarray, ndarray]
        Hyp: n et var sont positifs
        n: nombre de points voulus
        var: variance sur chaque dimension
    """
    
    data_desc1, data_label1 = genere_dataset_gaussian(np.array([1,0]),np.array([[var, 0],[0, var]]),np.array([0,0]),np.array([[var, 0],[0, var]]),n)
    data_desc, data_label = genere_dataset_gaussian(np.array([0,1]),np.array([[var, 0],[0, var]]),np.array([1,1]),np.array([[var, 0],[0, var]]),n)
    return (np.concatenate((data_desc1, data_desc)), np.concatenate((data_label1, data_label)))