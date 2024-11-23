.data
ch : .asciiz "1234"
.text
addiu $29,$29,-12 	#i=4octets,val=4octets,c=1+3octets de padding

sw $0,0($29) 	#écriture de i
sw $0,4(29) 		#écriture de val

loop :
	#ch[i] != 0
	lw $8,0($29) 		#lecture de i
	lui $9,0x1001 
	addu $9,$8,$9 	#$9=adresse de ch[i]
	lbu $10,0($9)
	beq $10,$0,fin 	#si @ch[i]=0, aller à fin
	
	#écriture de ch[i] dans c
	lw $8,0($29) 		#lecture de i
	lui $9,0x1001
	addu $9,$9,$8
	lbu $10, 0($9) 	#lbu charge 0x000000B1 alors que lb charge 0xFFFFFFB1
	sb $10,8($29) 	#c = ch[i]
	
	#c = c & 0x0F
	lbu  $9,8($29) 	#lecture de c
	andi $9,$9,0x0F	#récupère la valeur du chiffre(ascii vers int)
	sw $9,8($29) 	#écriture de c
	
	#val = val * 10 + c
	lw $8,4($29) 		#lecture de val
	ori $9,$0,10 		#$9 = 10
	multu $8,$9 		#val * 10
	mflo $10 
	lbu $11,8($29) 	#lecture de c
	addu $10, $10,$11 	#val * 10 + c
	sw $10,4($29) 	#val = val * 10 + c
	
	#i = i + 1
	lw $8,0($29) #lecture de i 
	addiu $8,$8,1 #i = i + 1
	sw $8,0($29) #écriture de i
	
	j loop
	
fin :
	lw $4,4($29) #affichage de val
	ori $2,$0,1
	syscall
	
	addiu $29,$29,$12 #désallocation des 12 octets
	ori $2,$0,1
	syscall
	
	
	
	

