# -*- coding: utf-8 -*-

"""
Package: iads
File: Clustering.py
Année: LU3IN026 - semestre 2 - 2024-2025, Sorbonne Université
"""

# ---------------------------
# Fonctions de Clustering

# import externe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------ 

def normalisation(df):
    df_norm = (df-df.min()) / (df.max()-df.min())
    return df_norm

def dist_euclidienne(x1, x2):
    
    x1 = np.array(x1).flatten()
    x2 = np.array(x2).flatten()

    return np.linalg.norm(x1 - x2)

def centroide(df):

    data = np.array(df)
    return np.mean(df,axis=0)

def dist_centroides(groupe1, groupe2):
    return np.linalg.norm(centroide(groupe1) - centroide(groupe2))

def initialise_CHA(DF):
    partition = {}
    for i in range(len(DF)):
        partition[i] = [i]
    return partition

def fusionne(DF, P0, verbose=False):
    best_distance = float('inf')
    best_pair = (None, None)
    keys = list(P0.keys())

    for i in range(len(keys) - 1):
        for j in range(i + 1, len(keys)):
            key1 = keys[i]
            key2 = keys[j]
            cluster1 = DF.iloc[P0[key1]]
            cluster2 = DF.iloc[P0[key2]]
            d = dist_centroides(cluster1, cluster2)
            if d < best_distance:
                best_distance = d
                best_pair = (key1, key2)

    cl1, cl2 = best_pair
    new_key = max(P0.keys()) + 1
    new_cluster = P0[cl1] + P0[cl2]

    if verbose:
        print(f"fusionne: on fusionne {cl1} et {cl2} à la distance {best_distance:.4f}")

    del P0[cl1]
    del P0[cl2]
    P0[new_key] = new_cluster

    return P0, cl1, cl2, best_distance

import scipy.cluster.hierarchy

def CHA_centroid(DF, verbose=False, dendrogramme=False):
    """
    Applique CHA avec centroid linkage
    et retourne la matrice de liaison pour affichage du dendrogramme.
    """
    partition = initialise_CHA(DF)
    fusion_results = []  
    next_cluster_index = len(partition)  # indices pour nouveaux clusters
    
    while len(partition) > 1:
        best_distance = float('inf')
        best_pair = (None, None)
        keys = list(partition.keys())
        
        for i in range(len(keys) - 1):
            for j in range(i + 1, len(keys)):
                key1 = keys[i]
                key2 = keys[j]
                cluster1 = DF.iloc[partition[key1]]
                cluster2 = DF.iloc[partition[key2]]
                d = dist_centroides(cluster1, cluster2)
                if d < best_distance:
                    best_distance = d
                    best_pair = (key1, key2)
        
        taille_total = len(partition[best_pair[0]]) + len(partition[best_pair[1]])
        
        if verbose:
            print(f"fusion des clusters {best_pair[0]} et {best_pair[1]} avec distance {best_distance:.4f} et taille {taille_total}")
        
        partition, cl1, cl2, distance = fusionne(DF, partition, verbose=verbose)
        
        fusion_results.append([cl1, cl2, distance, taille_total])
        
        next_cluster_index += 1
    
    linkage_matrix = np.array(fusion_results)

    if dendrogramme:
        plt.figure(figsize=(30, 15))
        plt.title('Dendrogramme', fontsize=25)
        plt.xlabel("Indice d'exemple", fontsize=25)
        plt.ylabel('Distance', fontsize=25)
        scipy.cluster.hierarchy.dendrogram(
            linkage_matrix,
            leaf_font_size=24.
        )
        plt.show()

    return linkage_matrix

import numpy as np
from scipy.spatial.distance import cdist

def dist_simple(cluster1, cluster2):
    """Distance minimale (single linkage)"""
    return np.min(cdist(cluster1, cluster2))

def dist_complete(cluster1, cluster2):
    """Distance maximale (complete linkage)"""
    return np.max(cdist(cluster1, cluster2))

def dist_average(cluster1, cluster2):
    """Distance moyenne (average linkage)"""
    return np.mean(cdist(cluster1, cluster2))


def CHA_linkage(DF, linkage_func, verbose=False, dendrogramme=False):
    """
    Clustering hiérarchique générique avec une fonction de linkage
    """
    partition = initialise_CHA(DF)
    fusion_results = []
    next_cluster_index = max(partition.keys()) + 1

    while len(partition) > 1:
        best_distance = float('inf')
        best_pair = (None, None)
        keys = list(partition.keys())

        for i in range(len(keys) - 1):
            for j in range(i + 1, len(keys)):
                key1 = keys[i]
                key2 = keys[j]
                cluster1 = DF.iloc[partition[key1]]
                cluster2 = DF.iloc[partition[key2]]
                d = linkage_func(cluster1.values, cluster2.values)
                if d < best_distance:
                    best_distance = d
                    best_pair = (key1, key2)

        cl1, cl2 = best_pair
        new_cluster = partition.pop(cl1) + partition.pop(cl2)
        partition[next_cluster_index] = new_cluster

        taille_total = len(new_cluster)
        fusion_results.append([cl1, cl2, best_distance, taille_total])
        if verbose:
            print(f"fusion des clusters {cl1} et {cl2} à distance {best_distance:.4f} (taille {taille_total})")

        next_cluster_index += 1

    linkage_matrix = np.array(fusion_results)

    if dendrogramme:
        plt.figure(figsize=(30, 15))
        plt.title('Dendrogramme', fontsize=25)
        plt.xlabel("Indice d'exemple", fontsize=25)
        plt.ylabel('Distance', fontsize=25)
        scipy.cluster.hierarchy.dendrogram(linkage_matrix, leaf_font_size=24.)
        plt.show()

    return linkage_matrix


def CHA_centroid(DF, verbose=False, dendrogramme=False):
    return CHA_linkage(DF, dist_centroides, verbose, dendrogramme)

def CHA_complete(DF, verbose=False, dendrogramme=False):
    return CHA_linkage(DF, dist_complete, verbose, dendrogramme)

def CHA_simple(DF, verbose=False, dendrogramme=False):
    return CHA_linkage(DF, dist_simple, verbose, dendrogramme)

def CHA_average(DF, verbose=False, dendrogramme=False):
    return CHA_linkage(DF, dist_average, verbose, dendrogramme)


def CHA(DF,linkage='centroid', verbose=False,dendrogramme=False):
    """  ##### donner une documentation à cette fonction
    """
    ############################ A COMPLETER

    linkage_funcs = {
        'centroid': dist_centroides,
        'complete': dist_complete,
        'simple': dist_simple,
        'average': dist_average
    }

    if linkage not in linkage_funcs:
        raise ValueError(f"Méthode de linkage inconnue : '{linkage}'. Choisissez parmi {list(linkage_funcs.keys())}.")

    dist_func = linkage_funcs[linkage]
    partition = initialise_CHA(DF)
    fusion_results = []
    next_cluster_index = max(partition.keys()) + 1

    while len(partition) > 1:
        best_distance = float('inf')
        best_pair = (None, None)
        keys = list(partition.keys())

        for i in range(len(keys) - 1):
            for j in range(i + 1, len(keys)):
                key1 = keys[i]
                key2 = keys[j]
                cluster1 = DF.iloc[partition[key1]]
                cluster2 = DF.iloc[partition[key2]]
                d = dist_func(cluster1.values, cluster2.values)
                if d < best_distance:
                    best_distance = d
                    best_pair = (key1, key2)

        cl1, cl2 = best_pair
        new_cluster = partition.pop(cl1) + partition.pop(cl2)
        partition[next_cluster_index] = new_cluster

        taille_total = len(new_cluster)
        fusion_results.append([cl1, cl2, best_distance, taille_total])
        if verbose:
            print(f"fusion des clusters {cl1} et {cl2} à distance {best_distance:.4f} (taille {taille_total})")

        next_cluster_index += 1

    linkage_matrix = np.array(fusion_results)

    if dendrogramme:
        plt.figure(figsize=(30, 15))
        plt.title(f'Dendrogramme - {linkage.capitalize()} linkage', fontsize=25)
        plt.xlabel("Indice d'exemple", fontsize=25)
        plt.ylabel('Distance', fontsize=25)
        scipy.cluster.hierarchy.dendrogram(linkage_matrix, leaf_font_size=24.)
        plt.show()

    return linkage_matrix
    