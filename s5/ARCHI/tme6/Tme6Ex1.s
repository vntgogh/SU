.data
ch : .space 11

.text
#char chaine[11]
lui $8,0x1001

#int i,nb,r,nbzero
addiu $29,$29,-16
sw $10,0($29) 	#écriture de i
sw $11,4($29) 	#écriture de nb
sw $12,8($29) 	#écriture de  r
sw $13,12($29) 	#écriture de  nbzero

#scanf("%d",&nb)
ori $2,$0,5
syscall
lw $2,4($29) 		#lecture de nb au clavier
 
#chaine[10]=0
sb $0,11($8)
 
lw $10,0($29) 	#lecture de i
addiu $10,$10,9 	#i = i+9
sw $10,0($29) 	#écriture de i

loop :
	 lw $10,0($29) 	#lecture de i
	 bltz $10, fin 		#si i<0, aller à fin
 	 
 	 #r = nb%10
	 addi $15,$0,10 	#$15 = 10
	 multu $11,$15 	#nb * 10
	 mfhi $14 		# r = nb % 10
	 sw $14,8($29)
	 lw $12,8($29)
	 
	 #nb = nb / 10
	 lw $11,4($29)
	 div $11,$15 
	 mflo $16
	 sw $16,4($29)
	 lw $11,4($29)
	 
	 #chaine[i] = r + 0x30
	 lw $10,0($29) 	#lecture de i 	 
	 add $8,$8,$10
	 lb $9,0($8)		#lecture de chaine[i]
	 addiu $9,$12,0x30
	  
	 #décrémenter i de 1
	 addi $10,$10,-1
	 addi $8,$8,-1
	  
	 j loop
 	 
fin :
	ori $4,$9,0
	ori $2,$0,1
	syscall
	addiu $29, $29,16 		#désallocation des variables locales
	ori $2,$0,10
	syscall


   
