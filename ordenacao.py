import time
import sys
import random

# Defina um novo limite de recursão
sys.setrecursionlimit(150000)

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for num in arr:
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda

    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr)//2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def partition(arr, baixo, alto):
    i = baixo - 1
    pivo = arr[alto]

    for j in range(baixo, alto):
        if arr[j] < pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[alto] = arr[alto], arr[i+1]
    return i+1

def quick_sort(arr, baixo, alto):
    if baixo < alto:
        pi = partition(arr, baixo, alto)

        quick_sort(arr, baixo, pi-1)
        quick_sort(arr, pi+1, alto)


inc = int(input("tamanho incial do vetor de entrada: "))
fim = int(input("tamanho final do vetor de entrada:  "))
stp = int(input("valor do 'stepper': "))
rps = int(input("número de repetições: "))


def my_random(inc, fim, stp, rps):

    print("[[RANDOM]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = [random.randint(0, inc*inc) for i in range(inc)]

        vetorCopia = vetor.copy()
        tempoBub = 0
        for i in range(rps):
            inicio = time.perf_counter()
            bubble_sort(vetorCopia)
            final = time.perf_counter()
            tempoBub += (final - inicio)

        vetorCopia = vetor.copy()
        tempoQuick = 0
        for i in range(rps):
            inicio = time.perf_counter()
            quick_sort(vetorCopia, 0, inc - 1)
            final = time.perf_counter()
            tempoQuick += (final - inicio)

        vetorCopia = vetor.copy()
        tempoIns = 0
        for i in range(rps):
            inicio = time.perf_counter()
            insertion_sort(vetorCopia)
            final = time.perf_counter()
            tempoIns += (final - inicio)

        vetorCopia = vetor.copy()
        tempoMer = 0
        for i in range(rps):
            inicio = time.perf_counter()
            merge_sort(vetorCopia)
            final = time.perf_counter()
            tempoMer += (final - inicio)

        vetorCopia = vetor.copy()
        tempoHeap = 0
        for i in range(rps):
            inicio = time.perf_counter()
            heap_sort(vetorCopia)
            final = time.perf_counter()
            tempoHeap += (final - inicio)

        vetorCopia = vetor.copy()
        tempoCount = 0
        for i in range(rps):
            inicio = time.perf_counter()
            counting_sort(vetorCopia)
            final = time.perf_counter()
            tempoCount += (final - inicio)

        print(f"{inc}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")
        inc = inc + stp


def reverse(inc, fim, stp, rps):

    print("[[REVERSE]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = list(range(inc, 0, -1))

        vetorCopia = vetor.copy()
        tempoBub = 0
        for i in range(rps):
            inicio = time.perf_counter()
            bubble_sort(vetorCopia)
            final = time.perf_counter()
            tempoBub += (final - inicio)

        vetorCopia = vetor.copy()
        tempoQuick = 0
        for i in range(rps):
            inicio = time.perf_counter()
            quick_sort(vetorCopia, 0, inc - 1)
            final = time.perf_counter()
            tempoQuick += (final - inicio)

        vetorCopia = vetor.copy()
        tempoIns = 0
        for i in range(rps):
            inicio = time.perf_counter()
            insertion_sort(vetorCopia)
            final = time.perf_counter()
            tempoIns += (final - inicio)

        vetorCopia = vetor.copy()
        tempoMer = 0
        for i in range(rps):
            inicio = time.perf_counter()
            merge_sort(vetorCopia)
            final = time.perf_counter()
            tempoMer += (final - inicio)

        vetorCopia = vetor.copy()
        tempoHeap = 0
        for i in range(rps):
            inicio = time.perf_counter()
            heap_sort(vetorCopia)
            final = time.perf_counter()
            tempoHeap += (final - inicio)

        vetorCopia = vetor.copy()
        tempoCount = 0
        for i in range(rps):
            inicio = time.perf_counter()
            counting_sort(vetorCopia)
            final = time.perf_counter()
            tempoCount += (final - inicio)

        print(f"{inc}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")
        inc = inc + stp

def sorted(inc, fim, stp, rps):

    print("[[SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = list(range(inc))

        vetorCopia = vetor.copy()
        tempoBub = 0
        for i in range(rps):
            inicio = time.perf_counter()
            bubble_sort(vetorCopia)
            final = time.perf_counter()
            tempoBub += (final - inicio)

        vetorCopia = vetor.copy()
        tempoQuick = 0
        for i in range(rps):
            inicio = time.perf_counter()
            quick_sort(vetorCopia, 0, inc - 1)
            final = time.perf_counter()
            tempoQuick += (final - inicio)

        vetorCopia = vetor.copy()
        tempoIns = 0
        for i in range(rps):
            inicio = time.perf_counter()
            insertion_sort(vetorCopia)
            final = time.perf_counter()
            tempoIns += (final - inicio)

        vetorCopia = vetor.copy()
        tempoMer = 0
        for i in range(rps):
            inicio = time.perf_counter()
            merge_sort(vetorCopia)
            final = time.perf_counter()
            tempoMer += (final - inicio)

        vetorCopia = vetor.copy()
        tempoHeap = 0
        for i in range(rps):
            inicio = time.perf_counter()
            heap_sort(vetorCopia)
            final = time.perf_counter()
            tempoHeap += (final - inicio)

        vetorCopia = vetor.copy()
        tempoCount = 0
        for i in range(rps):
            inicio = time.perf_counter()
            counting_sort(vetorCopia)
            final = time.perf_counter()
            tempoCount += (final - inicio)

        print(f"{inc}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")
        inc = inc + stp

def nearly(inc, fim, stp, rps):

    print("[[NEARLY SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = list(range(inc-1))
        vetor.append(0)

        vetorCopia = vetor.copy()
        tempoBub = 0
        for i in range(rps):
            inicio = time.perf_counter()
            bubble_sort(vetorCopia)
            final = time.perf_counter()
            tempoBub += (final - inicio)

        vetorCopia = vetor.copy()
        tempoQuick = 0
        for i in range(rps):
            inicio = time.perf_counter()
            quick_sort(vetorCopia, 0, inc - 1)
            final = time.perf_counter()
            tempoQuick += (final - inicio)

        vetorCopia = vetor.copy()
        tempoIns = 0
        for i in range(rps):
            inicio = time.perf_counter()
            insertion_sort(vetorCopia)
            final = time.perf_counter()
            tempoIns += (final - inicio)

        vetorCopia = vetor.copy()
        tempoMer = 0
        for i in range(rps):
            inicio = time.perf_counter()
            merge_sort(vetorCopia)
            final = time.perf_counter()
            tempoMer += (final - inicio)

        vetorCopia = vetor.copy()
        tempoHeap = 0
        for i in range(rps):
            inicio = time.perf_counter()
            heap_sort(vetorCopia)
            final = time.perf_counter()
            tempoHeap += (final - inicio)

        vetorCopia = vetor.copy()
        tempoCount = 0
        for i in range(rps):
            inicio = time.perf_counter()
            counting_sort(vetorCopia)
            final = time.perf_counter()
            tempoCount += (final - inicio)

        print(f"{inc}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")
        inc = inc + stp

my_random(inc, fim, stp, rps)
print()
print()
reverse(inc, fim, stp, rps)
print()
print()
sorted(inc, fim, stp, rps)
print()
print()
nearly(inc, fim, stp, rps)
