#TP2 : Notions de base en Python

#Les variables

#Exercice 1 :
#1. 74.6
#2. Hello world !
#3. 98
#4. 2
#5. 26
#6. 12

#7. 11 
# Erreur de syntaxe. Correction : ma_variable /= 3

#8. Bonjour

#Les fonctions print() et input()

#Exercice 2 :
#prenom = input("Entrer votre prénom : ")
#print ("Bonjour", prenom, "!")

#Exercice 3 :
#1. 
#age = input("Saisir votre âge :")
#print(age + 2)
#Explication : On ne peut pas concatener une chaîne (str) avec une autre chose qu'une chaîne(pas un "int")

#2. 
#age = input("Saisir votre âge :")
#print(age + "2")
#Explication : le terminal affiche la donnée entrée par l'utilisateur + "2"

#3. 
#age = input("Saisir votre âge :")
#print(age * 2)
#Explication : le terminal affiche la donnée que l'utilisateur a saisis, deux fois et cote a cote

#Calculs et affichage
#Exercice 4 :
#annee_naissance = input("Saisir votre année de naissance : ")
#annee_actuelle = input("Saisir votre année de actuelle : ")
#ecart_annee = int(annee_actuelle) - int(annee_naissance)
#print("Cétait il y a", ecart_annee, "années.")
# J'AI BON, MAIS VOICI LA CORRECTION :
#annee_naissance = int(input("Saisir votre année de naissance : "))
#annee_actuelle = int(input("Saisir année actuelle : "))
#print("Cétait il y a", annee_actuelle - annee_naissance, "années. ")

#Exercice 5 :
#nbr_entier = input("Saisir un nombre entier : ")
#result = 2 ** int(nbr_entier)
#print("2 puissance", nbr_entier, "=", result)
# J'AI BON, MAIS VOICI LA CORRECTION :
#nombre = int(input("Saisir un nombre entier : "))
#print("2 puissance", nombre, "=", 2**nombre)

#Exercice 6 :
#longueur = input("Saisir la longueur du côté : ")
#air = int(longueur) * int(longueur)
#perimetre = int(longueur) * 4
#print("Un carré de", longueur,"cm de côté a pour périmètre", perimetre, "cm et pour #aire", air, "cm².")
# J'AI BON, MAIS VOICI LA CORRECTION :
#cote = float(input("Saisir la longueur du côté : "))
#print("Un carré de", cote,"cm de côté a pour périmètre",cote*4,"cm et pour
#aire",cote*cote,"cm².")

#Les types de données

#Exercice 7 :
#a = 2 #int
#a = 2.0 #float
#a =3+1 #int
#a = 2.2 + 4 #float
#a = "Bonjour" #str
#a = False #bool
#a = "2>3" #str
#a = 2>3 #bool
#a = [4,6] #list
#a = (8,14) #tuple
#a = {4 : 5,6 : 3} #dict
#print(type(a))

#Exercice 8 :
#1.
#print(str(5.4) * 3)
#Explication : le terminal affiche la donnée que l'utilisateur a saisis, trois fois et cote a cote
#CORRECTION :
# Sortie : 5.45.45.4

#2.
#print(int("8") + float("9.8"))
#print(type(int("8")))
#print(type(float("9.8")))
#Explication : Le résultat afficher est celui d'un int (entier) additionner à un float (flottant)
#CORRECTION :
# Sortie : 17.8

#3.
#print(str(5) * int(7.6))
#Explication : Cela affiche 7 fois la chaine de caractere 5
#CORRECTION :
# Sortie : 5555555

#4.
#print(str(6) * float("4.8"))
#Explication : Cela affiche un message d'erreur qui nous dis que l'on ne peut pas multiplier un str (chaine de caractere) à un float (un nombre flottant)

#Exercice 9 :
#1. 
#test_list = []
#print(len(test_list))
# Résultat : 0

#2. 
#test_list = [1, 2, 3]
#print(len(test_list))
# Résultat : 3

#3. 
#test_tuple = (1, 2, 3)
#print(len(test_tuple))
# Résultat : 3

#4. 
#test_range = range(1, 10)
#print(len(test_range))
# Résultat : 9

#5. 
#test_string = "Bonjour"
#print(len(test_string))
# Résultat : 7

#6. 
#test_int = 6
#print(len(test_int))
# Résultat : 
#TypeError: object of type 'int' has lo len()

#7. 
#test_float = 54.26
#print(len(test_float))
# Résultat : TypeError: object of type 'float' has no len(). C'est à dire que ma fonction len ne peu pas afficher la taille d'un nombre floattant

#Donner une définition de la fonction len()
#La fonction len donne le nombre de caractère d'une chaine de caractere
#CORRECTION :
#Ainsi que le nombre d'éléments dans une list, un tuple ou un dict

#Bilan

#Exercice 10 :
'''
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
age_futur = age + 5
taille = int(input("Entrez votre taille en cm : "))
taille_metre = taille / 100
print("Bonjour", prenom, "!")
print("Dans 5 ans vous aurez", age_futur,"ans.")
print("Votre taille est de", taille_metre, "mètres.")
'''

#Exercice 11 :
'''
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
phrase_1 = "Bienvenue en SLAM,"
phrase_2 = str(prenom)
phrase_3 = str(nom)
taille_phrase = len(phrase_1 + phrase_2 + phrase_3) + 4
barriere = ("=" * taille_phrase)
print(barriere)
print(phrase_1, phrase_2, phrase_3, "!")
print(barriere)
'''
# J'AI BON, MAIS VOICI LA CORRECTION :
'''
# Saisie des données
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
# Construction du message
message = "Bienvenue en SLAM, " + prenom + " " + nom + " !"
# Ligne de séparation de même longueur que le message
ligne = "=" * len(message)
# Affichage
print(ligne)
print(message)
print(ligne)
'''