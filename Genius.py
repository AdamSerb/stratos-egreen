

import math
print('Yo! Ce programme va vous aider a realiser vos devoirs en Physique/Maths.')
Subject = input("Selectionnez votre matiere: ")
if Subject == "maths" or Subject == "physique":
    print("D'accord vous avez choisi", Subject)
else:
    print("Vous devez selectionner une matiere !")
if Subject == "maths":
    Sujet = input("Que voulez vous calculer? ")
    #Equation: int = 1
    #Surface: int = 2
    if Sujet == '1':
        print("Saisir les informations suivantes: ")
        a =int(input("enter a: "))
        b =int(input("enter b: "))
        c =int(input("enter c: "))
        Delta = b**2 - 4*a*c
        if Delta > 0:
            S1: float = (-b + math.sqrt(Delta))/(2*a)
            S2: float = (-b - math.sqrt(Delta))/(2*a)
            print('Le resultat de votre equation est: S1=', S1 )
            print('Le resultat de votre equation est: S2=', S2 )
        elif Delta == 0:
            S3: float = (-b)/(2*a)
            print('Le resultat de votre equation est: ', S3)
        else:
            print('S est un ensemble vide')

    if Sujet == '2':
        from math import pi
        area = input('Quelle est la surface que vous souhaitez calculer: carre/disc/triangle): ')

        if area == 'carre':
            print("entrer les informations suivantes: ")
            R = int(input('longueur: ')) * int(input('largeur: '))
            print(R)

        elif area == 'triangle':
            print("entrer les informations suivantes: ")
            R = int(input('hauteur: ')) * int(input('base: ')) * 1 / 2
            print(R)
        elif area == 'disc':
            print("entrer les informations suivantes: ")
            R = (int(input('radius: ')) ** 2 * pi)
            print(R)
        else:
            print("verifier les renseignements")
