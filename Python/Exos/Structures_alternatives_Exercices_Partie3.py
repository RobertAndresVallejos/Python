# Natation
'''
nbr_seance = int(input("Nombre de séances : "))
tarif_annuel = 145
total_tarif_annuel = 145 + (nbr_seance * 10.50)
tarif_sans_abbonement = 15.50
total_tarif_sans_abbonement = tarif_sans_abbonement * nbr_seance

if(total_tarif_sans_abbonement < total_tarif_annuel):
    print("Pour", nbr_seance, "séances, le tarif B est le plus avantageux.")
elif total_tarif_annuel < total_tarif_sans_abbonement:
    print("Pour", nbr_seance, "séances, le tarif A est le plus avantageux.")
else:
    print("Pour", nbr_seance, "séances, aucun tarif n'est plus avantageux que l'autre.")

details = input("Souhaitez-vous plus de détails? : ")
if details == "yes":
    print("Tarif A :", total_tarif_annuel, "euros")
    print("Tarif B :", total_tarif_sans_abbonement, "euros")
'''

#Voyelle, consonne ou caractère spécial
'''
voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
consonnes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
caractere = str(input("Saisir un caractère : "))
if caractere in consonnes:
    print(caractere, ": consonne")
elif caractere in voyelles:
    print(caractere, ": voyelle")
else:
    print(caractere, ": caractère spécial")
'''

#Facture
'''
HT = float(input("Saisir le prix hors taxe : "))
TVA = 19.6
TTC = HT * (1 + TVA / 100)

print("Prix HT : ", HT, "euros")
print("Prix TTC : ", round(TTC, 2), "euros")

if TTC < 1000:
    remise = 0
elif TTC >= 1000 and TTC < 2000:
    remise = TTC * 1 / 100
elif TTC >= 2000 and TTC < 5000:
    remise = TTC * 3 / 100
else:
    remise = TTC * 5 / 100

print("Remise : ", round(remise, 2), "euros")
NetAPayer = TTC - remise
print("Prix Net à payer : ", round(NetAPayer, 2), "euros")
'''

#Calculatrice
'''
nbr_1 = float(input("Entrez le premier nombre : "))
nbr_2 = float(input("Entrez le deuxième nombre : "))
operation = str(input("Entrez l'opération (addition, soustraction, multiplication, division) : "))
if nbr_2 == 0 and operation == "division":
    print("Erreur : Division par zéro !")
elif operation == "addition":
    total = nbr_1 + nbr_2
    print("     >", nbr_1, "+", nbr_2, "=", total)
elif operation == "soustraction":
    total = nbr_1 - nbr_2
    print("     >", nbr_1, "-", nbr_2, "=", total)
elif operation == "multiplication":
    total = nbr_1 * nbr_2
    print("     >", nbr_1, "*", nbr_2, "=", total)
elif operation == "division":
    total = nbr_1 / nbr_2
    print("     >", nbr_1, "/", nbr_2, "=", round(total, 2))
else:
    print("Opération non valide.")
'''

#Impôts
#PAS FINI, j'arrive pas a comprendre comment faire a partie du palier 25 001 <=> 50 000
'''
revenu_annuel = int(input("Entrez votre revenu annuel : "))

if revenu_annuel <= 10000:
    print("L'impôt à payer est de 0 €.")

if revenu_annuel >= 10001 and revenu_annuel <= 25000:
    tranche = revenu_annuel - 10000
    impot = tranche * 0.1
    print("L'impôt à payer est de ", impot," €.")

if revenu_annuel >= 25001 and revenu_annuel <= 50000:
    tranche = revenu_annuel - 25000
    impot = tranche * 0.15
    print("L'impôt à payer est de ", impot," €.")

if revenu_annuel > 50000:
    tranche = revenu_annuel - 50000
    impot = tranche * 0.2
    print("L'impôt à payer est de ", impot," €.")
'''

#Nature d’un triangle
'''
longueur_1 = int(input("Entrez la longueur du premier côté : "))
longueur_2 = int(input("Entrez la longueur du deuxième côté : "))
longueur_3 = int(input("Entrez la longueur du troisième côté : "))

if longueur_1 + longueur_2 > longueur_3 and longueur_1 + longueur_3 > longueur_2 and longueur_2 + longueur_3 > longueur_1:
    if longueur_1 == longueur_2 and longueur_2 == longueur_3:
        print("     > C'est un triangle équilatéral.")

    elif longueur_1 == longueur_2 and longueur_1 != longueur_3 or longueur_2 == longueur_3 and longueur_2 != longueur_1 or longueur_3 == longueur_1 and longueur_3 != longueur_2:
        print("     > C'est un triangle isocèle.")
        
    elif longueur_1 != longueur_2 and longueur_1 != longueur_3 and longueur_2 != longueur_3:
        print("     > C'est un triangle scalène.")
else:
    print("     > Les longueurs fournies ne forment pas un triangle valide.")
'''

#Salaire net
#M.Duttiloy m'a dis que le round est acceptable meme si l'on voie pas le 2e zéro après la virgule car on n'a pas appris les f-string en cours
'''
salaire = float(input("Entrez le salaire de base de l'employé : "))
vente = float(input("Entrez le nombre de ventes réalisées par l'employé : "))
annee = float(input("Entrez le nombre d'années travaillées (ancienneté) : "))
cadre = str(input("L'employé est-il un cadre ? (True/False) : "))

if vente > 100:
    prime_performance = salaire * 0.1
else:
    prime_performance = 0

if annee >= 5 and annee <= 10:
    prime_annee = salaire * 0.05
elif annee > 10:
    prime_annee = salaire * 0.1
else:
    prime_annee = 0

if cadre == "True":
    prime_responsabilite = salaire * 0.05
else:
    prime_responsabilite = 0

salaire_brut = salaire + prime_performance + prime_annee + prime_responsabilite

if salaire_brut < 2000:
    taxes = salaire_brut * 0.2
elif salaire_brut >= 2000 and salaire_brut <= 5000:
    taxes = salaire_brut * 0.3
else:
    taxes = salaire_brut * 0.4

salaire_net = salaire_brut - taxes

print("     > Salaire de base : ", round(salaire, 2)," €")
print("     > Prime de performance : ", round(prime_performance, 2)," €")
print("     > Prime d'ancienneté : ", round(prime_annee, 2)," €")
print("     > Prime de responsabilité : ", round(prime_responsabilite, 2)," €")
print("     > Salaire brut : ", round(salaire_brut, 2),"")
print("     > Montant des taxes : ", round(taxes, 2)," €")
print("     > Salaire net : :", round(salaire_net, 2),"")
'''

#Mot de passe
'''
'''
import re

mot_de_passe = str(input("Entrez un mot de passe : "))

longueur_mdp = len(mot_de_passe) < 8
majuscule = re.search("[A-Z]", mot_de_passe)
chiffre = re.search("[0-9]", mot_de_passe)
caractère_special = re.search("[!-/]", mot_de_passe)

if (longueur_mdp and majuscule and chiffre and caractère_special) == True:
    print("Mot de passe valide.")
else:
   
    if longueur_mdp == False:
        print("     > Le mot de passe doit contenir au moins 8 caractères.")

    if majuscule == False:
        print("     > Le mot de passe doit contenir au moins une majuscule.")

    if chiffre == False:
        print("     > Le mot de passe doit contenir au moins un chiffre.")

    if caractère_special == False:
        print("     > Il doit contenir au moins un caractère spécial (parmi @, #, !, $, %, &, *).")     
    print("     > Mot de passe invalide.")


'''
if len(mot_de_passe) < 8:
    print("     > Le mot de passe doit contenir au moins 8 caractères.")

if not re.search("[A-Z]", mot_de_passe):
    print("     > Le mot de passe doit contenir au moins une majuscule.")

if not re.search("[0-9]", mot_de_passe):
    print("     > Le mot de passe doit contenir au moins un chiffre.")

if not re.search("[!-/]", mot_de_passe):
    print("     > Il doit contenir au moins un caractère spécial (parmi @, #, !, $, %, &, *).")     
print("     > Mot de passe invalide.")

'''