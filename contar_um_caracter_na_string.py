palavra = str(input(""))
letra = str(input(""))
contador = 0
for i in palavra:
    if i == letra:
        contador +=1
print(contador)