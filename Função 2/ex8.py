# 8. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.

def valor():
    n = int(input("Digite um número inteiro: "))
    par_impar(n)

def par_impar(x):
    if x % 2 == 0:
        print(f'O número {x} é par!')
    else:
        print(f'O número {x} é ímpar!')

def main():
    valor()

main()