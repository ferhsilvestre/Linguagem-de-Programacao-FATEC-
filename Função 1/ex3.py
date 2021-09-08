# 3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.

def divisiveis():
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))
    qntd = 0
    txt = 'Números divisíveis: '

    for i in range(b, c + 1):
        if i % a == 0:
            qntd += 1
            txt += str(i) + ' '
    
    print(f'A quantidade de números divisíveis por {a} no intervalo entre {b} e {c} foi: {qntd} \n{txt}')

def main():
    divisiveis()

main()
    