Fichier README
pour le code principal :
Bibliothèques pour la base de données : datetime, sqlite3
Bibliothèques pour le capteur MQ2 : sys, ADC

La fonction MQ2() lit les valeurs du capteur de gaz. (ligne 17)

Les lignes 22 et 23 définissent les ports du buzzer et du bouton.

La fonction on_press(t) (ligne 26) provient du code de la bibliothèque grove; 
elle permet de mettre en pause le buzzer lorsque le bouton est pressé.

La fonction main() (ligne 30) affiche les valeurs du capteur et fait sonner le buzzer lorsque ces valeurs dépassent les 200 ppm.
L'indice i permet de faire sonner le buzzer par intermittence. Autrement dit, il sonne uniquement lorsque i est pair.

toutes lignes à partir de la ligne 40 concerne la création de la base de données et sa gestion. 



La fonction ajout_donnees(donnees) (ligne 50) permet de créer une requête pour chaque nouvelle valeur du capteur. 


N.B : la boucle en commentaire  """ """ (ligne 52) est une fonction qui génère des nombres aléatoires et
 remplace le code et est utilisé pour remplir la base de donnée en cas de panne du capteur de gaz .


pour le code html:
toute les pages html represente un site vitrine qui est un prototype de l'application qui pourrait être utilisé dans le cadre de la partie interaction humain machine. 