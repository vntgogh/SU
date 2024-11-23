.data
.word 0x10010004
.byte 0x33,0x32
.half 0x0031
.ascii "ÝÌ»?"
.asciiz "ÿÿÿ"
.word 0xBA439821
.word 0,0

.text
lui $7,0x1001
lhu $8,16($7)
lh $9,18($7)

srl $11,$9,8
sll $11,$11,24
sll $12,$9,24
srl $12,$12,16
srl $13,$8,8
sll $13,$13,16
sll $14,$8,24
srl $14,$14,24
or $15,$11,$12
or $16,$13,$14
or $10,$15,$16

#autre solution 

andi $11,$8,0x0000FF00 #isoler 98
sll $11,$11,8

andi $12,$8,0xFF #isoler 21

andi $13,$9,0x0000FF00 #isoler BA
sll $13,$13,16

andi $14,$9,0xFF #isoler 43
sll $14,$14,8

or $15,$11,$12 #0x00980021
or $16,$13,$14 #0xBA004300
or $10,$15,$16 #0xBA984321
