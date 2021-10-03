# 3. Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento.

class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0

produtos = []

def cadastrar(total):
    for i in range(total):
        p = Tipo_Produto()
        p.codigo = int (input(f'\nInforme o código do {i+1}º produto: '))
        p.nome = input(f'Informe o nome do {i+1}º produto: ')
        p.preco = float (input(f'Informe o preço do {i+1}º produto: '))
        produtos.append(p)
    
    reajuste()

def reajuste():
    for p in produtos:
        preco_reajustado = p.preco + (p.preco * 0.1)
        apresentar_cadastro(p, preco_reajustado)

def apresentar_cadastro(p, preco_reajustado):
    print()
    print('- - - ' * 5)
    print(f'Código: {p.codigo}')
    print(f'Nome: {p.nome}')
    print(f'Valor: {p.preco:.2f}')
    print(f'Valor reajustado: {preco_reajustado:.2f}')
    print('- - - ' * 5)

def main():
    cadastrar(5)

main()