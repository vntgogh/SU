import geoshape

carre_cote =2

peri = geoshape.carre_peri(carre_cote)
print("Le perimetre du carre de cote", carre_cote, "est", peri)

aire = geoshape.carre_aire(carre_cote)
print("L'aire du carre de cote", carre_cote, "est", aire)

volu = geoshape.carre_vol(carre_cote)
print("Le volume du carre de cote", carre_cote, "est", volu, "\n")

cercle_rayon = 5

perii = geoshape.cercle_peri(cercle_rayon)
print("Le périmètre du cercle de rayon", cercle_rayon, "est %.2f" % perii)

airee = geoshape.cercle_aire(cercle_rayon)
print("L'aire du cercle de rayon", cercle_rayon, "est %.2f" % airee)

vol = geoshape.cercle_vol(cercle_rayon)
print("Le volume du cercle de rayon", cercle_rayon, "est %.2f" % vol)



