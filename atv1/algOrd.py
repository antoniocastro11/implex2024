import random
# ALGORITMO DE ORDENAÇÃO COUNTINGSORT
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

# Teste do algoritmo
vetor = [926, 1622, 385, 144, 1632, 785, 688, 1647, 542, 617, 1116, 2421, 1332, 2210, 1025, 2390, 1975, 1145, 1578, 1147, 1750, 2286, 2276, 1553, 440, 993, 328, 872, 1033, 1324, 1653, 666, 165, 800, 1680, 10, 500, 643, 2130, 1506, 1025, 1002, 1052, 2302, 1951, 262, 1773, 1238, 1277, 2289]
counting_sort(vetor)
print("Vetor ordenado:")
print(vetor)

# ALGORITMO DE ORDENAÇÃO HEAPSORT
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

# Teste do algoritmo
vetor = [4, 2, 6, 8, 1, 3, 7, 5]
heap_sort(vetor)
print("Vetor ordenado:")
print(vetor)

# ALGORITMO DE ORDENAÇÃO MERGESORT
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

# Teste do algoritmo
vetor = [4, 2, 6, 8, 1, 3, 7, 5]
merge_sort(vetor)
print("Vetor ordenado:")
print(vetor)

# ALGORITMO DE ORDENAÇÃO INSERTIONSORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave

# Teste do algoritmo
vetor = [4, 2, 6, 8, 1, 3, 7, 5]
insertion_sort(vetor)
print("Vetor ordenado:")
print(vetor)

# ALGORITMO DE ORDENAÇÃO BUBBLESORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Teste do algoritmo
vetor = [4, 2, 6, 8, 1, 3, 7, 5]
bubble_sort(vetor)
print("Vetor ordenado:")
print(vetor)


# ALGORITMO DE ORDENAÇÃO QUICKSORT
def partition(arr, baixo, alto):
    # Escolhe um pivô aleatório
    rand_index = random.randint(baixo, alto)
    arr[rand_index], arr[alto] = arr[alto], arr[rand_index]
    
    i = baixo - 1
    pivo = arr[alto]

    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quick_sort(arr, baixo, alto):
    if baixo < alto:
        pi = partition(arr, baixo, alto)
        quick_sort(arr, baixo, pi - 1)
        quick_sort(arr, pi + 1, alto)


# Teste do algoritmo
vetor = [4, 2, 6, 8, 1, 3, 7, 5]
quick_sort(vetor, 0, len(vetor) - 1)
print("Vetor ordenado:")
print(vetor)

##############################################################################################################

def ordenar_90_porcento(vetor):
    # Calcular 90% do comprimento do vetor
    tamanho_vetor = len(vetor)
    tamanho_ordem = int(tamanho_vetor * 0.9)
    
    # Dividir o vetor em duas partes
    parte_a_ser_ordenada = vetor[:tamanho_ordem]
    parte_inalterada = vetor[tamanho_ordem:]
    
    # Ordenar a parte que precisa ser ordenada
    parte_a_ser_ordenada.sort()
    
    # Combinar as duas partes
    vetor_ordenado = parte_a_ser_ordenada + parte_inalterada
    
    return vetor_ordenado
