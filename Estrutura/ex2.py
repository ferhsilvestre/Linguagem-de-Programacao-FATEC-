# 2. Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço.

class Tipo_Produto:

    codigo = 0

    nome = ''

    preco = 0.0



def mostrar_membros(p):

    print(f'Código: {p.codigo} \tNome: {p.nome} \tPreço R$ {p.preco:.2f}')



def main():

    #1º passo, inicializar uma variável que representará a estrutura/Tipo_Produto

    vet_produtos = []

    for i in range(2):

        p1 = Tipo_Produto()

        p1.codigo = int (input('Informe o código do produto: '))

        p1.nome = input('Informe o nome do produto: ')

        p1.preco = float (input('Informe o preço do produto: '))

        p1.preco = p1.preco + p1.preco * 10 / 100

        vet_produtos.append(p1)



    for i in range(len(vet_produtos)):

        mostrar_membros(vet_produtos[i])



main()   