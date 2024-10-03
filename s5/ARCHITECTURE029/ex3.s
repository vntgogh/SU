.data
.text
ori $9,$0,84
ori $10,$0,10
div $9,$10
mflo $11
mfhi $12

ori $2,$0,1
syscall
ori $4,$0,84
ori $4,$0,10

mult $11,$10
mflo $16
mfhi $17
add $14,$16,$17
add $13,$12,$14

ori $2,$0,1
ori $4,$13,0
syscall

ori $2,$0,10
syscall
