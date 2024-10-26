import random
import time
import sys

# aumentando limite de recurção utilizando a biblioteca sys
sys.setrecursionlimit(150000000)

'''def partition(arr, baixo, alto):
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
        quick_sort(arr, pi + 1, alto)'''

def corte_guloso_tora(precos, n):
    # Caso base: se n for 0, não há mais cortes a serem feitos
    if n == 0:
        return 0, 0  # Retorna valor 0 e tempo 0

    # Calcula a densidade (preço por metro) para cada comprimento
    densidades = [0] * (n + 1)
    for i in range(1, n + 1):
        densidades[i] = precos[i - 1] / i  # os preços são indexados a partir de 0

    # Encontra o corte com a densidade máxima
    densidade_maxima = float('-inf')
    melhor_comprimento = 0
    
    inicio = time.perf_counter()
    for i in range(1, n + 1):
        if densidades[i] > densidade_maxima:
            densidade_maxima = densidades[i]
            melhor_comprimento = i
            
    final = time.perf_counter()
    tempo = final - inicio
    
    # Faz o corte e continua com o restante
    valor_corte = precos[melhor_comprimento - 1]
    valor_restante, _ = corte_guloso_tora(precos, n - melhor_comprimento)

    return valor_corte + valor_restante, tempo

def cortar_tora(precos, n):
    # Cria um vetor para armazenar o valor máximo para cada comprimento
    valores_maximos = [0] * (n + 1)
    inicio = time.perf_counter()
    # Preenche o vetor valores_maximos
    for comprimento in range(1, n + 1):
        
        valor_max = float('-inf')
        for corte in range(1, comprimento + 1):
            if corte <= comprimento:
                valor_max = max(valor_max, precos[corte - 1] + valores_maximos[comprimento - corte])
        valores_maximos[comprimento] = valor_max
    
    final = time.perf_counter()
    tempo = final - inicio
    return valores_maximos[n], tempo

def main():
    '''inc = int(input("tamanho incial do vetor de entrada: "))

    fim = int(input("tamanho final do vetor de entrada:  "))
    while fim <= inc:
        print("O valor final do vetor não pode ser menor ou igual ao valor inicial")
        fim = int(input("novo valor final do vetor de entrada: "))

    stp = int(input("valor do 'stepper': "))
    while stp == 0:
        print("O valor do 'stepper' não pode ser 0")
        stp = int(input("novo valor do 'stepper': "))'''
    
    inc = 1000
    fim = 10000
    stp = 1000


    print("    n         vDP         tDP         vGreedy      tGreedy      %")
    print("------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):
        # j  sera o tamanho do vetor
        vetor = [random.randint(0, j) for _ in range(j)]
        vetor.sort()
        vDP, tDP = cortar_tora(vetor, j)
        vGreedy, tGreedy = corte_guloso_tora(vetor, j)
        porcentagem = vGreedy * 100 / vDP

        print(f"{j:6.0f}     {vDP:6.0f}     {tDP:.6f}     {vGreedy:6.0f}     {tGreedy:.6f}     {porcentagem:.2f}")



main()