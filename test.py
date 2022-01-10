a=7
print(a+3)
b=3
print(a+b) # aficher le resultat des valeurs respectives des variables a et b
print(a)
#a=b+1 # on change la valeur de a
#print(a)
#print(a+b)
a+=b # equivalent à a=a+b
print(a)

a, b = 11, 4 # on affecte les valeurs à a et b
c=a//b # a egal à 10 car 
d=a%b
print('La division de ' + str(a) + ' par ' + str(b) + ' est egale à ' + str(c) + '. ll reste ' + str(d))
print(d)

string = "Et voilà du texte"# simple quote ou double quote
string1 = 'Nous l\'avons' 
string2 = " \"réparé\""# on met les antislach avant les quotes pour que ce soit pris en compte
print(string) # affiche le texte
print(string1 + " " + string2)

reponse =input()
age = int(input("Quel age avez vous?"))
print("Vous avez" + str(age) + " ans")

if age > 16 and age <100:
    print("Vous avez plus de 16 ans")
elif age > 100:
    print("Tu ne te moquerais pas de moi?")
else:
    print("Tu es encore un peu jeune")

a = 3
print(type(a))
b=8.2
print(type(b))
string = "Au revoir"
print(type(string))
vrai= False
print(type(vrai))

print (7 > 5 > 1)
print(7 > 11 < 9 != 10)



