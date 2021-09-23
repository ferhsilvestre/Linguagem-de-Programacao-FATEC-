# 2. Não use nenhum método/função pronto da linguagem Python.
# Desenvolva todas as funções a seguir:
# a) Faça uma função com retorno (um valor no INSS calculado) e com parâmetro (um salario e a alíquota de 9% do INSS) para calcular o imposto do INSS que é descontado de um funcionário.
# b) Faça uma função com retorno (um salário líquido) e com parâmetro (um salario, um valor do INSS) que calcule o salário líquido de cada funcionário.
# c) Na função main() num laço de repetição, preencha um vetor com o salário de 10 funcionários. Em outro laço chame as outras funções (a e b) e apresente o salário original, o valor que será descontado do INSS e o salário líquido gerado de todos os funcionários.


def func_inss(salario, percentual): 
    return  salario * percentual

def liquido(salario, inss):
    return salario - inss

def main():
    salarios, inss, liquidos = [], [], []
    aliquota = 9 / 100 
    for i in range(10):
        salario = float(input(f'Insira o salário do {i+1}º funcionário: '))
        salarios.append(salario)
        inss.append(func_inss(salario, aliquota))
        liquidos.append(liquido(salario, inss[i]))

    for i in range(10):
        print('\n' + '-'*12 + f'{i+1}º Funcionário' + '-'*12)
        print(f'O salário original: R$ {salarios[i]:.2f}')
        print(f'O desconto do INSS: R$ {inss[i]:.2f}')
        print(f'O salário líquido: R$ {liquidos[i]:.2f}\n')

main()