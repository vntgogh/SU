.data
ch1 : .asciiz "1 exemple d'exemple\n"
ch2 : .asciiz "hello world"

.text

main :

#printf("%s", ch1);
lui $8,0x1001
ori $4,$8,0
ori $2,$0,4
syscall

lui $4,0x1001
ori $4,$4,0

jal min_to_maj

ori $4, $16, 0 
ori $2,$0,4
syscall

#printf("%s", ch2)
lui $8,0x1001
ori $4,$8,0x0015
ori $2,$0,4
syscall

lui $4, 0x1001
ori $4, $4, 0x0015

jal min_to_maj

ori $4, $16, 0 
ori $2,$0,4
syscall

ori $2,$0,10
syscall


min_to_maj :
	#contexte pile : 1 variable locale + 1 octet pr sauvegarder $31
	#int i = 0
	addiu $29,$29,-8
	sw $31, 4($29) #@ de retour
	add $16, $4,$0
	sw $0,0($29) 

	loop :
	#ch[i] != '\0'
	addu $9,$4,$7 #@ch[i]
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
	addiu $7,$7,1
	sw $7,0($29)
	j loop

	fin :
	
	addu $16,$4,$0
	lw $31,4($29)
	addiu $29,$29,8
	jr $31
