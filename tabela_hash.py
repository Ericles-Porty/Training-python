n = int(input())
for a in range(n):
    line = input().split()
    m, c = int(line[0]), int(line[1])

    dic = {}
    for i in range(m):
        dic[i] = []
    line = input().split()
    valores = [int(x) for x in line]

    for i in range(c):
        temp = valores[i] % m 
        t = []
        try:
            t = dic[temp]
        except:
            pass
        t.append(valores[i])
        dic[temp] = t
    for i in range(m):
        print(i, end=' -> ')
        if dic[i] == []:
            print('\\')
        else:
            print(' -> '.join([str(x) for x in dic[i]]) + ' -> \\')

    print()