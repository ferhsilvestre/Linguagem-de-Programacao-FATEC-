def func_inss(salario, percentual=0.09): 
    return  salario * percentual

def liquido(salario, inss):
    return salario - inss

def main():
    salarios = []
    for i in range(10):
        salario = float(input(f'Insira o salário do {i+1}º funcionário: '))
        salarios.append(salario)

    for i in range(10):
        print('\n' + '-'*12 + f'{i+1}º Funcionário' + '-'*12)
        print(f'O salário original: R$ {salarios[i]:.2f}')
        print(f'O desconto do INSS: R$ {func_inss(salarios[i]):.2f}')
        print(f'O salário líquido: R$ {liquido(salarios[i], func_inss(salarios[i])):.2f}\n')

main()