def xor(t1, t2):
    t=[]
    n = len(t1)
    for i in range(n):
        if t1[i] == t2[i]:
            t.append(0)
        else :
            t.append(1)
    return t