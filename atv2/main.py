import random
import time


def corte_guloso(precos, n):
    valor_total = 0
    comprimento_restante = n

    while comprimento_restante > 0:
        melhor_densidade = 0
        melhor_comprimento = 0
        
        for i in range(1, comprimento_restante + 1):
            densidade = precos[i - 1] / i
            if densidade > melhor_densidade:
                melhor_densidade = densidade
                melhor_comprimento = i

        valor_total += precos[melhor_comprimento - 1]
        comprimento_restante -= melhor_comprimento

    return valor_total



def corte_dinamico(precos, n):
    # Cria um vetor para armazenar o valor máximo para cada comprimento
    valores_maximos = [0] * (n + 1)
    
    # Preenche o vetor valores_maximos
    for comprimento in range(1, n + 1):
        valor_max = 0  # Inicializa o valor máximo como 0
        for corte in range(1, comprimento + 1):
            # Calcula o valor máximo
            valor_max = max(valor_max, precos[corte - 1] + valores_maximos[comprimento - corte])
        valores_maximos[comprimento] = valor_max
    
    return valores_maximos[n]


def gerar_precos(n):
    precos = [random.randint(1, n) for i in range(n)]
    precos.sort()
    return precos


def main():
    inc = int(input("tamanho incial do vetor de entrada: "))
    fim = int(input("tamanho final do vetor de entrada:  "))

    while fim <= inc:
        print("O valor final do vetor não pode ser menor ou igual ao valor inicial")
        fim = int(input("novo valor final do vetor de entrada: "))

    stp = int(input("valor do 'stepper': "))

    while stp == 0:
        print("O valor do 'stepper' não pode ser 0")
        stp = int(input("novo valor do 'stepper': "))
    

    print("    n         vDP         tDP         vGreedy      tGreedy      %")
    print("------------------------------------------------------------------")

    for j in range(inc, fim+1, stp):

        vetor = gerar_precos(j)

        inicioDP = time.perf_counter()
        vDP = corte_dinamico(vetor, j)
        finalDP = time.perf_counter()
        tDP = finalDP - inicioDP

        inicioGreedy = time.perf_counter()
        vGreedy= corte_guloso(vetor, j)
        finalGreedy = time.perf_counter()
        tGreedy = finalGreedy - inicioGreedy

        porcentagem = vGreedy * 100 / vDP

        print(f"{j:6.0f}     {vDP:7.0f}     {tDP:.6f}     {vGreedy:7.0f}     {tGreedy:.6f}     {porcentagem:.2f}")


main()