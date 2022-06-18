decisao = str(input())
decisao = decisao.split(" ")

alunos = []

for i in range(int(decisao[0])):
    alunos.append(str(input()))

alunos.sort()

print(alunos[int(decisao[1])-1])
