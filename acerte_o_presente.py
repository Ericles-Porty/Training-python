n = int(input())
presentes = []
if (n >= 3 and n <= 20):
    for i in range(n):
        linha = str(input())
        linhatemp = linha.split(" ")
        temp = {"nome": linhatemp[0]}
        temp["p1"] = linhatemp[1]
        temp["p2"] = linhatemp[2]
        temp["p3"] = linhatemp[3]
        presentes.append(temp)


linha = str(input())
while linha != "FIM":
    linhatemp = linha.split(" ")
    
    for p in presentes:
        if linhatemp[0] == p["nome"]:
            if linhatemp[1] == p["p1"] or linhatemp[1] == p["p2"] or linhatemp[1] == p["p3"]:
                print("Uhul! Seu amigo secreto vai adorar")
                break
            else:
                print("Tente Novamente!")
                break

    linha = str(input())
