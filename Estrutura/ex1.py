# 1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.

class Tipo_Produto:

    codigo = 0

    nome = ''

    preco = 0.0



def mostrar_membros(p):

    print(f'\nCódigo: {p.codigo} \tNome: {p.nome} \tPreço R$ {p.preco:.2f}')



def main():

    #1º passo, inicializar uma variável que representará a estrutura/Tipo_Produto

    p1 = Tipo_Produto()

    p1.codigo = int (input('Informe o código do produto: '))

    p1.nome = input('Informe o nome do produto: ')

    p1.preco = float (input('Informe o preço do produto: '))

    mostrar_membros(p1)

    p1.preco = p1.preco + p1.preco * 10 / 100

    mostrar_membros(p1)



    p2 = Tipo_Produto()

    p2.codigo = int (input('Informe o código do produto: '))

    p2.nome = input('Informe o nome do produto: ')

    p2.preco = float (input('Informe o preço do produto: '))

    mostrar_membros(p2)

    p2.preco += p2.preco * 10 / 100

    mostrar_membros(p2)



main()