# 7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.

def fatorial():
    lista_A = []
    lista_B = []
    for i in range(5):
        n = int(input('Insira um número inteiro: '))
        lista_A.append(n)
        fat = 1
        for j in range(1, n + 1):
            fat *= j
        lista_B.append(fat)
    
    return lista_B

def main():
    print(fatorial())

main()
    