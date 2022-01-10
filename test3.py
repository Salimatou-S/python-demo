def affiche_menu():
    print("Menu:")
    print("* Action 1")
    print("* Action 2")

affiche_menu()

def dire(texte):
    print('#' + texte)

dire('Bonjour')
dire('Au revoir')
dire('A demain')

def addition(a,b):
    return a + b

somme = addition(10,5) 
print(somme)

def saluer(nom = 'Visiteur'): # on initialise pour avoir la valeur par defaut visiteur sinon si on met juste nom et appel fonction sans rien dedans ce serait une erreur
    print("Bonjour " + nom)

saluer('Muriel')
saluer()