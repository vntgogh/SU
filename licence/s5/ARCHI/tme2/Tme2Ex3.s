.data
ch : .ascii "coucou"

.text
lui $8,0x1001 #affichage avant échange
ori $4,$8,0
ori $2,$0,4
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $4,$8,0 # Charger l'adresse de la chaîne dans $4
lb $5,0($4) # Charger le premier caractère dans $5
lb $6,1($4) # Charger le deuxième caractère dans $6
sb $6,0($4) # Placer le deuxième caractère à la position 0
sb $5,1($4) # Placer le premier caractère à la position 1

lui $8, 0x1001 #affichage après échange
ori $4, $8, 0      
ori $2,$0,4
syscall

ori $2,$0,10
syscall




