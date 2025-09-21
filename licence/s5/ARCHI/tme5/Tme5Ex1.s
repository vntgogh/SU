.data
p : .space 4
q : .space 4

.text

lui $8,0x1001 #ecrire p au clavier
ori $2,$0,5
syscall
sw $2,0($8)

lui $8,0x1001 #ecrire q au clavier
ori $2,$0,5
syscall
sw $2,4($8)

lw $9,4($8) #charger q
lw $8,0($8) #charger p

xor $10,$10,$10 #initialiser la somme à 0

beq $8,$9,else #si p=q, aller à else

slt $11,$9,$8 #si q<p, $11=1, 0 sinon
bne $0,$11,else #si q<p, aller à else

add $10,$10,$8

loop :		
	beq $8,$9,fin
	
	addi $8,$8,1
	
	add $10,$10,$8

	j loop
	
else : #si p=q
	xor $10,$10,$10 #somme = 0
	
fin :
	ori $4,$10,0
	ori $2,$0,1
	syscall	
	ori $2,$0,10
	syscall
