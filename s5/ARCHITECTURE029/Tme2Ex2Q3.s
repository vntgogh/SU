.data
o1 : .byte 0xFF

.text

lui $10,0x1001
lb $9,0($10)
lbu $10,0($10)

ori $4,$9,0 
ori $2,$0,1 #afficher o1 signé
syscall

ori $2, $0, 11 #retour à la ligne
ori $4, $0, 0x0A
syscall

ori $4,$10,0 
ori $2,$0,1 #afficher o1 non-signé
syscall

ori $2, $0, 10
syscall
