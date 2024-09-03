import time

terminal_launched = True
terminal_name = "Défaut"
user_command = ""

while terminal_launched :
    user_command = input(f"[{terminal_name}] > ")
    if user_command == "run":
        for i in range(0,5,1):
            print(".")
            time.sleep(1)
    elif user_command == "name":
        terminal_name = input("Choisir le nouveau nom du terminal : ")
    elif user_command == "help":
        print("LISTE DES COMMANDES\n\
run : exécute la boucle 5 fois\n\
name : modifie le nom du terminal\n\
help : affiche la liste des commandes\n\
quit : quitte le programme\n")
    elif user_command == "quit":
        terminal_launched = False
    else : 
        print("Commande introuvable !")