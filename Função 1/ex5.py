# 5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.

def preco():
    preco_antigo = float(input('Informe o preço antigo do produto: '))
    preco_novo = float(input('Informe o preço novo do produto: '))

    r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo

    print(f'O percentual de acrésimo entre os valores é de {r:.1f}%')

def main():
    preco()

main()