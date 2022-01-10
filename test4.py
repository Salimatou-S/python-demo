a = 42
def affichage():
    print(a)

affichage()

def change(valeur):
    global a # global permet de stocker la valeur. Si on ne met pas global, la valeur du a ne se cahngera pas en 10 mais restera 42
    a = valeur

print(a)
change(10)
print(a)

nombre = 8
nombre  = int(input("La table de multiplication que vous souhaitez voir"))
print("Voici la table de multiplication de ", nombre)
for x in range(1,11):
    print(x, "x ", nombre, " = ", x*nombre) 