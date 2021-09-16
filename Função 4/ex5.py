# 5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.

def aumento(salario_atual,aumento_pct):
    salario_novo = salario_atual + (salario_atual * (aumento_pct / 100))
    return salario_novo

def main():
    porcentagem = int(input("Informe o valor, em porcentagem, de aumento do salário: "))
    soma_atual = soma_novo = 0
    for i in range(1,11):
        salario = float(input(f'Insira o salário do {i}º funcionário: '))
        salario_novo = aumento(salario, porcentagem)
        soma_novo += salario_novo
        soma_atual += salario
        print(f'Será gasto a mais, no salário do {i}º funcionário, R$ {salario_novo - salario:.2f}\n')
    print(f'Total diferença: R$ {soma_novo - soma_atual:.2f}')

main()