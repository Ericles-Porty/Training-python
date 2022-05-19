pessoa = [dict()]*100

total = 0
certo = 0

pessoa[total].update({"idade": int(input())})
velho = pessoa[total]["idade"]

while pessoa[total]["idade"] != -1:
    linha = str(input())
    linhatemp = linha.split(" ")
    pessoa[total].update({"sexo": linhatemp[0]})
    pessoa[total].update({"olhos": linhatemp[1]})
    pessoa[total].update({"cabelos": linhatemp[2]})

    if pessoa[total]["sexo"] == "f" and pessoa[total]["olhos"] == "l" and pessoa[total]["cabelos"] == "v" and pessoa[total]["idade"] >= 18 and pessoa[total]["idade"] <= 35:
        certo += 1
    if pessoa[total]["idade"] > velho:
        velho = pessoa[total]["idade"]
    total += 1
    pessoa[total].update({"idade": int(input())})


porcentagem = float(certo/total)*100
print("Mais velho:", velho)
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: {:.2f}%".format(porcentagem))
