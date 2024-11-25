.data 
user_num : .space 4 #0x10010000
tab_chiffre : .space 40 #0x10010004

.text
main :
lui $3,0x1001

#contexte pile : 1var loclae + 2 prametres
addiu $29,$29,-12
ori $2,$0,5
syscall
addiu $4,$2,0
sw $4,0($29)
addiu $5,$3,4
sw $5,4($29)

jal occ_num_chiffre

lui $3,0x1001
addiu $4,$3,0
sw $4,0($29)

jal affichage

ori $16,$2,0
ori $4,$16,0
ori $2,$0,1
syscall

addiu $29,$29,12
ori $2,$0,10
syscall


occ_num_chiffre :
#contexte pile : 3 var locales + @ de retour
addiu $29,$29,-16

ori $16,$0,1
sw $16,0($29) # nb_c =1

ori $8,$4,0 # $8 <- @n
sw $8,4($29) # q = n

ori $9,$0,10

loop :
	#while (q >= 10)
	slt $13,$8,$9
	bne $0,$13, fin
	
	div $8,$9
	
	# r = q % 10
	mfhi $10
	sw $10,8($29)
	
	# q = q / 10
	mflo $8
	
	# t[r] +=1
	sll $11,$10,2
	addu $11,$5,$11 # $11 <- @t[r]
	
	lw $12,0($11) # $12 <- t[r]
	addiu $12,$12,1
	sw $12,0($11)
	
	#nb_c +=1
	addiu $16,$16,1
	
	j loop

fin :
	# t[q] += 1
	sll $11,$8,2
	addu $11,$5,$11
	lw  $12,0($11)
	addiu $12,$12,1
	sw $12,0($11)
	#resultat dans $2
	ori $2,$16,0
	addiu $29,$29,16
	jr $31
	
affichage :
#1 var locale et $31
addiu $29,$29,-8
sw $31,4($29)
sw $0,0($29) # j = 0
lw $8,0($29) # $8 <- j

ori $10,$4,0 # $10 <- tab

ori $9,$0,10

loop2:
	beq $9,$8,fin2 #j = 10
	
	ori $4,$8,0 # printf j
	ori $2,$0,1
	syscall
	
	ori $4,$0,0x3A # ":"
	ori $2,$0,11
	syscall
	
	sll $11,$8,2 # j*4
	addu $11,$10,$11 # $11 <- @tab[j]
	lw $12,0($11) # $12 <- tab[j]
	ori $4,$12,0 
	ori $2,$0,1 
	syscall
	
	ori $4,$0,0x3B # ";"
	ori $2,$0,11
	syscall
	
	addiu $8,$8,1
	
	j loop2
	
fin2 :
	ori $13,$0,0x6E5C # "\n"
	ori $4,$13,0
	ori $2,$0,4
	syscall
	addiu $29,$29,8
	jr $31
  
