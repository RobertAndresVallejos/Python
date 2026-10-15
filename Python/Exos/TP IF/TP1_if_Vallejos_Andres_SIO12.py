#Structures alternatives

#Code PIN
'''
code = int(input("Entrer le code PIN : "))
if code == 4567:
    print("code correct")
else:
    print("code incorrect")
'''

#Signe d’un nombre
'''
nbr = int(input("Saisir un nombre entier : "))
if nbr > 0:
    print("Positif")
elif nbr == 0:
    print("Nul")
else:
    print("Négatif")
'''

#Parité
'''
nbr = int(input("Saisir un nombre entier : "))
if nbr % 2 == 0:
    print(nbr, "est un nombre pair")
else:
    print(nbr, "est un nombre impair")
'''

#Age
'''
age = int(input("Entrer votre âge : "))
if age < 12:
    print("A", age, "ans, vous êtes un enfant.")
elif age >= 12 and age <18:
    print("A", age, "ans, vous êtes un adolescent.")
else:
    print("A", age, "ans, vous êtes un adulte.")
'''

#Perte ou profit
'''
prix_fabrication = float(input("Prix de fabrication : "))
prix_vente = float(input("Prix de vente : "))
if prix_fabrication > prix_vente:
    print("perte")
else:
    print("profit")
'''

#Maximum
'''
nbr_1 = float(input("Saisir le premier nombre : "))
nbr_2 = float(input("Saisir le second nombre : "))
nbr_3 = float(input("Saisir le troisième nombre : "))
if nbr_1 > nbr_2 and nbr_1 > nbr_3:
    print("Le maximum est le premier nombre", nbr_1)
elif nbr_2 > nbr_1 and nbr_2 > nbr_3:
    print("Le maximum est le second nombre", nbr_2)
else:
    print("Le maximum est le troisième nombre", nbr_3)
'''

#Triangle rectangle
'''
cote_a = int(input("côté a : "))
cote_b = int(input("côté b : "))
cote_c = int(input("côté c : "))
cote_a_carre = cote_a ** 2
cote_b_carre = cote_b ** 2
cote_c_carre = cote_c ** 2

if cote_a < cote_b and cote_a < cote_c:
    if cote_c_carre == cote_b_carre + cote_a_carre:
        print("triangle rectangle")
    else:
        print("triangle non rectangle")
else:
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")
'''