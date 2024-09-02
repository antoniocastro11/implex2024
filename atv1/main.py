import time
import sys
import random
from algOrd import counting_sort, heapify, heap_sort, merge_sort, insertion_sort, bubble_sort, partition, quick_sort

# limite de recursão
sys.setrecursionlimit(150000)

# entrada dos valores iniciais, pedidos no enunciado
inc = int(input("tamanho incial do vetor de entrada: "))
fim = int(input("tamanho final do vetor de entrada:  "))
stp = int(input("valor do 'stepper': "))
rps = int(input("número de repetições: "))

# calculo do tempo do vetor RANDOM
def my_random(inc, fim, stp, rps):

    print("[[RANDOM]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = random.sample(range(1, fim+1), j)

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
            quick_sort(vetorCopia, 0, j - 1)

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

# calculo do tempo do vetor REVERSE
def reverse(inc, fim, stp, rps):
    print("[[REVERSE]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        #preencher vetor de j a 1
        vetor = list(range(j, 0, -1))
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
            quick_sort(vetorCopia, 0, j - 1)


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

# calculo do tempo do vetor SORTED
def sorted(inc, fim, stp, rps):

    print("[[SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        #preencher vetor ordenado de 1 a j
        vetor = list(range(1, j+1))

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
            quick_sort(vetorCopia, 0, j - 1)


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

# calculo do tempo do vetor NEARLY
def nearly(inc, fim, stp, rps):

    print("[[NEARLY SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        vetor = random.sample(range(1, fim+1), j)

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
            quick_sort(vetorCopia, 0, j - 1)


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