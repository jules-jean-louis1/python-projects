
oui = "Jouer"
score = "Scores"
tentatives = 12
score_list = [0,0]
round_number = 0 
user1 = "oo"
user2 = "ii"
user_list = [user2,user1]
def print_matrice():
        print()
        for i in range(3):
            print(' '.join(a[i]))                              # ' '.join pour enlever les crochets et parenthèses

def x(l,c):                                                    #l= ligne c=colonne, crée le X qui remplacera le '_'
        a[l][c] = 'X'

def o(l,c):                                                    #l= ligne c=colonne
        a[l][c] = 'O'

def input_user(lig,col):
            lig = int(input("Entrer une ligne entre 1 et 3 :"))
            col = int(input("Entrer une colonne entre 1 et 3 :"))
            x(lig-1,col-1)
            print_matrice()


a = ([ ["_","_","_"],["_","_","_"],["_","_","_"] ])

reponse = str(input("Bonjour, voulez-vous jouer ou voir le tableau des scores?"))

if reponse == oui:                                            #entrer dans le jeux
    user1 = input("entre le nom du premiers joueur : ")
    print("Croix :",user1)
    croix = "X"
    user2 = input("Entrer le nom du second joueur : ")
    print("Rond :",user2)
    rond = "O"
    print("Affichage de la grille:")
    print_matrice()
    while True:
        round_number +=1
        if round_number%2:
            print(user_list[1],"Joueur 1, à votre tour :")
            lig = int(input("Entrer une ligne entre 1 et 3 :"))
            col = int(input("Entrer une colonne entre 1 et 3 :"))
            if col < 4 and lig < 4 :
                if a[lig-1][col-1] =='_':
                    x(lig-1,col-1)
                    print_matrice()
                else:
                    print("Cette case est déjà prise.")
            else:
                print("Hors limite, les valeurs doivent être comprise entre 1 et 3")
        else:
            print(user_list[0],"Joueur 1, à votre tour :")
            lig = int(input("Entrer une ligne entre 1 et 3 :"))
            col = int(input("Entrer une colonne entre 1 et 3 :"))
            if col < 4 and lig < 4 :
                if a[lig-1][col-1] =='_':
                    x(lig-1,col-1)
                    print_matrice()
                else:
                    print("Cette case est déjà prise.")
            else:
                print("Hors limite, les valeurs doivent être comprise entre 1 et 3")


elif reponse == score:
    print("Tableau des scores")    
else:
    print("Au revoir")


