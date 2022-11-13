def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


nl, nc = map(int, input().split())

dados = []

for _ in range(nl):
    dados.append(input().split(' '))

l = [x for l in dados for x in l]


num = []
letras = []

for e in l:
    temp = [*e]
    num.append(int(temp[0]))
    letras.append(temp[1])
v = []
d = []

for i in range(len(num)):
    if letras[i] == 'V':
        v.append(num[i])
    else:
        d.append(num[i])

size = len(v)
quickSort(v, 0, size - 1)

size = len(d)
quickSort(d, 0, size - 1)

for e in v:
    print(e, 'V', sep='')

for e in d:
    print(e, 'D', sep='')
