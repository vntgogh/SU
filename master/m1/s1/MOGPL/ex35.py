#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:13:59 2025

@author: 21204796
"""

"""from numpy import *
from pylab import *

xi = array([4,17,37,55,88,71])
A = array([xi,ones(6)])

y = [11,25,46,48,65,95]

w = linalg.lstsq(A.T,y)[0]
print(w[0])
print(w[1])
line = w[0]*xi+w[1]
plot(xi,line,'r-',xi,y,'o')
show()"""
from gurobipy import *


nbcont=12
nbvar=8

# Range of plants and warehouses
lignes = range(nbcont)
colonnes = range(nbvar)

xi = [4,17,37,55,88,14]

# Matrice des contraintes
a = [[1,0,0,0,0,0,xi[0],1],
     [1,0,0,0,0,0,-xi[0],-1],
     [0,1,0,0,0,0,xi[1],1],
     [0,1,0,0,0,0,-xi[1],-1],
     [0,0,1,0,0,0,xi[2],1],
     [0,0,1,0,0,0,-xi[2],-1],
     [0,0,0,1,0,0,xi[3],1],
     [0,0,0,1,0,0,-xi[3],-1],
     [0,0,0,0,1,0,xi[4],1],
     [0,0,0,0,1,0,-xi[4],-1],
     [0,0,0,0,0,1,xi[5],1],
     [0,0,0,0,0,1,-xi[5],-1]]

# Second membre
b = [11, -11, 25, -25, 46, -46, 48, -48, 65, -65, 97, -97]

# Coefficients de la fonction objectif
c = [1,1,1,1,1,1,0,0]

m = Model("mogplex")     
        
# declaration variables de decision
x = []
for i in colonnes:
    x.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))

# maj du modele pour integrer les nouvelles variables
m.update()

obj = LinExpr();
obj =0
for j in colonnes:
    obj += c[j] * x[j]
        
# definition de l'objectif
m.setObjective(obj,GRB.MINIMIZE)

# Definition des contraintes
for i in lignes:
    m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) >= b[i], "Contrainte%d" % i)

# Resolution
m.optimize()


print("")                
print('Solution optimale:')
for j in colonnes:
    print('x%d'%(j+1), '=', x[j].x)
print("")
print('Valeur de la fonction objectif :', m.objVal)

   


