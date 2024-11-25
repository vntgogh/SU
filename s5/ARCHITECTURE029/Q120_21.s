.data 
s : .space 20
ch_ok : .asciiz "bien parenthésé\n"
ch_nok : .asciiz "mal parenthésé\n"

.text
main :
#contexte pile : 1 parametre + 1 variable locale 
addiu $29,$29,-8
lui $3,0x1001
ori $4,$3,0
ori $5,$0,20

ori $2,$0,8 #scanf("%20s", s)
syscall
ori $2,$0,4 #printf("%s", s)
syscall

#sw $4,4($29) 
jal bon_parenthesage 

sw $16,0($29) #ok = bon_parenthesage(s)

beq $16,$0,pch_ok

lui $3,0x1001
ori $4,$3,37
ori $2,$0,4 #printf("%s",ch_nok)
syscall
j fin_main

pch_ok : 
	lui $3,0x1001
	addiu $4,$3,20
	ori $2,$0,4 #printf("%s", ch_ok)
	syscall

fin_main :
	addiu $29,$29,8
	ori $2,$0,10 #exit()
	syscall

bon_parenthesage :
#contexte pile : 2var locales + @ de retour
addiu $29,$29,-12
sw $31,8($29)
sw $0,0($29) #d=0
sw $0,4($29) #i=0

lw $11,4($29) # $11 <- i

loop :
	addu $10,$4,$11 # $10 <- @s[i]
	lb $12,0($10) # $12 <- s[i]
	beq $12,$0,fin #ch[i] == ’\0’
	
	ori $13,$0,0x28 # '('
	ori $14,$0,0x29 #')'
	
	beq $12,$13,incr_d #ch[i] == ’('
	
	beq $12,$14,decr_d #ch[i] == ’)’
	
	j comp_d
	
incr_d :
	lw $16,0($29)
	addiu $16,$16,1
	sw $16,0($29)
	j comp_d
	
decr_d :
	lw $16,0($29)
	addiu $16,$16,-1
	sw $16,0($29)
	j comp_d

comp_d :
	lw $16,0($29)
	bltz $16,fin #d < 0
	j incr_i
	
incr_i :
	addiu $11,$11,1 #i++
	j loop
	
fin :	
	lw $16,0($29)
	addiu $29,$29,12
	jr $31


