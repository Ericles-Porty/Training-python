pares = []
impares = []
n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

pares = sorted(pares)
impares = sorted(impares, reverse=True)

for e in pares:
    print(e)

for e in impares:
    print(e)
