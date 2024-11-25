.data
user_num : .space 4
tab_chiffre : .space 40

.text
 main :
 addiu $29,$29,-12 #2param + 1variable locale

 ori $2,$0,5
 syscall
 ori $4,$2,0
 
 lui $3,0x1001
 sw $4,0($3)
 addiu $5,$3,4
 sw $5,4($29)
 
 jal occ_num_chiffre
 
 sw $16,8($29) # num_ch = occ_num_chiffre
 
 ori $4,$16,0
 ori $2,$0,1
 syscall
 
 addiu $29,$29,12
 ori $2,$0,10
 syscall
 
 occ_num_chiffre :
 addiu $29,$29,-16
 sw $31,12($29)
 ori $16,$0,1
 sw $16,0($29) #nb_c=1
 sw $4,4($29) #q=n
 
 lw $9,4($29)
 ori $10,$0,10
 
 loop :
 	slt $11,$9,$10 #q < 10
 	bne $11,$0,fin
 	
 	div $9,$10
 	mfhi $12 #r = q % 10
 	sw $12,8($29)
 	
 	mflo $9 # q = q/10
 	
 	sll $13,$12,2 #r*4
 	addu $13,$5,$13 # $14 <- @tab+r*4
 	
 	lw $14,0($13)
 	addiu $14,$14,1 #tab[r]+=1
 	sw $14,0($13)
 	
 	addiu $16,$16,1
 	
 	j loop
 
 fin :
 	sll $13,$9,2
 	addu $13,$5,$13 # $14 <- @tab+q*4
 	lw $14,0($13)
 	addiu $14,$14,1 #tab[q]+=1
 	sw $14,0($13)
 	addiu $29,$29,16
 	jr $31