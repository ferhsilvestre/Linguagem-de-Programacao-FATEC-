# 3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.

def area():
    base = float(input('Insira o valor da base: '))
    altura = float(input('Insira o valor da altura: '))
    return (base * altura) / 2

def main():
    print(f'A área desse triângulo é de {area()} m²')

main()