# 5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor.

def soma(x, y):
    soma_n = 0
    for i in range(x, y + 1):
        soma_n += i
    
    print(f'A soma de todos os números entre {x} e {y} é {soma_n}')

def main():
    n1 = int(input("Digite um número positivo: "))
    n2 = int(input("Digite outro número positivo: "))
    soma(n1, n2)

main()