.data
var1 : .word 0xFF
.align 2
var2 : .space 4

.text

lui $8, 0x1001

lw $9,0($8) 

ori $4,$9,0
ori $2,$0,1 #afficher var1
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

addiu $9,$9,5
#ori $8,$8,0x4 #charger les 16 bits de poids faible de var2
#sw $9,0($8) #

sw $9,4($8)

ori $4,$9,0
ori $2,$0,1 #afficher var1 dans var2
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $2,$0,10
syscall