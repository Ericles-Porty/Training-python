def conta_digitos(numero, index, n_pares):
    if(index == len(numero)):
        return n_pares

    if(int(numero[index]) % 2 == 0):
        return conta_digitos(numero, index+1, n_pares+1)
    else:
        return conta_digitos(numero, index+1, n_pares)


numero = str(input())
pares = conta_digitos(numero, 0, 0)
print(pares)
