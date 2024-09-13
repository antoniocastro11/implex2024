#Alunos: Antonio Galvan Castro e João Pedro da Cruz Silva de Camargo

import time
import sys
import random
from func import counting_sort, heapify, heap_sort, merge_sort, insertion_sort, bubble_sort, partition, quick_sort, ordenar_90_porcento

# aumentando limite de recurção utilizando a biblioteca sys
sys.setrecursionlimit(150000)

# entrada dos valores iniciais, pedidos no enunciado
inc = int(input("tamanho incial do vetor de entrada: "))

fim = int(input("tamanho final do vetor de entrada:  "))
while fim <= inc: # certificando que o valor final do vetor inserido pelo usuário seja maior que o valor inicial
    print("O valor final do vetor não pode ser menor ou igual ao valor inicial")
    fim = int(input("novo valor final do vetor de entrada: "))

stp = int(input("valor do 'stepper': "))
while stp == 0:
    print("O valor do 'stepper' não pode ser 0")
    stp = int(input("novo valor do 'stepper': "))
    
rps = int(input("número de repetições: "))

# calculo do tempo do vetor aleatorio
def my_random(inc, fim, stp, rps):

    # prints do cabeçalho dos dados do vetor aleatorio
    print("[[RANDOM]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        for i in range(rps):
            # gerar numeros no intervalo [0, j]
            vetor = [random.randint(0, j) for _ in range(j)]  
            tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            bubble_sort(vetorCopia)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoBub += (final - inicio) # guarda o tempo gasto para executar a funcao

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            quick_sort(vetorCopia, 0, j - 1)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoQuick += (final - inicio) # guarda o tempo gasto para executar a funcao

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            insertion_sort(vetorCopia)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoIns += (final - inicio) # guarda o tempo gasto para executar a funcao

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            merge_sort(vetorCopia)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoMer += (final - inicio) # guarda o tempo gasto para executar a funcao

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            heap_sort(vetorCopia)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoHeap += (final - inicio) # guarda o tempo gasto para executar a funcao

            # vetorCopia recebe os valores do vetor aleatorio
            vetorCopia = vetor.copy()
            inicio = time.perf_counter() # marca o tempo inicial do chamamento da funcao
            counting_sort(vetorCopia)
            final = time.perf_counter() # marca o tempo final do chamamento da funcao
            tempoCount += (final - inicio) # guarda o tempo gasto para executar a funcao

        # imprimir usando j para manter a progressão correta de n
        # e dividir o tempo pelo número de repetições para obter a média
        print(f"{j}  {(tempoBub/rps):.6f}     {(tempoIns/rps):.6f}     {(tempoMer/rps):.6f}     {(tempoHeap/rps):.6f}    {(tempoQuick/rps):.6f}     {(tempoCount/rps):.6f}")



def reverse(inc, fim, stp):

    # print do cabeçalho dos dados do vetor reverso
    print("[[REVERSE]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    # laco para executar as linhas de acordo com o tamanho do vetor, onde j é o tamanho do vetor
    for j in range(inc, fim+1, stp):

        # criar um vetor ordenado de forma decrescente: n, n-1, n-2, ..., 1
        vetor = list(range(j, 0, -1))
        
        # inicializar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble 
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion
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

        # Heap
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # exibir resultados para o tamanho atual do vetor (j)
        print(f"{j}  {(tempoBub):.6f}     {(tempoIns):.6f}     {(tempoMer):.6f}     {(tempoHeap):.6f}    {(tempoQuick):.6f}     {(tempoCount):.6f}")

def sorted(inc, fim, stp):

    # print do cabeçalho dos dados do vetor ordenado
    print("[[SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        vetor = list(range(1, j+1))
        
        # iniciar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble 
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        insertion_sort(vetorCopia)
        final = time.perf_counter()
        tempoIns = final - inicio

        # Merge
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        merge_sort(vetorCopia)
        final = time.perf_counter()
        tempoMer = final - inicio

        # Heap
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # exibir resultados para o tamanho atual do vetor (j)
        print(f"{j}  {(tempoBub):.6f}     {(tempoIns):.6f}     {(tempoMer):.6f}     {(tempoHeap):.6f}    {(tempoQuick):.6f}     {(tempoCount):.6f}")

def nearly(inc, fim, stp):

    # print do cabeçalho dos dados do vetor quase ordenado
    print("[[NEARLY SORTED]]")
    print("n      Bubble      Insertion       Merge       Heap        Quick       Counting")
    print("-------------------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        
        # criar vetor quase ordenado (90% ordenado)
        vetor = [random.randint(0, j) for _ in range(j)]
        vetor = ordenar_90_porcento(vetor)
        
        # iniciar as variáveis de tempo
        tempoBub = tempoQuick = tempoIns = tempoMer = tempoHeap = tempoCount = 0

        # Bubble 
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        bubble_sort(vetorCopia)
        final = time.perf_counter()
        tempoBub = final - inicio

        # Quick 
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        quick_sort(vetorCopia, 0, j - 1)
        final = time.perf_counter()
        tempoQuick = final - inicio

        # Insertion
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        insertion_sort(vetorCopia)
        final = time.perf_counter()
        tempoIns = final - inicio

        # Merge
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        merge_sort(vetorCopia)
        final = time.perf_counter()
        tempoMer = final - inicio

        # Heap
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        heap_sort(vetorCopia)
        final = time.perf_counter()
        tempoHeap = final - inicio

        # Counting
        vetorCopia = vetor.copy()
        inicio = time.perf_counter()
        counting_sort(vetorCopia)
        final = time.perf_counter()
        tempoCount = final - inicio

        # exibir resultados para o tamanho atual do vetor (j)
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
