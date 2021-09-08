# 5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.

def par_impar():
    n = int(input('Insira um número inteiro: '))
    if n % 2 == 0:
        return n, 'par'
    else:
        return n, 'ímpar'

def main():
    numero, resultado = par_impar()
    print(f'O número {numero} é {resultado}')

main()