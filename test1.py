i = 0 # initialiser toujours la boucle avant while
while i < 10:
    i+= 1
    if i%2 == 0: #si i est impair, donc le reste de division est different de 0
        continue
    print(i)
    
