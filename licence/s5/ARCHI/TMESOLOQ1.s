.data
s : .space 20
ch_ok : .asciiz "bien parenthésé"
ch_nok : .asciiz "mal parenthésé"

.text 
main :
addiu $29,$29,-8 #1 paramètre + 1 variable locale

lui $3,0x1001
ori $4,$3,0
ori $5,$0,20
ori $2,$0,8
syscall
ori $2,$0,4
syscall

jal bon_parenthesage

sw $16,0($29) #ok = bon_parenthesage(s)

beq $16,$0,fin0

lui $3,0x1001
addiu $4,$3,37
ori $2,$0,4
syscall
j fin

fin0 : 
	lui $3,0x1001
	addiu $4,$3,20
	ori $2,$0,4
	syscall
fin :
	addiu $29,$29,8
	ori $2,$0,10
	syscall
	
bon_parenthesage :
addiu $29,$29,-12 #2 variables locales + @de retour
sw $31,8($29)
sw $0,0($29) #d=0
sw $0,4($29) #i=0

lw $9,4($29) # $9 <- i

ori $12,$0,0x28 #'('
ori $13,$0,0x29 #')'

loop :
	addu $10,$4,$9 # $10 <- @s[i]
	lbu $11,0($10) # $11 <- s[i]
	beq $11,$0,fin1 
	
	beq $11,$12,if1
	
	beq $11,$13,if2
	
	j if3
if1 :
	lw $16,0($29)
	addiu $16,$16,1
	sw $16,0($29)
	j if3
if2 : 
	lw $16,0($29)
	addiu $16,$16,-1
	sw $16,0($29)
	j if3
if3 :
	lw $16,0($29)
	bltz $16,fin1 #d<0
	addiu $9,$9,1
	j loop
fin1 :
	lw $16,0($29)
	addiu $29,$29,12
	jr $31