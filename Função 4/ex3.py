# 3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.

def aumento(x,y):
    salario_novo = x + (x * (y / 100))    
    return salario_novo

def main():
    porcentagem = int(input("Informe o valor, em porcentagem, de aumento do salário: "))
    salario = float(input('Informe o salário atual: '))
    print(f'O valor do novo salário é R$ {aumento(salario, porcentagem):.2f}')

main()