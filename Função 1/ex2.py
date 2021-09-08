# 2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

def soma():
    n1 = int(input("Digite um número positivo: "))
    n2 = int(input("Digite outro número positivo: "))
    soma_n = 0

    for i in range(n1, n2 + 1):
        soma_n += i
    
    print(f'A soma de todos os números entre {n1} e {n2} é {soma_n}')

def main():
    soma()

main()