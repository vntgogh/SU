PI = 3.14

def carre_peri(cote):
    return 4 * cote

def carre_aire(cote):
    return cote * cote

def carre_vol(cote):
    return cote * cote * cote

def cercle_peri(rayon):
    return 2 * PI * rayon

def cercle_aire(rayon):
    return PI * rayon**2

def cercle_vol(rayon):
    return 4 * PI * rayon**3 /3

if __name__ == '__main__': #si le lancement de mon programme se fait sur le fichier geoshape on fera les tests par cette condition
    print("Périmètre du carre :", carre_peri(10))
    print("Aire du carre :", carre_aire(10))
    print("Volume du carre :", carre_vol(10), "\n")
    print("Rayon du cercle : %.2f" % cercle_peri(5))
    print("Aire du cercle : %.2f" % cercle_aire(10))
    print("Volume du cercle : %.2f" % cercle_vol(10))