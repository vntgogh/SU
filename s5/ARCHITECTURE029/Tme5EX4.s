.data

val : .word 4
tab : .word 1,2,3,4,5,-1

.text

lui $8,0x1001
lw $9,0($8) #lecture de val
lw $10,4($8) #lecture de tab
addi $8,$8,4

loop :
	lw $10,4($8) 
	
	bltz $10, fin 
	
	slt $12, $9, $10 #si tab[i]>val alors $12 = 1, 0 sinon
	
	bne $0,$12, then 
	
	addi $11,$11,1 #incrémenter le compteur
		
	addi $8,$8,4 #passer à l'élément suivant
	
	j loop
	
then :
	addi $8,$8,4 #passer à l'élément suivant
	
	j loop
	
fin :
	ori $4,$11,0
	ori $2,$0,1
	syscall
	ori $2,$0,10
	syscall
