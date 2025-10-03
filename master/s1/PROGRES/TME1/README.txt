Dans ce répertoire, chaque exercice possède son propre sous-répertoire.

Exercice 1 : le serveur renvoie le message du client en majuscules.
Exercice 2 : le client calcule la diiférence entre son heure actuelle et celle du serveur.
Exercice 3 : le serveur envoie au client le fichier demandé.

Exercice 1 - Client / Serveur UDP

serveur.py :
- attend et transforme les messages en majuscules et les renvoie au client

client.py :
- envoie plusieurs messages au serveur et calcule la moyenne des temps de requête + réception (RTT)
- affiche chaque message en majuscules et le temps aller-retour du message 
- calcule la moyenne des temps aller-retour de tous les messages

Question 4 : Que se passe-t-il?
    Le client ne passera pas à la requête suivante tant que le serveur n'aura pas reçu une réponse 
pour la i-ème requête. Il va donc renvoyer la même requête au serveur un nombre limité de fois puis,
passera, à la (i+1)ème requête. Si, la limite de tentatives est dépassée, le client arrête de renvoyer 
la même requête au serveur car ce dernier est possiblement "éteint".


Exercice 2 - Client / Serveur TCP

serveur.py :
- reçoit l'heure du client en secondes
- renvoie l’heure du serveur avec la fonction pack()

client.py :
- envoie l’heure du client avec la fonction pack()
- reçoit l’heure du serveur
- calcule et affiche la différence entre l’heure du client et du serveur (avec unpack())


Exercice 3 - Serveur Web avec TCP

serveur.py :
- écoute plusieurs clients en même temps (multithreading)
- extrait le chemin vers le fichier demandé dans la requête HTTP avec pathlib et split()
- vérifie si le fichier existe (is_file), lit son contenu (get_txt) puis l'envoie au client (put_block)
- affiche '404 Not Found', sinon

client.py :
- demande un fichier .txt au serveur
- reçoit et affiche la réponse du serveur
- utilise la fonction put_block pour envoyer, au serveur, la taille du message suivi du message 
- utilise get_block pour récupérer la taille de la réponse et recevoir toute la réponse avec recvall

