def delta(liste):
 t= [liste[0]]
 for i in range(len(liste)-1):
  diff= liste[i+1]-liste[i]
  t.append(diff)
 return t