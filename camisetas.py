total = int(input())

while total > 0:
    camisas = []
    for i in range(total):
        temp = {"nome": str(input())}

        linha = str(input())
        linhatemp = linha.split(" ")

        temp["cor"] = linhatemp[0]
        temp["tamanho"] = linhatemp[1]
        camisas.append(temp)

    camisas = sorted(camisas, key=lambda d: d["nome"])
    camisas = sorted(camisas, key=lambda d: d["tamanho"],reverse=True)
    camisas = sorted(camisas, key=lambda d: d["cor"])
    for i in camisas:
        print(i["cor"],i["tamanho"],i["nome"])
    print()
    total = int(input())