def progressao(numero):
    for i in range(1, numero+1):
        for j in range(i):
            print(i, end="")
            if(j+1 < i):
                print("-", end="")
        print()


numero = int(input(""))
progressao(numero)
