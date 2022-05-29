def fat(n, acumulado):
    if n > 0:
        return fat(n-1, acumulado*n)
    else:
        return acumulado


n = int(input())
while n != -1:
    print(fat(n, 1))
    n = int(input())
