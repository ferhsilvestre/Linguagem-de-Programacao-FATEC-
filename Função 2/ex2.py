# 2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.

def subtracao(x, y):
    s = x - y
    print(f'{x} - {y} = {s}')

def main():
    n1 = int(input("Entre com um número: "))
    n2 = int(input("Entre com outro número: "))
    subtracao(n1, n2)

main()