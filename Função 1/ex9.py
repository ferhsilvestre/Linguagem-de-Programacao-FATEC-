# 9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.

def contar():    
    for i in range (5):
        valor = int(input('Insira um número inteiro: '))

        if i == 0:
            maior = menor = valor
        elif valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        
    print(f'O maior valor encontrado é {maior}, e o menor valor encontrado é {menor}')

def main():
    contar()

main()

        