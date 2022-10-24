
import random

def string(length):
    if length=='':
        return 0
    else:
        return 1+string(length[1:])

debutant_tentative = 12
intermediaire_tentative = 8
expert_tentative = 5
debutant = "Débutant"
inter = "Intermédiaire"
expert = "Expert"
lettres_trouvees = ""
affichage = ""
word = [""]

dico = open('dico_france.txt','r', encoding="ISO-8859-1")
for line in dico:
    word.append(line.rstrip("\n#"))
    soluce = random.choice(word)

for l in soluce:
    affichage = affichage + "_ "
    print(l)
  
print("Choisir parmi plusieur niveau de difficulter: Débutant (10 vies), Intermédiaire (8 vies) et Expert(5 vies) :")
difficulter = str(input())

print(soluce)

if difficulter == debutant:
    while debutant_tentative > 0:
        print("\nMots a deviner :", affichage)
        print("Vous avez 12 tentatives")
        prop = input("Choisissez une lettre entre a et z :")[0:1].lower()
        if prop in soluce:
            lettres_trouvees = lettres_trouvees + prop
        else:
            debutant_tentative = debutant_tentative - 1
            print("Cette lettre ne compose pas ce mot")
            print("Il vous reste "+ str(debutant_tentative) + "tentatives")
            if debutant_tentative < 0:
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

if difficulter == inter:
    while intermediaire_tentative > 0:
        print("\nMots a deviner :", affichage)      
        print("Vous avez 12 tentatives")
        prop = input("Choisissez une lettre entre a et z :")[0:1].lower()
        if prop in soluce:
            lettres_trouvees = lettres_trouvees + prop
        else:
            intermediaire_tentative = intermediaire_tentative - 1
            print("Cette lettre ne compose pas ce mot")
            print("Il vous reste "+ str(intermediaire_tentative) + "tentatives")
            if intermediaire_tentative < 0:
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

if difficulter == expert:
    while expert_tentative > 0:
        print("\nMots a deviner :", affichage)      
        print("Vous avez 12 tentatives")
        prop = input("Choisissez une lettre entre a et z :")[0:1].lower()
        if prop in soluce:
            lettres_trouvees = lettres_trouvees + prop
        else:
            expert_tentative = expert_tentative - 1
            print("Cette lettre ne compose pas ce mot")
            print("Il vous reste "+ str(expert_tentative) + "tentatives")
            if expert_tentative < 0:
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