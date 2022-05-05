passeios = []
temp = int(input())
idades = 0
contador = 0
while temp != -1:
    dados = {}
    dados["num"] = temp
    dados["data"] = str(input())
    dados["origem"] = str(input())
    dados["destino"] = str(input())
    dados["hora"] = str(input())
    dados["poltrona"] = int(input())
    dados["idade"] = int(input())
    idades += dados["idade"]
    dados["nome"] = str(input())
    passeios.append(dados)
    contador+=1
    temp = int(input())

media = idades/contador
for i in range(contador):
    if passeios[i]["poltrona"]%2==0 and passeios[i]["idade"] > media:
        print(passeios[i]["nome"])