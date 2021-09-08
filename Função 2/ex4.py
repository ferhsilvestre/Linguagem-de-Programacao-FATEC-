# 4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário.

def reajuste(x, y):
    preco_novo = x + (x * y / 100)
    print(f'O novo preço reajustado em {y}% do produto informado é de R$ {preco_novo:.2f}')

def main():
    preco = float(input('Informe o preço do produto para reajuste: R$ '))
    aumento = float(input('Informe a porcentagem de reajuste do produto: '))
    reajuste(preco, aumento)

main()