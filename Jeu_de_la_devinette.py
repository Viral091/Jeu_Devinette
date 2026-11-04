from random import *

#Jeu de la devinette, on choisit un chiffre entre 1 et 100 et on demande à l'utilisateur de le deviner
#boucle while on demande jusqu'a ce que le joueur trouve le chiffre il a 10 essais ou perdu
#chaque itération de la boucle on dit plus petit ou plus grand


nombre_a_deviner = randint(1, 100) 
nombre_essais = 10 
a=int(input("Devinez le chiffre entre 1 et 100: ")) 

while a!=nombre_a_deviner and nombre_essais>0: 
    if a>nombre_a_deviner: 
        print("C'est plus petit que ",a)
    elif a<nombre_a_deviner: 
        print("C'est plus grand que",a)
    nombre_essais= nombre_essais-1 
    print("Vous avez encore",nombre_essais,"d'éssais.") 
    a=int(input("Vous n'avez pas eu le bon chiffre, réessayez: ")) 

if a==nombre_a_deviner:
    nombre_essais=nombre_essais-1
    print("Vous avez reussi à trouver le chiffre",nombre_a_deviner,"! Il vous réstait",nombre_essais,"d'éssais!")

elif nombre_essais==0:
    print("Vous avez perdu, vous n'avez plus d'éssais, le chiffre était",nombre_a_deviner) 








