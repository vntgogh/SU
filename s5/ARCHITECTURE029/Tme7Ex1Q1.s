.data
ch1 : .asciiz "1 exemple d'exemple\n"

.text
	lui $8,0x1001
	lw $9,0($8)
	
	#int i = 0
	addiu $29,$29,-4
	sw $0,0($29)
	lw $7,0($29)

	loop :
	#ch[i] != '\0'
	addu $9,$8,$7 #@ch[i]
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
	
	#i++
	addiu $7,$7,1
	j loop
	
	iter :
	addiu $7,$7,1
	j loop

	fin :
	#printf("%s", ch)
	addiu $29,$29,4
	ori $4,$8,0
	ori $2,$0,4
	syscall
	
	ori $2,$0,10
	syscall

