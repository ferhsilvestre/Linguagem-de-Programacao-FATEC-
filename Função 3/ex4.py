# 4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².

def area():
    lado = float(input('Insira o valor da lado: '))
    return lado * lado

def main():
    print(f'A área desse quadrado é de {area()} m²')

main()