import random

debutant_tentative = 12
intermediaire_tentative = 8
expert_tentative = 5
debutant = "Débutant"
inter = "Intermédiaire"
expert = "Expert"
lettres_trouvees = ""
affichage = ""
word = [""]

def pendule(tentatives):
    while tentatives > 0:
        print("\nMots a deviner :", affichage)      
        print("Vous avez 12 tentatives")
        prop = input("Choisissez une lettre entre a et z :")[0:1].lower()
        if prop in soluce:
            lettres_trouvees = lettres_trouvees + prop
        else:
            tentatives = tentatives - 1
            print("Cette lettre ne compose pas ce mot")
            print("Il vous reste "+ str(tentatives) + "tentatives")
            if tentatives < 0:
                print("Il ne vous rester plus de tentative")
        affichage = ""
        for x in soluce:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print("Félicitations vous avez gagné") 
            break
            
    print("\n    * Fin de la partie *    ") 



dico = open('dico_france.txt','r', encoding="ISO-8859-1")
for line in dico:
    word.append(line.rstrip("\n#"))
    soluce = random.choice(word)

for l in soluce:
    affichage = affichage + "_ "
  
print("Choisir parmi plusieur niveau de difficulter: Débutant (10 vies), Intermédiaire (8 vies) et Expert(5 vies) :")
difficulter = str(input())

if difficulter == debutant:
    pendule(12)

if difficulter == inter:
    pendule(8)
    
if difficulter == expert:
    pendule(5)
