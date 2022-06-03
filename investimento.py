entrada = str(input("")).split()
investimento_inicial = float(entrada[0])
juros = float(entrada[1])
anos = int(entrada[2])
rendimento = investimento_inicial
montante = rendimento
for i in range(anos*4):
    rendimento = montante*juros
    montante = montante * (juros+1)
    print("Rendimento: {:.2f} Montante: {:.2f}".format(rendimento, montante))
