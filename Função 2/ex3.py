# 3. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.

def reajuste(x):
    preco_novo = x + (x * 0.09)
    print(f'O novo preço reajustado em 9% do produto informado é de R$ {preco_novo:.2f}')

def main():
    preco = float(input('Informe o preço do produto para reajuste: R$ '))
    reajuste(preco)

main()