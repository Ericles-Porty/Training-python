n = int(input())

cod = []
desc = []
preco = []

for i in range(n):
    cod.append(int(input()))
    desc.append(str(input()))
    preco.append(float(input()))

valor_total = 0.0
codigo = int(input())
while codigo != 0:
    quantidade = int(input())
    for index, i in enumerate(cod):
        if codigo == i:
            if quantidade > 0:
                valor_total += float(preco[index] * quantidade)
    codigo = int(input())

print("{:.2f}".format(valor_total))
