.data
n : .word -1
.text

lui $8,0x1001
lw $9,0($8) #lecture de n

xor $11,$11,$11 #compteur

loop :
	beq $9,$0,fin
	
	andi $12,$9,1 	#masque
	bne $12,$0,iter	
	
	srl $9,$9,1		
	
	j loop	
	
iter :
	addiu $11,$11,1 
	srl $9,$9,1
	j loop

fin :
	ori $4,$11,0
	ori $2,$0,1
	syscall
	ori $2,$0,10
	syscall
	
	