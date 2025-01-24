import exemple

def AlgoPrefEtu(file):
    contenu = exemple.lectureFichier(file)
    n = int(contenu[0])
    mat = [[0]*9 for i in range((int)(contenu[0][0]))]
    
    for i in range(n):
        print(contenu[i])
    return mat

def AlgoPrefSpe(file):
    contenu = exemple.lectureFichier(file)
    n = int(contenu[0])
    cap = contenu[1]
    mat = [0 for i in range(9) for j in range(int(cap[i]))]

    for i in range(9):
        for j in range(int(cap[i])):
            mat[i][j] = contenu[i+2][j+2]
    return mat

print(AlgoPrefEtu("PrefEtu.txt"))