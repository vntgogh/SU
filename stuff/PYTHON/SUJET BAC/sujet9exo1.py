def calcul(n):
    l=[]
    while n!=1:
       l.append(n)
       if n%2==0:
        n=n//2
       else:
        n=n*3+1
    return l


