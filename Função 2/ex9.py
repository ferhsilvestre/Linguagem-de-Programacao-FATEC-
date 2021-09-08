# 9. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.

def nome_ana(x):
    print(x == 'Ana')

def main():
    nome = input("Entre com um nome: ").strip().capitalize()
    nome_ana(nome)

main()

