clientes = []
temp = str(input())
while temp != "SAIR":
    dados = {}
    dados["nome"] = temp
    dados["senha"] = int(input())
    dados["situ"] = str(input())
    clientes.append(dados)
    temp = str(input())

id = int(input())
while id != -1:
    cont = 0 
    for i in clientes:
        if i["senha"] == id:
            if i["situ"] == "P":
                print("{}, seja bem-vindo(a)!".format(i["nome"]))
            else:
                print("Não está esquecendo de algo, {}? Procure a recepção!".format(i["nome"]))
            cont +=1
    if cont == 0:
        print("Seja bem-vindo(a)! Procure a recepção!")
    id = int(input())   