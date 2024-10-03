.data

v1 : .word -1
.align 2
v2 : .word 0xFF

.text

lui $8,0x1001 #charger le debut de l'adresse car 32bits max(pas 64 bits) 

lw $9,4($8) #mettre la valeur de $9 dans le registre $9 décalé de 4
lw $8,0($8) #mettre la valeur de $8 dans le registre $8 décalé de 0

ori $4,$8,0 
ori $2,$0,1 #afficher v1
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $4,$9,0
ori $2,$0,1 #afficher v2
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

addi $8,$8,1 #ajouter 1 à v1
addi $9,$9,1 #ajouter 1 à v2

ori $4,$8,0
ori $2,$0,1 #afficher
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $4,$9,0
ori $2,$0,1
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $2,$0,10
syscall
