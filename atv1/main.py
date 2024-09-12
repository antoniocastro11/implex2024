import time
import sys
import random
from func import counting_sort, heapify, heap_sort, merge_sort, insertion_sort, bubble_sort, partition, quick_sort, ordenar_90_porcento

# limite de recursão
sys.setrecursionlimit(150000)

# entrada dos valores iniciais, pedidos no enunciado
inc = int(input("tamanho incial do vetor de entrada: "))

fim = int(input("tamanho final do vetor de entrada:  "))
while fim <= inc:
    print("O valor final do vetor não pode ser menor ou igual ao valor inicial")
    fim = int(input("novo valor final do vetor de entrada: "))

stp = int(input("valor do 'stepper': "))
while stp == 0:
    print("O valor do 'stepper' não pode ser 0")
    stp = int(input("novo valor do 'stepper': "))
    
rps = int(input("número de repetições: "))

# calculo do tempo do vetor RANDOM
def my_random(inc, fim, stp, rps):

    print("[[RANDOM]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        for i in range(rps):
            # Gerar números no intervalo [0, j^2]
            vetor = [random.randint(0, j*j) for _ in range(j)]  
            tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            bubble_sort(vetorCopia)
            final = time.perf_counter()
            tempoBub += (final - inicio)

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            quick_sort(vetorCopia, 0, j - 1)
            final = time.perf_counter()
            tempoQuick += (final - inicio)

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            insertion_sort(vetorCopia)
            final = time.perf_counter()
            tempoIns += (final - inicio)

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            merge_sort(vetorCopia)
            final = time.perf_counter()
            tempoMer += (final - inicio)

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            heap_sort(vetorCopia)
            final = time.perf_counter()
            tempoHeap += (final - inicio)

            vetorCopia = vetor.copy()
            inicio = time.perf_counter()
            counting_sort(vetorCopia)
            final = time.perf_counter()
            tempoCount += (final - inicio)

        # Imprimir usando j para manter a progressão correta de n
        print(f"{j}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")

def reverse(inc, fim, stp):
    print("[[REVERSE]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        # Criar um vetor ordenado de forma decrescente: n, n-1, n-2, ..., 1
        vetor = list(range(j, 0, -1))
        
        # Inicializar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        insertion_sort(vetorCopia)
        final = time.perf_counter()
        tempoIns = final - inicio

        # Merge Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        merge_sort(vetorCopia)
        final = time.perf_counter()
        tempoMer = final - inicio

        # Heap Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # Exibir resultados para o tamanho atual do vetor
        print(f"{j}  {(tempoBub):.6f}     {(tempoIns):.6f}     {(tempoMer):.6f}     {(tempoHeap):.6f}    {(tempoQuick):.6f}     {(tempoCount):.6f}")

def sorted(inc, fim, stp):

    print("[[SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        # Criar vetor já ordenado: 1, 2, 3, ..., n
        vetor = list(range(j))
        
        # Inicializar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        insertion_sort(vetorCopia)
        final = time.perf_counter()
        tempoIns = final - inicio

        # Merge Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        merge_sort(vetorCopia)
        final = time.perf_counter()
        tempoMer = final - inicio

        # Heap Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # Exibir resultados para o tamanho atual do vetor
        print(f"{j}  {(tempoBub):.6f}     {(tempoIns):.6f}     {(tempoMer):.6f}     {(tempoHeap):.6f}    {(tempoQuick):.6f}     {(tempoCount):.6f}")

def nearly(inc, fim, stp):

    print("[[NEARLY SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        
        # Criar vetor quase ordenado (90% ordenado)
        vetor = [random.randint(0, j**2) for _ in range(j)]
        vetor = ordenar_90_porcento(vetor)
        
        # Inicializar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        insertion_sort(vetorCopia)
        final = time.perf_counter()
        tempoIns = final - inicio

        # Merge Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        merge_sort(vetorCopia)
        final = time.perf_counter()
        tempoMer = final - inicio

        # Heap Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting Sort
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # Exibir resultados para o tamanho atual do vetor
        print(f"{j}  {(tempoBub):.6f}     {(tempoIns):.6f}     {(tempoMer):.6f}     {(tempoHeap):.6f}    {(tempoQuick):.6f}     {(tempoCount):.6f}")



my_random(inc, fim, stp, rps)
print()
print()
reverse(inc, fim, stp)
print()
print()
sorted(inc, fim, stp)
print()
print()
nearly(inc, fim, stp)