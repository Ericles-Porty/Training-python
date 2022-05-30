def fib(n,lista):
    i = 3
    fib1 = 1
    fib2 = 1
    while i < n:
        soma = fib1 + fib2
        fib1 = fib2
        fib2 = soma
        i += 1
        lista.append(fib2)
    return lista


def printa(n,lista):
    if n > 0:
        print(lista[n-1],end=" ")
        n -=1
        return printa(n,lista)
    return
    

n = int(input())
lista= [0,1,1]
lista = fib(n,lista)
printa(n,lista)