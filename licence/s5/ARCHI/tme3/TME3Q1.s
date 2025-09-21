.data
str : .byte 20

.text

main :
addiu $29,$29,-16

lui $8,0x1001
ori $2, $0,8
ori $4,$8,0
ori $5,$0,20
syscall

jal len

sw $16,8($29)

addu $5,$4,$16
addiu $5,$5,-1

jal est_palin

sw $17,12($29)

lw $9,12($29)

ori $4,$9,0
ori $2,$0,1
syscall

addiu $29,$29,8
ori $2,$0,10
syscall

len :
#contexte pile : 1 variable locale + @ de retour
addiu $29,$29,-8
sw $31,4($29)
sw $0,0($29)

lw $16,0($29)

loop :
	addu $10,$4,$16
	lb $11,0($10)
	beq $11,$0,fin1
	
	addiu $16,$16,1
	
	j loop
	
fin1 : 
	addiu $16,$16,-1
	addiu $29,$29,8
	jr $31
	
est_palin :
addiu $29,$29,-4
sw $31,0($29)

loop1 :
	slt $8,$5,$4
	bne $8,$0,fin2
	
	lb $9,0($4)
	lb $10,0($5)
	
	bne $9,$10,fin3
	
	addiu $4,$4,1
	addiu $5,$5,-1
	
	j loop1

fin2 : 
	addiu $2,$0,0
	addiu $29,$29,4
	jr $31

fin3 :
	addiu $2,$0,1
	addiu $29,$29,4
	jr $31
