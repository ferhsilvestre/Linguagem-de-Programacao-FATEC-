# 6. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário.

def tabuada(x):
    for i in range(1, 11):
        print(f'{x} x {i:^2} = {x * i}')

def main():
    n = int(input("Digite um número que queira a tabuada: "))
    tabuada(n)

main()