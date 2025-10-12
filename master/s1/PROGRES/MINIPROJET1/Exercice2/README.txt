Présentation du projet :
Ce projet met en oeuvre différents types de relais TCP et HTTP. L’objectif est d'insérer un ou plusieurs relais entre le client et le serveur.
On expériencera ici 3 types de relais :
- Un relai qui stocke les URI des clients et les réponses du serveur dans un cache HTTP (cache)
- Un relai qui stocke les requêtes et réponses suivies de l'adresse client ayant fait la requête et de l'adresse client ayant reçu une réponse non vide (sniffeur)
- Un relai qui censure l’accès à des sites interdits et sauvegarde l’adresse du client dans un log (censeur)

Voici la liste des fichiers et leurs rôles :
Client.py	    : client qui envoie une requête au relai (bonjour.txt)
Client2.py	    : variante du client qui envoie une requête différente (aurevoir.txt)
Client3.py	    : variante du client qui teste l’accès à un fichier interdit (interdit2.txt)
Serveur.py	    : serveur TCP/HTTP qui répond aux requêtes du relai
RelaiCache.py	: relai qui stocke les URI des clients et les réponses du serveur dans deux listes et qui répond directement au client s'il possède déjà la réponse de l'URI
RelaiSniffer.py	: relai qui stocke (dans sniffer.log) toutes les URI demandées et clients associés et renvoie les adresses client qui ont obtenu une réponse concernant une URI donnée
RelaiCenseur.py	: relai qui bloque l’accès à certains sites interdits (interdit1, interdit2) et qui stocke (dans interdit.log) toute adresse client qui tente d'accéder à l'un de ces sites
bonjour.txt	    : fichier autorisé à consulter
aurevoir.txt	: fichier autorisé à consulter
interdit1.txt	: fichier interdit de consulter
interdit2.txt	: fichier interdit de consulter
interdit.log	: log des adresses clients ayant tenté d'accéder à un site interdit
sniffer.log	    : log des URI consultées avec adresse client associée (Format : "URI : Adresse Client")

Fonctionnement :
Un client envoie une requête de lecture de fichier par l'intermédiaire d'un ou de plusieurs relais.
Le serveur lit et renvoie le contenu des fichiers demandés, ou retourne une erreur HTTP si le fichier n'a pas été trouvé.
Les relais, ainsi que le serveur, traitent les connexions en parallèle avec multithreading.
On peut connecter les entités de la manière suivante : client -> cache -> censeur -> log -> serveur.

Pour lancer l'exécution des fichiers :
- on lance le serveur sur le port 1234
- on lance un relai avec l’IP et le port du serveur
- on lance un client avec l'IP et le port du relai