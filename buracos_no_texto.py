def conta_buracos(letra):
    if(letra in ("ADOPORQ")):
        return 1
    elif(letra == 'B'):
        return 2
    return 0


t = int(input(""))
for i in range(t):
    contador = 0
    palavra = str(input(""))
    for letra in palavra:
        contador += conta_buracos(letra)
    print(contador)
