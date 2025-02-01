import datetime
from random import randint
import time
import sqlite3
import math
import sys
from grove.adc import ADC
from gpiozero import Buzzer
from grove.grove_button import GroveButton

#lecture de données
class capteur_gazMQ2:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def MQ2(self):
        valeur = self.adc.read(self.channel)
        return valeur
          
Grove = capteur_gazMQ2
sensor = capteur_gazMQ2(0)
buzzer = Buzzer(12)
button = GroveButton(5)
 
def on_press(t):
    print('test')
    buzzer.off()
 
def main():
    button.on_press= on_press
    i = 0
    print('Detection...')
    while True:
        i = i + 1
        print ('concentration de gaz:{0} ppm'.format(sensor.MQ2))
        if sensor.MQ2 > 200 and i%2==0:
            buzzer.on()
        time.sleep(.3)
        


#Base de données 
sqlite_connexion= sqlite3.connect('db_gaz_4.db')
print('base créer')#test
curseur = sqlite_connexion.cursor()
print("Connecter à la base de donnée")#test
table= '''create TABLE donnees_gaz(donnees INTEGER ,
                                    heure DATETIME  AUTO_INCREMENT);'''
curseur.execute(table)
print('table créer')#test

def ajout_donnees(donnees):
     curseur.execute(f"INSERT INTO `donnees_gaz` (  `donnees`, 'heure') VALUES ( '{donnees}','{datetime.datetime.now()}')")


"""for i in range (10) :
    #test base de données avec un generateur de nombre
    donnees= randint(0,100)
    print (donnees)
    time.sleep(1)
ajout_donnees(donnees)"""

ajout_donnees(sensor.MQ2)#execution de la fonction
print('données ajoutées')#test


""""print('donnes ajouté')
result= 'SELECT * FROM donnees_gaz;'
a=curseur.execute(result)
for i in a :
    print(i)"""

curseur.close()
main()



 

