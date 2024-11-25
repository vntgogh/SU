.data
ph : .space 256

.text
lui $10,0x1001
ori $2,$0,8
or $4,$0,$10
ori $5,$0,256
syscall

ori $8,$0,0x20
ori $9,$0,0x2E
xor $15,$15,$15

loop :
	lbu $16,0($10)
	beq $16,$8,espace
	beq $16,$9,point

cpt : 
	addiu $10,$10,1
	j loop

espace :
	addiu $15,$15,1
	j cpt

point :
	addiu $15,$15,1
	j end
	
end :
	ori $2,$0,1
	xor $4,$4,$4
	or $4,$0,$15
	syscall