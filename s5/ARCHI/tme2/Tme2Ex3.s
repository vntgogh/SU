.data
ch : .ascii "coucou"

.text
lui $8,0x1001 #affichage avant �change
ori $4,$8,0
ori $2,$0,4
syscall

ori $2, $0, 11 #retour � la ligne
ori $4, $0, 0x0A
syscall

ori $4,$8,0 # Charger l'adresse de la cha�ne dans $4
lb $5,0($4) # Charger le premier caract�re dans $5
lb $6,1($4) # Charger le deuxi�me caract�re dans $6
sb $6,0($4) # Placer le deuxi�me caract�re � la position 0
sb $5,1($4) # Placer le premier caract�re � la position 1

lui $8, 0x1001 #affichage apr�s �change
ori $4, $8, 0      
ori $2,$0,4
syscall

ori $2,$0,10
syscall




