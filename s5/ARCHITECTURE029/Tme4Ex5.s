.data
tab : .word 4,23,12,3,8,1
s : .space 4 
p : .space 4

.text
lui $8,0x1001
lw $16,12($8)
lw $17,16($8)
ori $4,$16,0
ori $2,$0,1
syscall

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall

ori $4,$17,0
ori $2,$0,1
syscall

lw $18,20($8)
addi $18,$16,1

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall

ori $4,$18,0
ori $2,$0,1
syscall

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall

lw $19,24($8)
add $19,$16,$17
ori $4,$19,0
ori $2,$0,1
syscall

ori $2,$0,10
syscall
