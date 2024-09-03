#exercice1
class BinaryTreeCode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

    def insert(abr,y):
        if abr != None:
            x = abr.data
        if abr != None:
            if y < x :
                if abr.left != None:
                    y= abr.left
                else:
                    abr.left=insert(abr.left, y)
            elif val > abr.data:
                if abr.right != None:
                    abr.right = abr(y)
                else:
                    abr.right=insert(abr.right,y)
        else:
            y = abr.data

#exercice2
#question1
    def prefixe(abr,x):
        if abr != None:
            x= abr.data
        print(x + prefixe(x.left) + prefixe(abr.right)
#question2
    def infixe(abr,x):
        if abr != None:
            x= abr.data
        print(infixe(abr.left) + x + infixe(abr.right))

#exercice3
def recherche(abr,k: int) :
  if abr == None :
    return False
    else:
      x = abr.data
      if k == x :
        return True
      if k < x :
        return recherche(abr.left,k)
      else :
        return recherche(abr.right,k)

#exercice4
def extremum(abr):
    if abr == None:
        return min=0, max=0
    else:
        e = abr.data
        f = abr.data
        min = extremum(abr.left)
        max = extremum(abr.right)
        if (min > x):
            e = min
        if (max > f):
            f = max
        return e

#exercice5
#question1
On obtient une suite de sous-arbres droits
#question2
def hauteur(abr) :
  if abr =! None :
    x = abr.data
    return 1 + max(hauteur(abr.left), hauteur(abr.right))
  else :
    return 0
#question3
#question4
#question5
"""def inserte(abr):
    A=insertion(abr,k)
    G=abr.left
    D=abr.right
    if hauteur(G)-hauteur(D)<2:
        return abr"""



