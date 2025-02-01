.data
ch1 : .asciiz "1 exemple d'exemple\n"

.text

main :
#contexte pile : 1 paramètre + @ de retour
addiu $29,$29,-5

loop :
	beq $9,$0,fin
sw $31,4($29)
sw $4,0($29)

ori $2,$0,11
syscall

fin :
	addiu $29,$29,5
	ori $2,$0,10
	syscall


min_to_maj :
	#contexte pile : 1 variable locale + 1 octet pr sauvegarder $31
	addiu $29,$29,-8
	sw $31,4($29) #@ de retour
	#int i = 0
	sw $0,0($29) 

	loop :
	#ch[i] != '\0'
	lw $8,0($29)
	addu $9,$4,$8 #@ch[i]
	lbu $10,0($9)   #ch[i]
	beq $10,$0,fin
	
	#if (ch[i] >= 'a' && ch[i] <= 'z')
	addiu $11,$0,0x61
	addiu $12,$0,0x7A
	slt $13,$10,$11    #ch[i] < 'a' = 1 si vrai 0 sinon
	bne $13,$0,iter
	slt $14,$12,$10    #ch[i] > 'z' = 1
	bne $14,$0, iter
	
	#ch[i] = ch[i] - 0x20
	addiu $15,$0,0x20
	sub $10,$10,$15	#ch[i] = ch[i] - 0x20
	sb $10,0($9)		#écriture de ch[i] dans @ch[i]
	
	iter :
	#i++
	addiu $8,$8,1
	sw $8,0($29)
	j loop

	fin :
	
	lw $31,4($29)
	addiu $29,$29,8
	jr $31
