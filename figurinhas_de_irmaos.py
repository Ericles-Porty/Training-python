par = []
impar = []
lista = []

n = int(input())

for i in range(n):
    lista.append(int(input()))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print(len(par))
print(len(impar))

temp = set(par)
par = list(temp)

temp = set(impar)
impar = list(temp)

maior = sum(par) if sum(par) > sum(impar) else sum(impar)

print(maior)
