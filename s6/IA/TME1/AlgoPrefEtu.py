import exemple

def AlgoPrefEtu(file):
    contenu = []
    contenu.lectureFichier(file)
    n = contenu[0]
    mat = [0 for i in range(n-1) for j in range(9)]

    for i in range(n):
        for j in range(9):
            for k in range(1,n+1):
                for l in range(2,11):
                    mat[i][j] = contenu[k][l]
    return mat

def AlgoPrefSpe(file):