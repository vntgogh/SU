.data
tab : .byte 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x00

.text
lui $8,0x1001 
ori $4,$8,0
ori $2,$0,4
syscall

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall

lb $16,2($8) #met le 3ème élément dans $16
ori $4,$16,0
ori $2,$0,1
syscall

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall

ori $18,$0,48

sub $17,$16,$18 #enleve 48 au code ascii -> renvoie le chiffre en decimal
ori $4,$17,0 
ori $2,$0,1
syscall

ori $19,$0,0x34
sub $17,$19,$18 #enleve 48 au code ascii -> renvoie le chiffre en decimal

ori $4, $0, 0x0A
ori $2, $0, 11 #retour à la ligne
syscall
ori $4,$17,0 
ori $2,$0,1
syscall



ori $2,$0,10
syscall
