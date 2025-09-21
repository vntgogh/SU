Ines HARRAOUI
Richard ENG
Nawad KARIHILA
Maxime

Exercice 2


1. Pour x0 = 2, α = 0.3, ε = 0.001 :

la suite semble converger vers L=1.0 et le rapport |x(n+1)-1|/|x(n)-1| diminue. 
En effet, |x7-1|/|x6-1| ≈ 0.01837405859191
        > |x8-1|/|x7-1| ≈ 0.00962030941684
        > |x9-1|/|x8-1| ≈ 0.00497942768741
        > |x10-1|/|x9-1| ≈ 0.00246822605736
        > |x11-1|/|x10-1| ≈ 0.00123739048061

On constate que le rapport |x(n+1)-L|/|x(n)-L| diminue rapidement puis de manière constante
C'est donc une convergence linéaire vers L=1.



2. Pour x0 = 2, α = 0.3, ε = 10^(−14) :
la suite semble converger vers L=1.0 et le rapport |x(n+1)-1|/|x(n)-1| diminue.
En effet, |x(47)-L|/|x(46)-L|=  0.99999999999987 
        < |x(48)-L|/|x(47)-L| = 0,99999999999994
        < |x(49)-L|/|x(48)-L| = 0,99999999999997

Les rapports tendent rapidement vers 1, ce qui veut dire que |x(n+1)-1| diminue 
de manière exponentielle par rapport à |x(n)-1|. C'est donc une convergence exponentielle.



3. Pour x0 = 5, α = 3.5 et ε = 10^(−14) :
la suite semble converger vers L=3.5 et le rapport |x(n+1)-1|/|x(n)-1| diminue.
En effet, les rapports des 5 derniers termes qui vérifient |x(n+1)-x(n)| > ε, ci-dessous montre
une diminution lente pour chaque itération :

    |x3-3.5|/|x2-3.5| ≈ 0.06287555848034
  > |x4-3.5|/|x3-3.5| ≈ 0.00621185261663
  > |x5-3.5|/|x4-3.5| ≈ 0.00087528282575
  > |x6-3.5|/|x5-3.5| ≈ 0.00000088655363
  > |x7-3.5|/|x6-3.5| = 0

La limite de ces rapports tend vers 0 et suggère donc une convergence logarithmique vers 0.
La convergence est logarithmique vers la limite L=3.5. 



4. Pour x0 = 0.5, α = 3.5, ε = 10^(−14) :
la suite semble converger vers L=1 et le rapport |x(n+1)-L|/|x(n)-L| diminue
En effet, |x42-1|/|x41-1| ≈ 0.08004897959185
        > |x43-1|/|x42-1| ≈ 0.03633673469387
        > |x44-1|/|x43-1| ≈ 0.01700612244898
        > |x45-1|/|x44-1| ≈ 0.00794897959184
        > |x46-1|/|x45-1| ≈ 0.00372448979592

On que la différence entre les termes consécutifs diminue à chaque itération de manière lente. 
Cela suggère une convergence logarithmique vers la limite.
La convergence est logarithmique vers la limite L=1. 



5. Pour x0 = −3.0, α = 1.0, ε = 10^(−14) :
La suite semble converger vers L=-2 et le rapport |x(n+1)-L|/|x(n)-L| augmente. 
En effet, |x44-2|/|x43-2| ≈ 0.49999637614
        < |x45-2|/|x44-2| ≈ 0.49999818807
        < |x46-2|/|x45-2| ≈ 0.49999941657
        < |x47-2|/|x46-2| ≈ 0.49999980206
        < |x48-2|/|x47-2| ≈ 0.49999995068

On constate que les valeurs sont proches de 0.5 
ce qui signifie que le rapport |x(n+1) - 2| / |x(n) - 2| converge rapidement vers 0.5. 
La convergence est rapide donc elle est logarithmique vers la limite L=2. 



6. Pour x0 = 2.0, α = 1.0, ε = 10^(−14) :
La suite semble converger vers L=1 et le rapport |x(n+1)-L|/|x(n)-L| reste constant.
En effet, |x48-1|/|x47-1| ≈ 1.0
          |x49-1|/|x48-1| ≈ 1.0
          |x50-1|/|x49-1| ≈ 1.0
          |x51-1|/|x50-1| ≈ 1.0
          |x52-1|/|x51-1| ≈ 1.0

On constate que le rapport |x(n+1) - L| / |x(n) - L| est égal à 1 pour les derniers termes.
Cette convergence est donc linéaire vers la limite L=1. 