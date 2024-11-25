.data
ch1: .asciiz "1 exemple d'exemple\n"
ch2: .asciiz "hello world"

.text
main:
    # Obtenir l'adresse de ch1 et la stocker dans $16
    jal get_ch1_address
    move $16, $4      # Stocker l'adresse de ch1 dans un registre persistant

    # Obtenir l'adresse de ch2 et la stocker dans $17
    jal get_ch2_address
    move $17, $4      # Stocker l'adresse de ch2 dans un autre registre persistant

    # Afficher ch1
    move $4, $16      # Charger l'adresse de ch1 dans $4
    ori $2, $0, 4
    syscall

    # Appeler la fonction min_to_maj pour transformer ch1
    jal min_to_maj

    # Afficher ch1 transformé
    move $4, $16
    ori $2, $0, 4
    syscall

    # Afficher ch2
    move $4, $17      # Charger l'adresse de ch2 dans $4
    ori $2, $0, 4
    syscall

    # Appeler la fonction min_to_maj pour transformer ch2
    jal min_to_maj

    # Afficher ch2 transformé
    move $4, $17
    ori $2, $0, 4
    syscall

    # Sortie du programme
    ori $2, $0, 10
    syscall

# Fonction pour obtenir l'adresse de ch1
get_ch1_address:
    la $4, ch1        # Charger l'adresse de ch1 dans $4
    jr $31            # Retour

# Fonction pour obtenir l'adresse de ch2
get_ch2_address:
    la $4, ch2        # Charger l'adresse de ch2 dans $4
    jr $31            # Retour

min_to_maj:
    # Contexte de pile pour sauvegarder $31 et i
    addiu $29, $29, -8
    sw $31, 4($29)    # Sauvegarder l'adresse de retour
    sw $0, 0($29)     # Initialiser i = 0

    loop:
        # Charger ch[i] dans $10
        lw $7, 0($29)           # Récupérer i
        addu $9, $4, $7         # Adresse de ch[i]
        lbu $10, 0($9)          # Charger ch[i]
        beq $10, $0, fin        # Si ch[i] == '\0', fin

        # Si ch[i] est une minuscule, transformer en majuscule
        addiu $11, $0, 0x61     # 'a'
        addiu $12, $0, 0x7A     # 'z'
        slt $13, $10, $11       # ch[i] < 'a'
        bne $13, $0, iter
        slt $14, $12, $10       # ch[i] > 'z'
        bne $14, $0, iter

        # Transformer ch[i] en majuscule
        addiu $15, $0, 0x20
        sub $10, $10, $15       # ch[i] = ch[i] - 0x20
        sb $10, 0($9)           # Stocker ch[i] transformé

    iter:
        # i++
        addiu $7, $7, 1
        sw $7, 0($29)
        j loop

    fin:
        # Restauration de l'environnement de pile
        lw $31, 4($29)
        addiu $29, $29, 8
        jr $31
