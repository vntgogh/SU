.data

tab : .word 4,3,7,2,1024,6,1

.text

lui $8,0x1001

xor $10,$10,$10 #max=0

loop :	
	lw $9,0($8) #lit le premier entier de tab

	beq $9,$0,fin #si c'est l'entier nul, aller à fin
	
	addiu $8,$8,4 #incrémenter l'indice du tableau
	
	slt $11,$9,$10 #si tab[i] < max, $11 = 1
	
	beq $11,$0,then 
	
	j loop
	
then :
	ori $10,$9,0 #max = tabi]
	
	j loop
	
fin :
	ori $4,$10,0
	ori $2,$0,1
	syscall
	ori $2,$0,10
	syscall
	
