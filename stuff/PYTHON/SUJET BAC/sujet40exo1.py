def recherche(elt,tab):
 l= []
 for i in range(len(tab)):
  if tab[i]== elt:
   l.append(i)
 return l
