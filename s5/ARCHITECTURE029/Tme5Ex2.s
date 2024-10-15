.data
a : .space 4
b : .space 4

.text 

lui $8,0x1001 #ecrire a au clavier
ori $2,$0,5
syscall
sw $2,0($8)

lui $8,0x1001 #ecrire b au clavier
ori $2,$0,5
syscall
sw $2,4($8)

lw $9,4($8) #charger b
lw $8,0($8) #charger a

beq $8,$9,fin #si a=b, aller à fin

loop : 
	beq $8,$9,fin #si a=b, aller à fin
	slt  $10,$9,$8 #si a>b, $10=1
	beq $0,$10,else #sinon, aller à else
	
	sub $8,$8,$9 #a=a-b
	
	j loop
	
	else : #si a<b
		sub $9,$9,$8 #b=b-a
		
		j loop
fin :
	ori $4,$8,0 #afficher a
	ori $2,$0,1
	syscall	
	
	ori $2,$0,10
	syscall