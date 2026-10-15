#Structures alternatives
#Année bissextile
'''
annee = int(input("Saisir l'année : "))
annee_bissextile = 366

if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print("Année bissextile")
else:
    print("Année non bissextile")
'''

#Société de transport
'''
age = int(input("Saisir votre âge : "))

if age <= 5:
    print("Le prix du transport est gratuit.")
elif age < 16:
    print("Le prix du transport est de 5 euros.")
elif age <= 21:
    print("Le prix du transport est de 6 euros.")
elif age < 51:
    print("Le prix du transport est de 10 euros.")
else:
    print("Le prix du transport est de 9 euros.")
'''
# A CORRIGER

#Voyage scolaire
'''
nbr_eleves = int(input("Nombre d’élèves : "))
nbr_jours = int(input("Durée du voyage en jours : "))

cout_nourriture = 3.50 * nbr_jours

if nbr_eleves <= 25:
    cout_transport = 110
else:
    cout_transport = 100

if nbr_eleves < 20:
    prix_hebergement = 4.20 * nbr_jours
elif nbr_eleves <= 35 :
    prix_hebergement = 3.80 * nbr_jours
else:
    prix_hebergement = 4.00 * nbr_jours

prix_voyage = cout_nourriture + cout_transport + prix_hebergement

print("Le prix du voyage revient à", prix_voyage, "euros à par élève.")
'''

#Vinci location
'''

type_vehicule = input("Type du véhicule : ")
carburant = input("Carburant : ")
duree_location = int(input("Durée de location en jour : "))
distance_km = int(input("Distance en km : "))
offre_commerciale = bool(input("Offre commerciale : "))

if type_vehicule == "Citadine":
    citadine_location_par_jour = 80
elif type_vehicule == "Berline":
    berline_location_par_jour = 100
else:
    sportive_location_par_jour = 130

montant_consommation = 
'''