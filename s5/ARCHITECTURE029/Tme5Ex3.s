.data
ch : .asciiz "yanislpb"

.text
lui $8,0x1001

xor $10,$10,$10 #compteur pour la taille de ch

loop :
	
	lb $9,0($8) #charger le premier caract�re de la chaine
	
	beq $9,$0,fin #si le caract�re est nul, aller � fin
	
	addi $10,$10,1 #incrementer le compteur
	
	addi $8,$8,1 # Supprimer la premier caract�re=premier octet
	
	j loop

fin :
	ori $4,$10,0 #affichage de la taille
	ori $2,$0,1
	syscall	
	
	ori $2,$0,10
	syscall
